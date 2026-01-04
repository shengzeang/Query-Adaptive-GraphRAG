# from vllm import LLM, SamplingParams
import torch
import json
import numpy as np
from transformers import AutoTokenizer
from utils import load_dataset, normalize_question, build_qa_prompt, compute_f1
from pathlib import Path
from itertools import chain
from tqdm import tqdm
import pickle

# from raptor import RetrievalAugmentationConfig, RetrievalAugmentation
from raptor import Builder, BuilderConfig, Retriever, RetrieverConfig
from model_for_test import LLAMASummarizationModel, LLAMAQAModel, SBertEmbeddingModel, MLP

eval_dataset = load_dataset("../inputs/graphrag-bench/OE.json")

tree_num_layers = 2

model_name = 'Qwen/Qwen2.5-7B-Instruct'
tokenizer = AutoTokenizer.from_pretrained(model_name)
retriever_config = RetrieverConfig(qa_model=LLAMAQAModel(model_name),
                                  embedding_model=SBertEmbeddingModel())

prefix_prompt = "You are given an open-ended question that may require integrating information from multiple knowledge domains or conceptual subfields.\
        Your task is to produce a detailed, comprehensive, and logically coherent response that demonstrates deep understanding, \
            factual accuracy, and clear organization.\n"
query_prompt = "Answer the question based on the given context.\n Question: "

router = MLP(in_feats=768, hidden=64, out_feats=tree_num_layers+1, n_layers=3, dropout=0.5).to(torch.device("cuda:0"))
optimizer = torch.optim.Adam(router.parameters(), lr=0.01, weight_decay=5e-5)
router.load_state_dict(torch.load("router.pth"))

f = open("sum_tree.pkl", "rb")
tree = pickle.load(f)
print(tree.num_layers)

for epoch in range(1):
    f1_blend = []
    # collect predictions in evaluator-compatible format
    predictions = {}
    for ex in tqdm(eval_dataset):
        answers = ex["Answer"]

        q = f"{normalize_question(ex['Question'])}"
        q_prompt = f"{query_prompt}{q}\nAnswer:"

        retriever = Retriever(retriever_config, tree)

        user_prompt = [prefix_prompt]
        user_prompt.append(q_prompt)
        user_prompt = " ".join(user_prompt)

        q_embedding = torch.from_numpy(retriever.retriever.create_embedding(q_prompt)).to(torch.device("cuda:0"))
        coefficient_tensor = router(q_embedding)
        choice = torch.argmax(coefficient_tensor).item()
        # choice = 2

        res = retriever.answer_question(question=user_prompt, start_layer=choice, num_layers=choice+1, collapse_tree=False)
        f1 = max([compute_f1(res, answer, tokenizer) for answer in answers])
        f1_blend.append(f1)

        # Save the model response in the predictions dict in the format expected by evaluator.py
        # Use the example's index if present, otherwise use incremental integer keys.
        idx = ex.get("_idx") if isinstance(ex, dict) and ex.get("_idx") is not None else len(predictions)
        predictions[str(idx)] = {"prediction": f"{res}"}

    print("---------------Result Summary---------------------")
    print(f"F1: {np.mean(f1_blend)}")
    # write predictions to GraphRAG-Bench_OE.json in the current working directory
    out_path = Path("../outputs/GraphRAG-Bench_OE.json")
    try:
        with open(out_path, 'w', encoding='utf-8') as out_f:
            json.dump(predictions, out_f, ensure_ascii=False, indent=2)
        print(f"Wrote predictions to {out_path.resolve()}")
    except Exception as e:
        print(f"Failed to write predictions file: {e}")
f.close()

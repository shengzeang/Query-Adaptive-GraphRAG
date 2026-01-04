# from vllm import LLM, SamplingParams
import torch
import json
import numpy as np
from transformers import AutoTokenizer
from utils import load_dataset, normalize_question, build_qa_prompt, compute_f1
from pathlib import Path
from itertools import chain
from tqdm import tqdm

# from raptor import RetrievalAugmentationConfig, RetrievalAugmentation
from raptor import Builder, BuilderConfig, Retriever, RetrieverConfig
from model_for_test import LLAMASummarizationModel, LLAMAQAModel, SBertEmbeddingModel, MLP

eval_dataset = load_dataset("./inputs/hotpot_train.json")

tree_num_layers = 2

model_name = 'Qwen/Qwen2.5-7B-Instruct'
tokenizer = AutoTokenizer.from_pretrained(model_name)
builder_config = BuilderConfig(summarization_model=LLAMASummarizationModel(model_name),
                    embedding_model=SBertEmbeddingModel(),
                    tb_num_layers=tree_num_layers)
retriever_config = RetrieverConfig(qa_model=LLAMAQAModel(model_name),
                                  embedding_model=SBertEmbeddingModel(),
                                  tr_start_layer=0,
                                  tr_num_layers=1)

prefix_prompt = "Answer the question based on the given passages. Only give me the answer and do not output any other words.\n\nThe following are given passages.\n"
query_prompt = f"\n\nAnswer the question based on the given passages. Answer the question within 5 words. Do NOT repeat the question or output any other words. Question: "

train_data = None
idx = -1
mask = torch.ones(len(eval_dataset[2000]))
for epoch in range(1):
    f1_blend = []
    for ex in tqdm(eval_dataset[2000]):
        answers = ex["answers"]
        idx += 1

        doc_prompts, q_prompt = build_qa_prompt(ex, query_prompt)

        builder = Builder(builder_config)
        tree = builder.add_documents(" ".join(doc_prompts))
        if tree.num_layers != tree_num_layers:
            print(f'Constructed tree only has {tree.num_layers} layers')
            mask[idx] = 0.
            continue

        retriever = Retriever(retriever_config, tree)

        user_prompt = [prefix_prompt]
        user_prompt.append(q_prompt)
        user_prompt = " ".join(user_prompt)

        res_list = []
        for i in range(tree_num_layers+1):
            res = retriever.answer_question(question=user_prompt, start_layer=i, num_layers=i+1, collapse_tree=False)
            res_list.append(max([compute_f1(res, answer[0], tokenizer) for answer in answers]))

        if train_data is None:
            train_data = torch.FloatTensor(res_list).view(1,-1)
        else:
            train_data = torch.cat((train_data, torch.FloatTensor(res_list).view(1,-1)), dim=0)

        f1 = max([res for res in res_list])
        f1_blend.append(f1)

        torch.save(train_data, "hotpot_train.pt")
        torch.save(mask, "train_mask_train.pt")

    print("---------------Result Summary---------------------")
    print(f"F1: {np.mean(f1_blend)}")

torch.save(train_data, "hotpot_train.pt")
torch.save(mask, "train_mask_train.pt")
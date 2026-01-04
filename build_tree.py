import torch
# from vllm import LLM, SamplingParams
import json
import numpy as np
from utils import load_dataset, normalize_question, build_qa_prompt, compute_f1, combine_input_prompt_chunks
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForCausalLM
from tqdm import tqdm

# from raptor import RetrievalAugmentationConfig, RetrievalAugmentation
from raptor import Builder, BuilderConfig, Retriever, RetrieverConfig
from model_for_test import DeepseekSummarizationModel, DeepseekQAModel, SBertEmbeddingModel, MLP


for i in tqdm(range(1,21)):
    tree_num_layers = 2
    builder_config = BuilderConfig(summarization_model=DeepseekSummarizationModel(),
                        embedding_model=SBertEmbeddingModel(),
                        tb_num_layers=tree_num_layers)

    builder = Builder(builder_config)
    with open(f"./inputs/graphrag-bench/textbooks/textbook{i}/textbook{i}.md") as f:
        doc = f.read()
        tree = builder.add_documents(doc)
        builder.save(f"./trees/graphrag_bench_tree_{i}_ds.pt")

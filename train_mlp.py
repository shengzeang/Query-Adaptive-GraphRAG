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

embedding_model = SBertEmbeddingModel()

router_device = torch.device("cuda:0")
router = MLP(in_feats=768, hidden=384, out_feats=tree_num_layers+1, n_layers=3, dropout=0.5).to(router_device)
optimizer = torch.optim.Adam(router.parameters(), lr=0.01, weight_decay=5e-4)

res_list_set = torch.load("hotpot_train.pt")
train_mask = torch.load("train_mask_train.pt")
# print(train_mask)
# print(res_list_set)

max_f1 = 0.
for epoch in range(10):
    f1_blend = []
    f1_max = []
    acc_cnt = 0
    total_cnt = 0
    i = -1
    loss = 0.
    for j, ex in tqdm(enumerate(eval_dataset[:3500])):
        if train_mask[j] == 0:
            continue
        i += 1
        _, q_prompt = build_qa_prompt(ex, "")

        q_embedding = torch.from_numpy(embedding_model.create_embedding(q_prompt)).to(router_device)
        # q_embedding = embedding_list[i, :]
        # print(q_embedding)
        coefficient_tensor = router(q_embedding)

        res_list = res_list_set[i, :tree_num_layers+1]
        choice = torch.argmax(coefficient_tensor).item()
        choice_max = torch.argmax(res_list).item()

        # res_tensor = torch.nn.functional.normalize(res_list, dim=0).to(router_device)
        res_tensor = torch.nn.functional.softmax(res_list, dim=0).to(router_device)
        # print(coefficient_tensor, res_tensor)
        pred_score = torch.mul(coefficient_tensor, res_tensor).sum()
        max_score = res_list[choice_max]
        if max_score == 0:
            continue
        single_loss = (1 - pred_score) * (1 / max_score)
        # single_loss = 1 - pred_score
        # print(single_loss.item())
        loss += single_loss

        total_cnt += 1
        if choice == choice_max:
            acc_cnt += 1

        f1 = res_list[choice]
        f1_blend.append(f1)
        f1_max.append(res_list[choice_max])

    loss /= train_mask.sum()
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    mean_f1 = np.mean(f1_blend)
    print(f"Epoch: {epoch+1}, Loss: {np.round(loss.item(), 4)}, F1: {np.mean(f1_blend)}, Accuracy: {np.round(acc_cnt/total_cnt*100, 2)}%, Highest possible F1: {np.mean(f1_max)}")
    if mean_f1 > max_f1:
        max_f1 = mean_f1
        torch.save(router.state_dict(), "router.pth")

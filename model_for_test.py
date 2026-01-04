import torch
import numpy as np
# rom lmcache_vllm.vllm import LLM, SamplingParams
# from vllm import LLM, SamplingParams
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM

from raptor import BaseSummarizationModel, BaseQAModel, BaseEmbeddingModel
import os
from openai import OpenAI


class MLP(torch.nn.Module):
    def __init__(self, in_feats, hidden, out_feats, n_layers, dropout):
        super(MLP, self).__init__()
        self.layers = torch.nn.ModuleList()
        self.n_layers = n_layers
        if n_layers == 1:
            self.layers.append(torch.nn.Linear(in_feats, out_feats))
        else:
            self.layers.append(torch.nn.Linear(in_feats, hidden))
            for _ in range(n_layers - 2):
                self.layers.append(torch.nn.Linear(hidden, hidden))
            self.layers.append(torch.nn.Linear(hidden, out_feats))
        if self.n_layers > 1:
            self.prelu = torch.nn.PReLU()
            self.dropout = torch.nn.Dropout(dropout)
        self.reset_parameters()

    def reset_parameters(self):
        gain = torch.nn.init.calculate_gain("relu")
        for layer in self.layers:
            torch.nn.init.xavier_uniform_(layer.weight, gain=gain)
            torch.nn.init.zeros_(layer.bias)

    def forward(self, x):
        for layer_id, layer in enumerate(self.layers):
            x = layer(x)
            if layer_id < self.n_layers -1:
                x = self.dropout(self.prelu(x))
        # return torch.nn.functional.softmax(x, dim=-1)
        return torch.nn.functional.gumbel_softmax(x, tau=1, hard=True, dim=-1)


class DeepseekSummarizationModel(BaseSummarizationModel):
    def __init__(self):
        self.client = OpenAI(
            api_key="sk-7bd09534c48f4001ad1020ec304fa446",
            base_url="https://api.deepseek.com")

    def summarize(self, context, max_tokens=150):
        prompt = f"Write a summary of the following, including as many key details as possible: {context}:"
        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt},
            ],
            stream=False
        )
        summary = response.choices[0].message.content
        return summary


class LLAMASummarizationModel(BaseSummarizationModel):
    def __init__(self, model_name):
        self.model = AutoModelForCausalLM.from_pretrained(model_name, dtype=torch.bfloat16, device_map="balanced_low_0")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    def summarize(self, context, max_tokens=150):
        prompt = f"Write a summary of the following, including as many key details as possible: {context}:"
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt").to(self.model.device)
        outputs = self.model.generate(
            input_ids,
            attention_mask=torch.ones_like(input_ids),
            max_new_tokens=max_tokens,
            pad_token_id=self.tokenizer.eos_token_id,
            top_k=50,
            do_sample=True,
        )

        generated_tokens = outputs[0][input_ids.shape[-1]:]
        summary = self.tokenizer.decode(generated_tokens, skip_special_tokens=True).strip()
        return summary


class DeepseekQAModel(BaseQAModel):
    def __init__(self):
        self.client = OpenAI(
            api_key="sk-7bd09534c48f4001ad1020ec304fa446",
            base_url="https://api.deepseek.com")

    def answer_question(self, context, question):
        # Prepare the prompt for the model
        prompt = f"Given Context: {context} Give the best full answer to the question: {question}"
        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                {"role": "user", "content": prompt},
            ],
            stream=False
        )
        answer = response.choices[0].message.content
        return answer


class LLAMAQAModel(BaseQAModel):
    def __init__(self, model_name):
        # Initialize the model
        self.model = AutoModelForCausalLM.from_pretrained(model_name, dtype=torch.bfloat16, device_map="balanced_low_0")
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)

    def answer_question(self, context, question):
        # Prepare the prompt for the model
        # prompt = f"Given Context: {context} Give the best full answer to the question: {question}"
        prompt = question
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt").to(self.model.device)
        outputs = self.model.generate(
            input_ids,
            attention_mask=torch.ones_like(input_ids),
            # max_new_tokens=512,
            pad_token_id=self.tokenizer.eos_token_id,
            top_k=50,
            do_sample=False,
        )

        # Generate the answer using the model
        generated_tokens = outputs[0][input_ids.shape[-1]:]
        answer = self.tokenizer.decode(generated_tokens, skip_special_tokens=True).strip()
        return answer

        '''ttft = outputs[0].metrics.first_token_time-outputs[0].metrics.first_scheduled_time
        print(f"TTFT: {np.round(ttft, 4)}s")

        # Extract and return the generated answer
        answer = outputs[0].outputs[0].text.strip()
        return answer'''


class SBertEmbeddingModel(BaseEmbeddingModel):
    def __init__(self, model_name="sentence-transformers/multi-qa-mpnet-base-cos-v1"):
        self.model = SentenceTransformer(model_name)

    def create_embedding(self, text):
        return self.model.encode(text)


'''class SBertEmbeddingModel(BaseEmbeddingModel):
    def __init__(self, model_name: str = "Qwen/Qwen2.5-3B"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto", trust_remote_code=True)

    def create_embedding(self, text: str):
        # 使用 transformers 模型计算 hidden states，然后平均池化（按 attention mask）
        inputs = self.tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
            max_length=2048,
        )

        device = next(self.model.parameters()).device
        input_ids = inputs["input_ids"].to(device)
        attention_mask = inputs.get("attention_mask")
        if attention_mask is not None:
            attention_mask = attention_mask.to(device)

        with torch.no_grad():
            outputs = self.model(input_ids=input_ids, attention_mask=attention_mask, output_hidden_states=True, return_dict=True)
            last_hidden = getattr(outputs, "last_hidden_state", None)
            if last_hidden is None:
                hidden_states = outputs.hidden_states
                last_hidden = hidden_states[-1]

            # attention-aware mean pooling
            if attention_mask is None:
                pooled = last_hidden.mean(dim=1)
            else:
                mask = attention_mask.unsqueeze(-1).type_as(last_hidden)
                summed = (last_hidden * mask).sum(dim=1)
                counts = mask.sum(dim=1).clamp(min=1e-9)
                pooled = summed / counts

        vec = pooled[0].cpu().numpy()
        # L2 normalize
        norm = np.linalg.norm(vec)
        if norm > 0:
            vec = vec / norm
        return vec'''

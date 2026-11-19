"""KGQA metrics (MuSiQue / 2WikiMQA / HotpotQA), following the evaluation code of
"In-depth Analysis of Graph-based RAG in a Unified Framework" (the setting the paper builds on):

* Accuracy: 1 if the normalised gold answer is a substring of the normalised prediction.
* Recall:   token-level recall of the gold answer in the prediction.

Both take the best score over all gold answer aliases and are reported x100.
"""
import re
import string
from collections import Counter
from typing import Dict, Iterable, List, Sequence


_PUNCT = set(string.punctuation)


def normalize_answer(s: str) -> str:
    s = s.lower()
    s = "".join(ch for ch in s if ch not in _PUNCT)
    s = re.sub(r"\b(a|an|the)\b", " ", s)
    return " ".join(s.split())


def accuracy(prediction: str, gold: str) -> float:
    g, p = normalize_answer(gold), normalize_answer(prediction)
    if not g:
        return 0.0
    return float(g in p)


def token_recall(prediction: str, gold: str) -> float:
    g, p = normalize_answer(gold), normalize_answer(prediction)
    if g in ("yes", "no", "noanswer") or p in ("yes", "no", "noanswer"):
        if g != p:
            return 0.0
    g_tokens, p_tokens = g.split(), p.split()
    if not g_tokens or not p_tokens:
        return 0.0
    common = sum((Counter(g_tokens) & Counter(p_tokens)).values())
    return common / len(g_tokens)


def score_example(prediction: str, golds: Sequence[str]) -> Dict[str, float]:
    return {
        "acc": max((accuracy(prediction, g) for g in golds), default=0.0),
        "recall": max((token_recall(prediction, g) for g in golds), default=0.0),
    }


def aggregate(scores: Iterable[Dict[str, float]]) -> Dict[str, float]:
    scores = list(scores)
    if not scores:
        return {"acc": 0.0, "recall": 0.0, "n": 0}
    return {
        "acc": 100 * sum(s["acc"] for s in scores) / len(scores),
        "recall": 100 * sum(s["recall"] for s in scores) / len(scores),
        "n": len(scores),
    }

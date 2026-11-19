"""GraphRAG-Bench evaluation: a faithful port of the official ``evaluator.py``
(https://github.com/birfly/GraphRAG-Bench), with two deliberate differences:

* the LLM judge is configurable (default: DeepSeek flash via ``DEEPSEEK_API_KEY``; the official
  script hard-codes ``gpt-4o``). Prompts, ``max_tokens=5`` and ``temperature=0`` are unchanged;
* judge calls run concurrently (this does not change any score).

Prediction file format (one per task, e.g. ``GraphRAG-Bench_FB.json``)::

    {"0": {"prediction": "RATIONALE: ... ANSWER: ..."}, "1": {...}, ...}

Scoring rules (unchanged from the official script): MC / TF answers by exact match, MS answers by
set comparison of the option letters (1 / 0.5 for a strict subset / 0), FB and OE answers and all
rationales by the LLM judge (0 / 0.5 / 1), and AR = the combination of answer and rationale score.
"""
import json
from pathlib import Path
from typing import Callable, Dict, List

from .data import BENCH_TASKS, load_bench_questions
from .llm import ChatLLM, parallel_map

QUESTION_TYPES = ["FB", "MC", "MS", "OE", "TF"]


def extract_feature(text: str):
    if "Please answer the following" in text:
        text = text.split("Please answer the following")[0].strip()
    parts = text.split("ANSWER:")
    if len(parts) < 2:
        return "", ""
    answer = parts[1].strip().split("\n")[0]
    rationale_text = parts[0].strip()
    if "RATIONALE:" in rationale_text:
        rationale = rationale_text.split("RATIONALE:")[1].strip()
    else:
        rationale = rationale_text.strip()
    return [rationale, answer]


_RATIONALE_PROMPT = """
        You are a strict evaluator. Compare the following two rationales for correctness and completeness:

        Predicted Rationale: {pred}

        Gold Rationale: {gold}

        Please evaluate the predicted rationale in comparison to the gold rationale. Respond with a score between 0 and 1:
        - 1: The predicted rationale fully aligns with the gold rationale.
        - 0.5: The predicted rationale is partially correct but lacks completeness or includes incorrect information.
        - 0: The predicted rationale is incorrect or completely misaligned with the gold rationale.

        only provide the score without any explanation.
        """

_ANSWER_PROMPT = """
            You are a strict evaluator. Compare the following two answers for correctness and completeness:

            Predicted Answer: {pred}

            Gold Answer: {gold}

            Please evaluate the predicted answer in comparison to the gold answer. Respond with a score between 0 and 1:
            - 1: The predicted answer fully aligns with the gold answer.
            - 0.5: The predicted answer is partially correct but lacks completeness or includes incorrect information.
            - 0: The predicted answer is incorrect or completely misaligned with the gold answer.

            only provide the score without any explanation.
            """


class Judge:
    def __init__(self, llm: ChatLLM = None, workers: int = 16):
        self.llm = llm or ChatLLM.from_role("judge")
        self.workers = workers

    def _score(self, prompt: str) -> float:
        text = self.llm.chat(prompt, max_tokens=5, temperature=0.0, system=None)
        try:
            return float(text)
        except ValueError:
            return 0.0

    def rationale(self, pred: str, gold: str) -> float:
        return self._score(_RATIONALE_PROMPT.format(pred=pred, gold=gold))

    def answer(self, pred: str, gold: str) -> float:
        return self._score(_ANSWER_PROMPT.format(pred=pred, gold=gold))


def calculate_ar_score(answer_score: float, rationale_score: float) -> float:
    if answer_score == 1 and rationale_score == 1:
        return 1.0
    elif answer_score == 1 and rationale_score == 0.5:
        return 0.5
    elif answer_score == 1 and rationale_score == 0:
        return 0.0
    elif answer_score == 0 and rationale_score == 1:
        return 0.5
    elif answer_score == 0 and rationale_score == 0.5:
        return 0.25
    return 0.0


def _answer_score_rule(type_: str, item: Dict, judge: Judge) -> float:
    if type_ in ("MC", "TF"):
        return 1.0 if item["predict_answer"] == item["answer"] else 0.0
    if type_ == "MS":
        correct, predicted = set(item["answer"]), set(item["predict_answer"])
        if predicted == correct:
            return 1.0
        if predicted.issubset(correct):
            return 0.5
        return 0.0
    return judge.answer(item["predict_answer"], item["answer"])  # FB, OE


def score_task(type_: str, items: List[Dict], judge: Judge) -> List[Dict]:
    def one(item):
        item = dict(item)
        item["rationale_score"] = judge.rationale(item["predict_rationale"], item["rationale"])
        item["answer_score"] = _answer_score_rule(type_, item, judge)
        item["ar_score"] = calculate_ar_score(item["answer_score"], item["rationale_score"])
        return item

    return parallel_map(one, items, workers=judge.workers)


def merge_with_gold(type_: str, gold: List[Dict], predictions: List[str]) -> List[Dict]:
    if len(gold) != len(predictions):
        raise ValueError(f"{type_}: {len(predictions)} predictions for {len(gold)} questions")
    merged = []
    for orig, pred in zip(gold, predictions):
        rationale, answer = extract_feature(pred)
        merged.append(
            {
                "predict_rationale": rationale,
                "predict_answer": answer,
                "rationale": orig["Rationale"],
                "answer": orig["Answer"],
                "topic": orig["Level-1 Topic"],
            }
        )
    return merged


def _acc_dict() -> Dict:
    return {"rationale_score": 0.0, "answer_score": 0.0, "ar_score": 0.0, "count": 0}


def _add(acc: Dict, item: Dict) -> None:
    acc["rationale_score"] += item["rationale_score"]
    acc["answer_score"] += item["answer_score"]
    acc["ar_score"] += item["ar_score"]
    acc["count"] += 1


def _mean(acc: Dict) -> Dict:
    if acc["count"]:
        for k in ("rationale_score", "answer_score", "ar_score"):
            acc[k] /= acc["count"]
    return acc


def run_eval(gold_by_type: Dict[str, List[Dict]], preds_by_type: Dict[str, List[str]], judge: Judge) -> Dict:
    """Same output structure as the official ``run_eval``: total / by_type / by_topic."""
    types = [t for t in QUESTION_TYPES if t in preds_by_type]
    results = {"total": _acc_dict(), "by_type": {t: _acc_dict() for t in types}, "by_topic": {}}
    details = {}
    for t in types:
        scored = score_task(t, merge_with_gold(t, gold_by_type[t], preds_by_type[t]), judge)
        details[t] = scored
        for item in scored:
            _add(results["total"], item)
            _add(results["by_type"][t], item)
            _add(results["by_topic"].setdefault(item["topic"], _acc_dict()), item)
    _mean(results["total"])
    for acc in results["by_type"].values():
        _mean(acc)
    for acc in results["by_topic"].values():
        _mean(acc)
    results["details"] = details
    return results


def load_predictions(pred_dir: str) -> Dict[str, List[str]]:
    """Read ``GraphRAG-Bench_<TYPE>.json`` files (keys are question indices, in order)."""
    out = {}
    for t in QUESTION_TYPES:
        path = Path(pred_dir) / f"GraphRAG-Bench_{t}.json"
        if path.exists():
            data = json.loads(path.read_text(encoding="utf-8", errors="ignore"))
            out[t] = [data[k]["prediction"] for k in sorted(data, key=int)]
    return out


def evaluate_dir(pred_dir: str, judge: Judge = None, limit: int = None) -> Dict:
    preds = load_predictions(pred_dir)
    if not preds:
        raise FileNotFoundError(f"no GraphRAG-Bench_<TYPE>.json files in {pred_dir}")
    gold = {t: load_bench_questions(t, limit) for t in preds}
    return run_eval(gold, preds, judge or Judge())

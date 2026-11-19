"""Why are questions answered wrongly, although the retrieved context holds the gold answer?

Reads the per-question results of ``run_kgqa.py`` (``outputs/kgqa/<dataset>.jsonl``), reloads each question's cached RAPTOR
tree and repeats the retrieval of every method (no LLM call, CPU only; the generation prompt is not stored in the results,
the retrieved context is recomputed). Every question with ``acc == 0`` is put into one category, in this order:

* ``retrieval miss``     the normalised gold answer is not in the context (nothing the prompt could fix)
* ``empty``              the model returned nothing
* ``refusal``            the answer is in the context but the model says it is not stated / cannot be answered
* ``yes/no wrong``       a yes/no question answered with the wrong one
* ``near miss``          token recall of the gold answer >= 0.5 (partial name, other wording): mostly an answer-format issue
* ``wrong span``         the prediction is itself a piece of the context: the model picked another entity / passage
* ``not from context``   the prediction is not in the context: inferred, computed or invented

A context that holds the gold string does not prove that it holds the evidence (multi-hop questions, short answers that
occur by chance), so ``wrong span`` / ``not from context`` are an upper bound of the prompt/generation errors. Among the
answer-in-context failures the share whose gold string occurs only in a summary node (not in any leaf chunk) is also given.
``--samples N`` writes N failures per category, with the context, to ``<out stem>_samples.jsonl`` for reading by hand.

    python scripts/analyze_failures.py --results outputs/kgqa/{musique,2wikimqa,hotpotqa}.jsonl --cache-dir indexes \
        --samples 30 --out outputs/failures.json

The trees are looked up like ``run_kgqa.py`` stores them (namespace = dataset, key = ``<id>|<tree tag>``), so the encoder / tree
settings and the summariser model (``SUMMARIZER_MODEL`` / ``BACKBONE_MODEL``, or ``--summarizer-model``) must be those used to
build them; ``--top-k`` and, for the ``raptor`` / ``raptor-qa`` rows, the env variable ``RETRIEVAL`` (collapse | traverse; rows
without a ``retrieval`` field are traverse) must be those of the run. Query embeddings are recomputed (near-ties may resolve differently).
For ``raptor-qa[...]`` the level the router chose in the run is reused.
"""
import argparse
import json
import pickle
import random
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np
from tqdm import tqdm

from qa_graphrag import NUM_TREE_LAYERS
from qa_graphrag.data import read_jsonl
from qa_graphrag.embedding import DEFAULT_ENCODER, SBertEncoder
from qa_graphrag.index import cache_path
from qa_graphrag.metrics import normalize_answer
from qa_graphrag.pipeline import LEVEL_METHOD, QueryRunner
from qa_graphrag.retrieval import RetrievalSettings, TreeIndex
from qa_graphrag.runtime import tree_tag
from qa_graphrag.settings import get_llm_spec

CATEGORIES = ("retrieval miss", "empty", "refusal", "yes/no wrong", "near miss", "wrong span", "not from context")
REFUSAL = re.compile(
    r"\b(not (?:provided|mentioned|specified|stated|available|found|clear|given|contain\w*)|no (?:information|mention|data)|"
    r"cannot|can't|can not|unable|unknown|insufficient|does not (?:say|specify|mention|provide|contain)|"
    r"doesn't (?:say|specify|mention|provide|contain))", re.I)


def contains_answer(text_norm: str, golds_norm) -> bool:
    return any(g and g in text_norm for g in golds_norm)


def classify_failure(prediction: str, golds_norm, recall: float, context_norm: str) -> str:
    """Category of one wrong answer (``acc == 0``); ``golds_norm`` and ``context_norm`` are normalised."""
    if not contains_answer(context_norm, golds_norm):
        return "retrieval miss"
    p = normalize_answer(prediction)
    if not p:
        return "empty"
    if REFUSAL.search(prediction):
        return "refusal"
    if any(g in ("yes", "no") for g in golds_norm):
        return "yes/no wrong"
    if recall >= 0.5:
        return "near miss"
    return "wrong span" if p in context_norm else "not from context"


def retrieve(index: TreeIndex, runner: QueryRunner, method: str, level, question: str):
    """``(context, text of the leaf chunks in it)`` of one method; ``None`` for a method that cannot be reproduced."""
    base = method.split("[")[0]
    if base in ("bm25", "tfidf"):
        ctx = runner.retrieve(base, question)[0].context
        return ctx, ctx
    if base == "raptor-collapsed":
        nodes, ctx = index.retriever.retrieve_information_collapse_tree(question, index.settings.top_k, index.settings.max_tokens)
    elif base in ("raptor", "raptor-qa"):      # in the retrieval mode of the run (env RETRIEVAL, as for the run itself)
        k = index.max_level if base == "raptor" else level
        if k is None:
            return None
        nodes, ctx = index._start(question, k)
    else:
        m = LEVEL_METHOD.match(base)
        if not m:
            return None
        nodes, ctx = index._traverse(question, index.clamp(int(m.group(1))))
    leaf_ids = {n.index for n in index.tree.layer_to_nodes[0]}
    return ctx, "\n".join(n.text for n in nodes if n.index in leaf_ids)


def gold_window(context: str, golds, width: int = 300) -> str:
    low = context.lower()
    for g in golds:
        i = low.find(g.lower()) if g else -1
        if i >= 0:
            return context[max(0, i - width): i + len(g) + width]
    return context[: 2 * width]


def analyse_question(index: TreeIndex, runner: QueryRunner, row: dict, methods) -> list:
    golds, golds_norm = row["answers"], [normalize_answer(a) for a in row["answers"]]
    found = []
    for m, o in row["outs"].items():
        if methods and m.split("[")[0] not in methods and m not in methods:
            continue
        got = retrieve(index, runner, m, o.get("level"), row["question"])
        if got is None:
            continue
        ctx, leaf_text = got
        ctx_norm = normalize_answer(ctx)
        has = contains_answer(ctx_norm, golds_norm)
        wrong = not o["acc"]
        found.append({
            "method": m, "acc": float(o["acc"]), "has_answer": has,
            "category": classify_failure(o["prediction"], golds_norm, o["recall"], ctx_norm) if wrong else None,
            "only_summary": bool(has and not contains_answer(normalize_answer(leaf_text), golds_norm)),
            "words": len(o["prediction"].split()), "level": o.get("level"), "prediction": o["prediction"],
            "context": ctx, "window": gold_window(ctx, golds) if has else None,
        })
    return found


def summarize(items: list) -> dict:
    n = len(items)
    has = [i for i in items if i["has_answer"]]
    miss = [i for i in items if not i["has_answer"]]
    fails = [i for i in items if i["category"]]
    ctx_fails = [i for i in has if i["category"]]
    mean = lambda xs: float(np.mean(xs)) if len(xs) else None
    return {
        "n": n, "acc": mean([i["acc"] for i in items]),
        "answer_in_context": len(has) / n if n else None,
        "acc_if_answer_in_context": mean([i["acc"] for i in has]),
        "acc_if_answer_not_in_context": mean([i["acc"] for i in miss]),
        "failures": len(fails),
        "categories": {c: sum(i["category"] == c for i in fails) / len(fails) if fails else 0.0 for c in CATEGORIES},
        "answer_in_context_failures": len(ctx_fails),
        "failures_with_gold_only_in_summary": mean([i["only_summary"] for i in ctx_fails]),
        "words_correct": mean([i["words"] for i in items if not i["category"]]),
        "words_wrong": mean([i["words"] for i in fails]),
    }


def pct(x) -> str:
    return "  -  " if x is None else f"{100 * x:5.1f}"


def print_summary(name: str, s: dict) -> None:
    print(f"\n== {name}   n={s['n']}  acc {pct(s['acc'])}  failures {s['failures']}")
    print(f"   answer in context {pct(s['answer_in_context'])}%   acc if it is {pct(s['acc_if_answer_in_context'])}%   "
          f"acc if it is not {pct(s['acc_if_answer_not_in_context'])}%")
    print("   failures by category: " + "  ".join(f"{c} {pct(v)}%" for c, v in s["categories"].items()))
    print(f"   of the {s['answer_in_context_failures']} failures with the answer in the context, gold only in a summary node: "
          f"{pct(s['failures_with_gold_only_in_summary'])}%;  answer length (words) correct {s['words_correct'] or 0:.1f} / wrong {s['words_wrong'] or 0:.1f}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--results", nargs="+", required=True, help="run_kgqa.py result files (<dataset>.jsonl)")
    ap.add_argument("--methods", nargs="*", default=None, help="only these methods (e.g. raptor raptor-qa); default: all in the files")
    ap.add_argument("--n", type=int, default=None, help="questions sampled per file (default: all)")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--top-k", type=int, default=RetrievalSettings.top_k, help="must be the top-k of the run")
    ap.add_argument("--samples", type=int, default=0, help="failures per category written for manual reading")
    ap.add_argument("--cache-dir", default="indexes")
    ap.add_argument("--encoder", default=DEFAULT_ENCODER)
    ap.add_argument("--device", default=None)
    ap.add_argument("--tree-layers", type=int, default=NUM_TREE_LAYERS)
    ap.add_argument("--chunk-tokens", type=int, default=100)
    ap.add_argument("--summary-tokens", type=int, default=100)
    ap.add_argument("--summarizer-model", default=None, help="model name inside the tree tag (default: from the environment)")
    ap.add_argument("--out", default="outputs/failures.json")
    args = ap.parse_args()

    tag = tree_tag(args.encoder, args.summarizer_model or get_llm_spec("summarizer").model, args.tree_layers,
                   args.chunk_tokens, args.summary_tokens)
    print(f"tree tag: {tag}")
    encoder = SBertEncoder(args.encoder, device=args.device)
    settings = RetrievalSettings(top_k=args.top_k)

    by_group, missing = {}, {}
    for path in args.results:
        dataset = Path(path).stem
        rows = read_jsonl(path)
        if args.n and args.n < len(rows):
            rows = random.Random(args.seed).sample(rows, args.n)
        for row in tqdm(rows, desc=dataset, mininterval=10):
            tree_path = cache_path(args.cache_dir, dataset, f"{row['id']}|{tag}")
            if not tree_path.exists():
                missing[dataset] = missing.get(dataset, 0) + 1
                continue
            with open(tree_path, "rb") as f:
                index = TreeIndex(pickle.load(f), encoder, settings)
            for item in analyse_question(index, QueryRunner(index, None), row, set(args.methods or [])):
                item.update(id=str(row["id"]), question=row["question"], gold=row["answers"])
                by_group.setdefault((dataset, item["method"]), []).append(item)
    if missing:
        print(f"trees not found (skipped): {missing}")
    if not by_group:
        sys.exit(f"nothing analysed: check --cache-dir {args.cache_dir}, the tree tag above (--summarizer-model) and --methods")

    result = {"tag": tag, "top_k": args.top_k, "missing": missing, "groups": {}}
    for (dataset, method), items in sorted(by_group.items()):
        result["groups"][f"{dataset}/{method}"] = summarize(items)
        print_summary(f"{dataset} / {method}", result["groups"][f"{dataset}/{method}"])
    for method in sorted({m for _, m in by_group}):
        pooled = [i for (_, m), items in by_group.items() if m == method for i in items]
        result["groups"][f"ALL/{method}"] = summarize(pooled)
        print_summary(f"ALL datasets / {method}", result["groups"][f"ALL/{method}"])

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=1))
    if args.samples:
        rng, path = random.Random(args.seed), out.with_name(out.stem + "_samples.jsonl")
        pool = {}
        for (dataset, _), items in by_group.items():
            for i in items:
                if i["category"]:
                    pool.setdefault(i["category"], []).append({"dataset": dataset, **i})
        with open(path, "w", encoding="utf-8") as f:
            for c in CATEGORIES:
                for i in rng.sample(pool.get(c, []), min(args.samples, len(pool.get(c, [])))):
                    f.write(json.dumps({k: i[k] for k in ("category", "dataset", "method", "id", "level", "question", "gold",
                                                          "prediction", "window", "context")}, ensure_ascii=False) + "\n")
        print(f"\nsamples for reading by hand: {path}  (categories: {dict(Counter(c for c, v in pool.items() for _ in v))})")
    print(f"\nsummary: {out}")


if __name__ == "__main__":
    main()

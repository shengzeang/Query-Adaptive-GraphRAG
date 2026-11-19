"""Does the chunk size favour or hurt BM25 / TF-IDF? (no LLM, no embeddings, no tree: CPU only)

For the KGQA test questions, the per-question corpus is cut into chunks of several sizes (the RAPTOR splitter, as for the
leaves of the trees), BM25 / TF-IDF rank the chunks for the question, and the best chunks are taken until a token budget
is used up (greedy, never beyond the budget, at least one chunk: the rule of ``FlatRetriever``). The score is how often
the normalised gold answer is inside the retrieved text, the measure of ``analyze_failures.py``.

Chunk size and ``top_k`` are not independent: ``top_k`` chunks of ``c`` tokens are ``top_k * c`` tokens of context. The
comparison therefore fixes the TOKEN budget, not ``k``; the budgets 500 / 1000 / 2000 are what ``top_k`` = 5 / 10 / 20
chunks of 100 tokens give. Two reference rows per table:

* ``random``     chunks drawn at random under the same budget: the hits that a string match gets by chance (short answers
                 such as years, numbers and yes/no occur in any text), to be subtracted when reading the other rows;
* ``corpus``     the whole corpus: the ceiling, how often the answer is in the provided paragraphs at all.

    python scripts/measure_chunk_size.py --datasets musique 2wikimqa hotpotqa --n 1000 --out outputs/chunk_size.json

The questions are the test questions of ``run_kgqa.py`` (same seed and specialist split; a smaller ``--n`` is a random subset
of them). ``hit`` is a measure of the retrieval only: it says nothing about whether the generator uses the text well,
and more or longer context also brings more distractors.
"""
import argparse
import json
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np
import tiktoken
from tqdm import tqdm

import qa_graphrag  # noqa: F401  (sets the offline tiktoken cache)
from qa_graphrag.data import KGQA_SOURCES, split_specialist_and_test
from qa_graphrag.index import corpus_text
from qa_graphrag.metrics import normalize_answer
from qa_graphrag.retrieval import FlatRetriever
from raptor.utils import split_text

METHODS = ("bm25", "tfidf")


def contains(text: str, golds_norm) -> bool:
    t = normalize_answer(text)
    return any(g and g in t for g in golds_norm)


def random_context(chunks, counts, budget: int, rng: random.Random) -> str:
    order = list(range(len(chunks)))
    rng.shuffle(order)
    picked, used = [], 0
    for i in order:
        if picked and used + counts[i] > budget:
            break
        picked.append(chunks[i])
        used += counts[i]
    return "\n\n".join(picked)


def measure_question(ex: dict, chunk_sizes, budgets, tokenizer, rng: random.Random, methods=METHODS) -> dict:
    """``{(row, chunk_size, budget): (hit, tokens)}`` for one question; rows: the methods and ``random``;
    the key ``("corpus", 0, 0)`` is the ceiling."""
    golds = [normalize_answer(a) for a in ex["answers"]]
    text = corpus_text(ex["ctxs"])
    out = {("corpus", 0, 0): (contains(text, golds), len(tokenizer.encode(text)))}
    count = lambda t: len(tokenizer.encode(t))
    for size in chunk_sizes:
        chunks = split_text(text, tokenizer, size)
        counts = [count(c) for c in chunks]
        retrievers = {m: FlatRetriever(chunks, m, top_k=len(chunks), max_tokens=0, count_tokens=count) for m in methods}
        for budget in budgets:
            for m, r in retrievers.items():
                r.max_tokens = budget
                ctx = r.retrieve(ex["question"]).context
                out[(m, size, budget)] = (contains(ctx, golds), count(ctx))
            ctx = random_context(chunks, counts, budget, rng)
            out[("random", size, budget)] = (contains(ctx, golds), count(ctx))
    return out


def summarize(per_question: list) -> dict:
    keys = per_question[0].keys()
    return {"|".join(map(str, k)): {"hit": float(np.mean([q[k][0] for q in per_question])),
                                    "tokens": float(np.mean([q[k][1] for q in per_question]))} for k in keys}


def print_table(name: str, s: dict, chunk_sizes, budgets, n: int) -> None:
    corpus = s["corpus|0|0"]
    print(f"\n== {name}   n={n}   corpus {corpus['tokens']:.0f} tokens on average, answer anywhere in it: {100 * corpus['hit']:.1f}%")
    print("   answer in the retrieved text (%), by token budget; in brackets the mean tokens really retrieved")
    print(f"   {'row':8s} {'chunk':>6s} " + "".join(f"{b:>16d}" for b in budgets))
    for row in (*METHODS, "random"):
        for size in chunk_sizes:
            cells = [s[f"{row}|{size}|{b}"] for b in budgets]
            print(f"   {row:8s} {size:6d} " + "".join(f"{100 * c['hit']:9.1f} ({c['tokens']:4.0f})" for c in cells))
        print()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--datasets", nargs="+", default=list(KGQA_SOURCES), choices=list(KGQA_SOURCES))
    ap.add_argument("--n", type=int, default=1000, help="test questions per dataset (as in run_kgqa.py)")
    ap.add_argument("--n-specialist", type=int, default=200)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--chunk-sizes", type=int, nargs="+", default=[50, 100, 200, 400])
    ap.add_argument("--budgets", type=int, nargs="+", default=[500, 1000, 2000])
    ap.add_argument("--out", default="outputs/chunk_size.json")
    args = ap.parse_args()

    tokenizer = tiktoken.get_encoding("cl100k_base")
    result = {"chunk_sizes": args.chunk_sizes, "budgets": args.budgets, "datasets": {}}
    for name in args.datasets:
        _, test = split_specialist_and_test(name, n_specialist=args.n_specialist, n_test=args.n, seed=args.seed)
        rng = random.Random(args.seed)
        per_question = [measure_question(ex, args.chunk_sizes, args.budgets, tokenizer, rng)
                        for ex in tqdm(test, desc=name, mininterval=10)]
        result["datasets"][name] = {"n": len(per_question), "cells": summarize(per_question)}
        print_table(name, result["datasets"][name]["cells"], args.chunk_sizes, args.budgets, len(per_question))
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(json.dumps(result, indent=1))
    print(f"summary: {args.out}")


if __name__ == "__main__":
    main()

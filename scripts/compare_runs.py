"""Compare two GraphRAG-Bench runs question by question (e.g. two settings on the same tree, or two routers).

    python scripts/compare_runs.py outputs/bench_a outputs/bench_b
    # two routers of one run (their directories are raptor-qa_<router name>):
    python scripts/compare_runs.py outputs/bench_x outputs/bench_x --pair raptor-qa_old raptor-qa_new

For every method directory present in both runs (it must hold ``eval_details.json``, written by ``run_bench.py``):

* **scores**: AR / Answer / Rationale per task and in total, A -> B with the difference and a 95% paired-bootstrap
  interval (questions are resampled, the same ones on both sides). ``*`` marks an interval that excludes 0. The interval
  covers question sampling only, not the variation of the LLM judge or of generation;
* **format**: answers without an ``ANSWER:`` tag, empty answers, MS outcomes (exact / 0.5 partial / empty / wrong; an
  empty answer counts as a subset and scores 0.5 in the official scorer) and the True / False split of TF.

Scores are read from the files, nothing is recomputed or judged again.
"""
import argparse
import json
from collections import Counter
from pathlib import Path

import numpy as np

TASKS = ["FB", "MC", "MS", "OE", "TF"]
METRICS = [("ar_score", "AR"), ("answer_score", "Answer"), ("rationale_score", "Rationale")]


def load_run(root):
    runs = {}
    for d in sorted(Path(root).iterdir()):
        f = d / "eval_details.json"
        if d.is_dir() and f.exists():
            runs[d.name] = json.loads(f.read_text(encoding="utf-8"))
    if not runs:
        raise SystemExit(f"no <method>/eval_details.json under {root}")
    return runs


def paired_scores(a_items, b_items, task):
    """(n, len(METRICS)) score arrays of both sides, or None when the two files are not about the same questions."""
    if len(a_items) != len(b_items):
        print(f"  [{task}] skipped: {len(a_items)} vs {len(b_items)} questions")
        return None
    if any(x["answer"] != y["answer"] or x["rationale"] != y["rationale"] for x, y in zip(a_items, b_items)):
        print(f"  [{task}] skipped: the gold data of the two runs differ")
        return None
    pick = lambda items: np.array([[i[k] for k, _ in METRICS] for i in items], dtype=float)
    return pick(a_items), pick(b_items)


def bootstrap_ci(diff, boot, rng, chunk=500):
    n = len(diff)
    means = np.concatenate([diff[rng.integers(0, n, size=(min(chunk, boot - s), n))].mean(axis=1)
                            for s in range(0, boot, chunk)])
    return np.percentile(means, [2.5, 97.5])


def score_table(a_scores, b_scores, boot, rng, la, lb):
    scopes = {t: (a_scores[t], b_scores[t]) for t in TASKS if t in a_scores}
    scopes = {"total": (np.concatenate([v[0] for v in scopes.values()]),
                        np.concatenate([v[1] for v in scopes.values()])), **scopes}
    for name, (a, b) in scopes.items():
        cells = []
        for j, (_, metric) in enumerate(METRICS):
            d = b[:, j] - a[:, j]
            lo, hi = bootstrap_ci(d, boot, rng)
            star = "*" if lo > 0 or hi < 0 else " "
            cells.append(f"{metric} {100*a[:, j].mean():5.1f}->{100*b[:, j].mean():5.1f} "
                         f"d{100*d.mean():+5.1f} [{100*lo:+5.1f},{100*hi:+5.1f}]{star}")
        print(f"  {name:5s} n={len(a):4d} | " + " | ".join(cells))
    print(f"  ({la} -> {lb}; d = {lb} minus {la}; [95% bootstrap interval]; * = excludes 0)")


def format_counts(items, task):
    no_tag = sum(1 for i in items if not i["predict_answer"] and not i["predict_rationale"])
    empty = sum(1 for i in items if not i["predict_answer"]) - no_tag
    out = {"no-tag": no_tag, "empty": empty}
    if task == "MS":
        s = [(i["answer_score"], bool(i["predict_answer"])) for i in items]
        out.update({"exact": sum(1 for v, _ in s if v == 1), "part": sum(1 for v, e in s if v == 0.5 and e),
                    "empty=.5": sum(1 for v, e in s if v == 0.5 and not e), "wrong": sum(1 for v, _ in s if v == 0)})
    return out


def format_report(a_run, b_run, la, lb):
    for t in TASKS:
        if t not in a_run or t not in b_run:
            continue
        ca, cb = format_counts(a_run[t], t), format_counts(b_run[t], t)
        print(f"  {t:3s} " + "  ".join(f"{k} {ca[k]}/{cb[k]}" for k in ca))
    if "TF" in a_run and "TF" in b_run:
        gold, pa, pb = (Counter(i[k] for i in run["TF"]) for run, k in
                        ((a_run, "answer"), (a_run, "predict_answer"), (b_run, "predict_answer")))
        values = [v for v, _ in (gold + pa + pb).most_common(4)]
        show = lambda c: " ".join(f"{v!r}:{c[v]}" for v in values) + (
            f" other:{sum(c.values()) - sum(c[v] for v in values)}" if sum(c.values()) > sum(c[v] for v in values) else "")
        print(f"  TF answers   gold {show(gold)} | {la} {show(pa)} | {lb} {show(pb)}")
    print(f"  (format counts are {la}/{lb}; no-tag = no ANSWER: found, empty = tag present but nothing after it)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("run_a", help="output directory of run A, e.g. outputs/bench_c1200_v1")
    ap.add_argument("run_b", help="output directory of run B, e.g. outputs/bench_c1200_v2")
    ap.add_argument("--methods", nargs="*", help="only these method directories (default: all in both runs)")
    ap.add_argument("--pair", nargs=2, metavar=("METHOD_A", "METHOD_B"),
                    help="compare the method directory METHOD_A of run A with METHOD_B of run B instead of equal names; run A "
                         "and run B may be the same directory, e.g. two routers of one run: --pair raptor-qa_old raptor-qa_new")
    ap.add_argument("--boot", type=int, default=10000, help="bootstrap resamples (default 10000)")
    ap.add_argument("--seed", type=int, default=0)
    args = ap.parse_args()

    runs_a, runs_b = load_run(args.run_a), load_run(args.run_b)
    if args.pair:
        missing = [m for m, runs in zip(args.pair, (runs_a, runs_b)) if m not in runs]
        if missing:
            raise SystemExit(f"not found (needs eval_details.json): {missing}; available: A {sorted(runs_a)}, B {sorted(runs_b)}")
        pairs = [tuple(args.pair)]
    else:
        pairs = [(m, m) for m in runs_a if m in runs_b and (not args.methods or m in args.methods)]
        for m in set(runs_a) ^ set(runs_b):
            print(f"[only in one run, ignored] {m}")
    rng = np.random.default_rng(args.seed)

    for ma, mb in pairs:
        la, lb = (ma, mb) if ma != mb else ("A", "B")   # two different methods: name the sides after them
        print(f"\n== {ma if ma == mb else f'{ma} vs {mb}'}   A={args.run_a}   B={args.run_b}")
        a_run, b_run = runs_a[ma], runs_b[mb]
        a_scores, b_scores = {}, {}
        for t in TASKS:
            if t in a_run and t in b_run:
                pair = paired_scores(a_run[t], b_run[t], t)
                if pair:
                    a_scores[t], b_scores[t] = pair
        if a_scores:
            score_table(a_scores, b_scores, args.boot, rng, la, lb)
        format_report({t: a_run[t] for t in a_scores}, {t: b_run[t] for t in b_scores}, la, lb)


if __name__ == "__main__":
    main()

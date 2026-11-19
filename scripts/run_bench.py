"""GraphRAG-Bench evaluation (FB / MC / MS / TF / OE): BM25, TF-IDF, RAPTOR and RAPTOR-QA (paper Table 5).

    python scripts/build_bench_index.py --out indexes/graphrag_bench_c200.pkl
    python scripts/run_bench.py --tree indexes/graphrag_bench_c200.pkl \
        --methods bm25 tfidf raptor raptor-qa --routers generalist=checkpoints/generalist.pt

Predictions are written in the official format to ``<out>/<method>/GraphRAG-Bench_<TYPE>.json`` and
scored with the official evaluation protocol (``qa_graphrag/bench_eval.py``; judge = DeepSeek flash,
key from ``DEEPSEEK_API_KEY``). Use ``--no-eval`` to only generate, ``--eval-only`` to only score.
"""
import argparse
import json
import pickle
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tqdm import tqdm

from qa_graphrag.bench_eval import QUESTION_TYPES, Judge, evaluate_dir
from qa_graphrag.data import (append_jsonl, load_bench_questions, read_jsonl, refuse_other_prompt, refuse_other_retrieval,
                              refuse_other_top_k, warn_router_retrieval)
from qa_graphrag.llm import parallel_unordered
from qa_graphrag.pipeline import QueryRunner, check_method
from qa_graphrag.prompts import BENCH_MAX_NEW_TOKENS, PROMPT_VERSION, build_bench_prompt, build_bench_query
from qa_graphrag.retrieval import TreeIndex
from qa_graphrag.router import MLPRouter
from qa_graphrag.runtime import add_common_args, make_runtime


def dir_name(method: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", method).strip("_")


def generate(args, rt, index, tasks, variants):
    for method, router in variants:
        runner = QueryRunner(index, rt.generator)
        runner.router = router
        out_dir = Path(args.out) / dir_name(method)
        for task in tasks:
            questions = load_bench_questions(task, args.limit)
            partial = out_dir / f"GraphRAG-Bench_{task}.jsonl"
            refuse_other_prompt(partial, PROMPT_VERSION)
            refuse_other_top_k(partial, args.top_k)
            uses_retrieval_mode = method.split("[")[0] in ("raptor", "raptor-qa")      # bm25 / tfidf do not depend on it
            if uses_retrieval_mode:
                refuse_other_retrieval(partial, rt.settings.retrieval)
            finished = {r["idx"] for r in read_jsonl(partial)} if partial.exists() else set()
            todo = [i for i in range(len(questions)) if i not in finished]

            def run_one(i):
                ex = questions[i]
                try:
                    o = runner.run(
                        method.split("[")[0], build_bench_query(task, ex),
                        prompt_fn=lambda ctx, _q, ex=ex: build_bench_prompt(task, ex, ctx),
                        max_new_tokens=BENCH_MAX_NEW_TOKENS[task],
                    )
                except Exception as e:
                    print(f"[skip {task}#{i}] {type(e).__name__}: {e}")
                    return None
                row = {"idx": i, "prompt": PROMPT_VERSION, "top_k": args.top_k, "prediction": o.prediction, "level": o.level,
                       "preference": o.preference, "num_nodes": o.num_nodes, "times": o.times}
                if uses_retrieval_mode:
                    row["retrieval"] = rt.settings.retrieval
                return row

            for rec in tqdm(parallel_unordered(run_one, todo, workers=args.workers), total=len(todo),
                            desc=f"{method} {task}", mininterval=30):
                if rec:
                    append_jsonl(partial, rec)
            rows = {r["idx"]: r for r in read_jsonl(partial)}
            if len(rows) == len(questions):
                final = {str(i): {k: v for k, v in rows[i].items() if k != "idx"} for i in range(len(questions))}
                (out_dir / f"GraphRAG-Bench_{task}.json").write_text(json.dumps(final, ensure_ascii=False))
            else:
                print(f"{method} {task}: {len(questions) - len(rows)} questions failed, rerun to retry")


def score(args, methods):
    judge = Judge(workers=args.judge_workers)
    summary = {}
    for method in methods:
        out_dir = Path(args.out) / dir_name(method)
        result = evaluate_dir(str(out_dir), judge, args.limit)
        details = result.pop("details")
        (out_dir / "eval.json").write_text(json.dumps(result, indent=1))
        (out_dir / "eval_details.json").write_text(json.dumps(details, ensure_ascii=False))
        summary[method] = {"total": result["total"], **{t: v for t, v in result["by_type"].items()}}
        print(f"\n== {method}")
        for name, v in summary[method].items():
            print(f"  {name:6s} AR {100*v['ar_score']:.2f}  Answer {100*v['answer_score']:.2f}  Rationale {100*v['rationale_score']:.2f}  (n={v['count']})")
    summary_path = Path(args.out) / "summary.json"
    if summary_path.exists():      # keep the methods of earlier invocations on the same --out (e.g. routers added later)
        summary = {**json.loads(summary_path.read_text()), **summary}
    summary_path.write_text(json.dumps(summary, indent=1))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tree", default="indexes/graphrag_bench_c200.pkl")
    ap.add_argument("--methods", nargs="+", default=["bm25", "tfidf", "raptor", "raptor-qa"])
    ap.add_argument("--routers", nargs="*", default=[], help="name=checkpoint pairs used by raptor-qa")
    ap.add_argument("--tasks", nargs="+", default=QUESTION_TYPES, choices=QUESTION_TYPES)
    ap.add_argument("--limit", type=int, default=None, help="only the first N questions of each task (debugging)")
    ap.add_argument("--out", default="outputs/bench")
    ap.add_argument("--no-eval", action="store_true")
    ap.add_argument("--eval-only", action="store_true")
    ap.add_argument("--judge-workers", type=int, default=16)
    ap.add_argument("--max-tokens", type=int, default=None,
                    help="token budget of the retrieved context (default: the KGQA value, 3500). With chunks of more than "
                         "~500 tokens it must grow with them: top-k chunks that do not fit the budget are cut off, so "
                         "1200-token chunks under 3500 tokens leave only 2 of the 5 leaves (run_all.sh sets it)")
    add_common_args(ap)
    args = ap.parse_args()

    for m in args.methods:
        check_method(m)
    routers = {n: MLPRouter.load(p) for n, p in (item.split("=", 1) for item in args.routers)}
    if "raptor-qa" in args.methods and not routers:
        ap.error("raptor-qa needs --routers name=checkpoint")
    variants = []
    for m in args.methods:
        variants += [(f"raptor-qa[{n}]", r) for n, r in routers.items()] if m == "raptor-qa" else [(m, None)]

    if not args.eval_only:
        rt = make_runtime(args)
        if "raptor-qa" in args.methods:
            warn_router_retrieval(routers, rt.settings.retrieval, args.top_k)
        if args.max_tokens:
            rt.settings.max_tokens = args.max_tokens      # used by TreeIndex and by the BM25 / TF-IDF retrievers alike
        with open(args.tree, "rb") as f:
            tree = pickle.load(f)
        generate(args, rt, TreeIndex(tree, rt.encoder, rt.settings), args.tasks, variants)
    if not args.no_eval:
        score(args, [name for name, _ in variants])


if __name__ == "__main__":
    main()

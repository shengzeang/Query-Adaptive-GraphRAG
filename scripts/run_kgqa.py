"""KGQA evaluation (HotpotQA / 2WikiMQA / MuSiQue): RAPTOR and RAPTOR-QA (paper Table 4).

The BM25 / TF-IDF baselines are not run by default: add them with ``--methods bm25 tfidf raptor raptor-qa``.

Every question gets its own RAPTOR tree (built from its own paragraphs, cached under --cache-dir and
shared by all methods). Results are appended to ``<out>/<dataset>.jsonl`` and the script can be resumed.

    python scripts/run_kgqa.py --dataset musique --n 1000 \
        --methods raptor raptor-qa --routers generalist=checkpoints/generalist.pt --out outputs/kgqa

The first ``--n-specialist`` (default 200) questions of the seeded shuffle are held out of the test set
(``split_specialist_and_test``): they are not used by this pipeline, but keep the test questions identical to those of
earlier runs, so results stay comparable.
Per-query times are only meaningful with ``--workers 1``.

Parallel run on many CPU cores: start ``--shard 0/8`` ... ``--shard 7/8`` as separate processes, then one final
run without ``--shard`` (retries failures and writes the summary).
"""
import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tqdm import tqdm

from qa_graphrag.data import (KGQA_SOURCES, append_jsonl, done_ids, longest_first, parse_shard, refuse_other_prompt,
                              refuse_other_retrieval, refuse_other_top_k, split_specialist_and_test, take_shard,
                              warn_router_retrieval)
from qa_graphrag.index import corpus_text, load_or_build_tree
from qa_graphrag.llm import parallel_unordered
from qa_graphrag.metrics import aggregate, score_example
from qa_graphrag.pipeline import QueryRunner, check_method
from qa_graphrag.prompts import PROMPT_VERSION
from qa_graphrag.retrieval import RetrievalSettings, TreeIndex
from qa_graphrag.router import MLPRouter
from qa_graphrag.runtime import add_common_args, add_shard_arg, make_runtime


def summarize(path: Path) -> dict:
    rows = [json.loads(l) for l in open(path, encoding="utf-8")]
    methods = sorted({m for r in rows for m in r["outs"]})
    table = {}
    for m in methods:
        sel = [r["outs"][m] for r in rows if m in r["outs"]]
        agg = aggregate({"acc": o["acc"], "recall": o["recall"]} for o in sel)
        agg["time_per_query_s"] = sum(o["times"]["total"] for o in sel) / len(sel)
        levels = [o["level"] for o in sel if o.get("level") is not None]
        if levels and m.startswith("raptor-qa"):
            agg["level_distribution"] = {k: levels.count(k) for k in sorted(set(levels))}
        table[m] = agg
    return table


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dataset", required=True, choices=list(KGQA_SOURCES))
    ap.add_argument("--n", type=int, default=1000, help="number of test questions")
    ap.add_argument("--n-specialist", type=int, default=200)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--methods", nargs="+", default=["raptor", "raptor-qa"])
    ap.add_argument("--routers", nargs="*", default=[], help="name=checkpoint pairs used by raptor-qa")
    ap.add_argument("--max-new-tokens", type=int, default=256, help="room for the reasoning and the answer")
    ap.add_argument("--out", default="outputs/kgqa")
    add_common_args(ap)
    add_shard_arg(ap)
    args = ap.parse_args()

    for m in args.methods:
        check_method(m)
    routers = {}
    for item in args.routers:
        name, path = item.split("=", 1)
        routers[name] = MLPRouter.load(path)
    if "raptor-qa" in args.methods and not routers:
        ap.error("raptor-qa needs --routers name=checkpoint")

    _, test = split_specialist_and_test(args.dataset, n_specialist=args.n_specialist, n_test=args.n, seed=args.seed)
    out_path = Path(args.out) / f"{args.dataset}.jsonl"
    refuse_other_prompt(out_path, PROMPT_VERSION)
    refuse_other_top_k(out_path, args.top_k)
    uses_retrieval_mode = bool({"raptor", "raptor-qa"} & set(args.methods))      # bm25 / tfidf do not depend on it
    if uses_retrieval_mode:
        refuse_other_retrieval(out_path, RetrievalSettings().retrieval)
        warn_router_retrieval(routers, RetrievalSettings().retrieval, args.top_k)
    shard = parse_shard(args.shard)
    finished = done_ids(out_path)
    todo = longest_first([e for e in take_shard(test, shard) if str(e["id"]) not in finished])
    print(f"shard {shard[0]}/{shard[1]}: {len(test)} test questions, {len(finished)} done, {len(todo)} to go -> {out_path}")

    rt = make_runtime(args)

    def process(ex):
        tree = load_or_build_tree(rt.builder, corpus_text(ex["ctxs"]), args.cache_dir, args.dataset, f"{ex['id']}|{rt.tag}")
        runner = QueryRunner(TreeIndex(tree, rt.encoder, rt.settings), rt.generator, max_new_tokens=args.max_new_tokens)
        outs = {}
        for method in args.methods:
            variants = [(f"raptor-qa[{n}]", r) for n, r in routers.items()] if method == "raptor-qa" else [(method, None)]
            for name, router in variants:
                runner.router = router
                o = runner.run(method, ex["question"])
                sc = score_example(o.prediction, ex["answers"])
                outs[name] = {"prediction": o.prediction, "raw": o.raw, "level": o.level, "preference": o.preference,
                              "num_nodes": o.num_nodes, "times": o.times, **sc}
        row = {"id": str(ex["id"]), "question": ex["question"], "answers": ex["answers"], "prompt": PROMPT_VERSION,
               "top_k": args.top_k, "max_level": tree.num_layers, "outs": outs}
        if uses_retrieval_mode:
            row["retrieval"] = rt.settings.retrieval
        return row

    def safe(ex):
        try:
            return process(ex)
        except Exception as e:
            print(f"[skip {ex['id']}] {type(e).__name__}: {e}")
            return None

    for rec in tqdm(parallel_unordered(safe, todo, workers=args.workers), total=len(todo), mininterval=30):
        if rec is not None:
            append_jsonl(out_path, rec)

    if shard[1] > 1:   # the other shards may still be running: summarize in the final run without --shard
        return
    table = summarize(out_path)
    (Path(args.out) / f"{args.dataset}_summary.json").write_text(json.dumps(table, indent=1))
    print(json.dumps(table, indent=1))


if __name__ == "__main__":
    main()

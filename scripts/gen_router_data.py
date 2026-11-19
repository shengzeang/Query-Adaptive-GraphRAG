"""Build the router training data (paper Sec. 5.2.1).

For every sampled question: build its RAPTOR tree, then answer it starting retrieval from each level
0..K-1 and record the score of every level. Output is a resumable jsonl file with one record per
question::

    {"id", "source", "question", "answers", "max_level", "top_k", "prompt", "preds": [K], "acc": [K], "recall": [K]}

``top_k`` is the retrieval top-k the labels were made with (see ``--top-k``); the router must be used with the same.
``retrieval`` is how a start level retrieves (env ``RETRIEVAL``: ``collapse`` = top-k over the nodes of the layers 0..level,
``traverse`` = layer-by-layer descent from it; rows without the field are ``traverse``). A router must be used with the
retrieval its labels were made with, so labels of another mode are refused in one file: relabel into another ``--out``. The
cached trees do not depend on it, so relabelling reuses them (only the answers are generated again).
``prompt`` is the version of the generation prompt (``qa_graphrag.prompts.PROMPT_VERSION``); ``preds`` are the extracted
answers (the prompt asks for "REASONING: ... ANSWER: ..."). Labels of another version are not comparable: relabel.
``max_level`` is the number of summary layers the tree really has; levels above it repeat the
result of the top level (their retrieval is identical).

    python scripts/gen_router_data.py --source hotpotqa --n 2000 --out data/router/hotpotqa.jsonl
    python scripts/gen_router_data.py --source nq --n 2000 --out data/router/nq.jsonl
    python scripts/gen_router_data.py --source triviaqa --n 2000 --out data/router/triviaqa.jsonl

Tree building is CPU-bound; to use many cores run N processes on disjoint slices of the questions
(``--shard 0/8`` ... ``--shard 7/8``, same ``--out``), then one final run without ``--shard`` to retry failures.
"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tqdm import tqdm

from qa_graphrag import NUM_LEVELS
from qa_graphrag.data import (append_jsonl, done_ids, load_router_source, longest_first, parse_shard, read_jsonl,
                              refuse_other_prompt, refuse_other_retrieval)
from qa_graphrag.index import corpus_text, load_or_build_tree
from qa_graphrag.llm import parallel_unordered
from qa_graphrag.metrics import score_example
from qa_graphrag.pipeline import QueryRunner
from qa_graphrag.prompts import PROMPT_VERSION
from qa_graphrag.retrieval import RetrievalSettings, TreeIndex
from qa_graphrag.runtime import add_common_args, add_shard_arg, make_runtime


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", required=True, help="hotpotqa | nq | triviaqa")
    ap.add_argument("--n", type=int, default=2000, help="number of questions (paper: 2000 per source)")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--max-new-tokens", type=int, default=256, help="room for the reasoning and the answer")
    ap.add_argument("--out", required=True)
    add_common_args(ap)
    add_shard_arg(ap)
    args = ap.parse_args()

    shard = parse_shard(args.shard)
    examples = load_router_source(args.source, n=args.n, seed=args.seed, shard=shard)
    # Rows written before ``top_k`` was recorded were made with the then fixed value 5. Mixing values in one file would
    # make the labels inconsistent, so refuse to append to a file made with another top-k.
    previous = {r.get("top_k", 5) for r in read_jsonl(args.out)} if Path(args.out).exists() else set()
    if previous - {args.top_k}:
        sys.exit(f"{args.out} was made with --top-k {sorted(previous)}, not {args.top_k}: use another --out "
                 f"(or delete the file) to relabel with a different top-k")
    if Path(args.out).exists():
        refuse_other_prompt(args.out, PROMPT_VERSION)
        refuse_other_retrieval(args.out, RetrievalSettings().retrieval)
    finished = done_ids(args.out)
    todo = longest_first([e for e in examples if str(e["id"]) not in finished])
    print(f"retrieval of the labels: {RetrievalSettings().retrieval}")
    print(f"shard {shard[0]}/{shard[1]}: {len(examples)} questions, {len(finished)} already done in {args.out}, {len(todo)} to go")

    # NQ / TriviaQA corpora are whole Wikipedia pages / web pages (hundreds of chunks), so the summaries
    # of one layer are requested concurrently (thread-safe HTTP endpoint).
    rt = make_runtime(args, parallel_summaries=True)
    namespace = args.source

    def process(ex):
        tree = load_or_build_tree(rt.builder, corpus_text(ex["ctxs"]), args.cache_dir, namespace, f"{ex['id']}|{rt.tag}")
        runner = QueryRunner(TreeIndex(tree, rt.encoder, rt.settings), rt.generator, max_new_tokens=args.max_new_tokens)
        outs = runner.run_all_levels(ex["question"])
        scores = [score_example(o.prediction, ex["answers"]) for o in outs]
        pad = NUM_LEVELS - len(outs)
        outs, scores = outs + [outs[-1]] * pad, scores + [scores[-1]] * pad
        return {
            "id": str(ex["id"]),
            "source": args.source,
            "question": ex["question"],
            "answers": ex["answers"],
            "max_level": tree.num_layers,
            "top_k": args.top_k,
            "prompt": PROMPT_VERSION,
            "retrieval": rt.settings.retrieval,
            "preds": [o.prediction for o in outs],
            "acc": [s["acc"] for s in scores],
            "recall": [s["recall"] for s in scores],
        }

    def safe(ex):
        try:
            return process(ex)
        except Exception as e:  # keep going; failed questions are retried on the next run
            print(f"[skip {ex['id']}] {type(e).__name__}: {e}")
            return None

    for rec in tqdm(parallel_unordered(safe, todo, workers=args.workers), total=len(todo), mininterval=30):
        if rec is not None:
            append_jsonl(args.out, rec)


if __name__ == "__main__":
    main()

"""Build the shared RAPTOR knowledge base of GraphRAG-Bench (20 textbooks).

One tree is built per textbook (cached, resumable) and the trees are merged layer by layer into the
single tree that all five question types are answered from. Chunks are ``BENCH_CHUNK_TOKENS`` (200) tokens long unless
``--chunk-tokens`` says otherwise (the KGQA / router trees use 100). The cache key contains the chunk size and the cluster
cap, so trees made with other settings are neither reused nor overwritten; ``--out`` is overwritten, so give a tree of
another chunk size its own file name.

    python scripts/build_bench_index.py --out indexes/graphrag_bench_c200.pkl --workers 32
    # the size of the GraphRAG-Bench paper: needs replicas with --max-model-len 16384 (summaries of up to 9600 tokens)
    python scripts/build_bench_index.py --chunk-tokens 1200 --out indexes/graphrag_bench_c1200.pkl --workers 32

``--cluster-tokens`` (default: ``bench_cluster_tokens(chunk)``) caps the text of one cluster = the input of one summary;
chunks longer than the encoder reads (256 word pieces) are embedded window by window (``--truncate-long-texts`` turns
that off).

Summaries are the expensive part (tens of thousands of LLM calls): point SUMMARIZER_BASE_URL /
SUMMARIZER_MODEL / SUMMARIZER_API_KEY at a fast endpoint (a vLLM server or the DeepSeek API).

Building a textbook tree is CPU-bound, so the textbooks can be built by several processes
(``--shard 0/8`` ... ``--shard 7/8``, same ``--cache-dir``); a final run without ``--shard`` merges the cached trees.
"""
import argparse
import pickle
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from qa_graphrag import CLUSTER_TOKENS
from qa_graphrag.data import NUM_TEXTBOOKS, load_bench_textbook, parse_shard, take_shard
from qa_graphrag.index import load_or_build_tree
from qa_graphrag.runtime import add_common_args, add_shard_arg, make_runtime
from raptor.tree_builder import merge_trees

BENCH_CHUNK_TOKENS = 200   # GraphRAG-Bench textbooks: longer chunks than the 100 of the KGQA paragraphs
CLUSTER_CHUNKS = 8         # chunks per cluster for large chunks (see bench_cluster_tokens)


def bench_cluster_tokens(chunk_tokens: int) -> int:
    """Cap on the text of one cluster (= input of one summary). RAPTOR's 3500 is ~35 chunks of 100 tokens; the same
    number of 1200-token chunks (42000 tokens) does not fit any 7B model, so large chunks get CLUSTER_CHUNKS per cluster
    (1200 -> 9600, which the 16384-token window of the vLLM replicas holds, Qwen counting ~1.5x more tokens than cl100k
    included). Up to 437-token chunks the original 3500 stays."""
    return max(CLUSTER_TOKENS, CLUSTER_CHUNKS * chunk_tokens)


def build_bench_tree(rt, cache_dir: str, textbooks=None, merge: bool = True):
    trees = []
    for i in textbooks or range(1, NUM_TEXTBOOKS + 1):
        print(f"textbook {i}", flush=True)
        trees.append(load_or_build_tree(rt.builder, load_bench_textbook(i), cache_dir, "bench", f"textbook{i}|{rt.tag}"))
    return merge_trees(trees) if merge else None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default="indexes/graphrag_bench.pkl")
    ap.add_argument("--textbooks", type=int, nargs="*", help="subset of textbooks (default: all 20)")
    add_common_args(ap)
    add_shard_arg(ap)
    ap.set_defaults(chunk_tokens=BENCH_CHUNK_TOKENS, cluster_tokens=None)
    args = ap.parse_args()
    if args.cluster_tokens is None:
        args.cluster_tokens = bench_cluster_tokens(args.chunk_tokens)
    print(f"chunks of {args.chunk_tokens} tokens, clusters of at most {args.cluster_tokens} tokens"
          f"{', long chunks truncated by the encoder' if args.truncate_long_texts else ''}", flush=True)

    rt = make_runtime(args, parallel_summaries=args.workers > 1)
    shard = parse_shard(args.shard)
    if shard[1] > 1:   # build (and cache) only this shard's textbooks; the final run without --shard merges them
        books = take_shard(args.textbooks or list(range(1, NUM_TEXTBOOKS + 1)), shard)
        build_bench_tree(rt, args.cache_dir, books, merge=False)
        return
    tree = build_bench_tree(rt, args.cache_dir, args.textbooks)
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "wb") as f:
        pickle.dump(tree, f)
    print(f"merged tree: {len(tree.all_nodes)} nodes, summary layers {tree.num_layers}, "
          f"nodes per layer {[len(tree.layer_to_nodes[k]) for k in sorted(tree.layer_to_nodes)]}")


if __name__ == "__main__":
    main()

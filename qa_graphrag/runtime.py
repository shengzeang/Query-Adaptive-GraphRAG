"""Shared construction of the models / builder used by all scripts."""
import argparse
import logging
import os
from dataclasses import dataclass, field

from . import CLUSTER_TOKENS, NUM_TREE_LAYERS
from .embedding import DEFAULT_ENCODER, SBertEncoder
from .index import make_builder
from .llm import ChatLLM, LLMSummarizationModel
from .retrieval import RetrievalSettings


def add_common_args(p: argparse.ArgumentParser) -> None:
    p.add_argument("--encoder", default=DEFAULT_ENCODER, help="sentence encoder for nodes, queries and the router input")
    p.add_argument("--device", default=os.environ.get("ENCODER_DEVICE") or None,
                   help="device of the encoder (default: $ENCODER_DEVICE, else cuda if available)")
    p.add_argument("--tree-layers", type=int, default=NUM_TREE_LAYERS)
    p.add_argument("--top-k", type=int, default=RetrievalSettings.top_k,
                   help="nodes kept per layer by tree traversal and in total by BM25 / TF-IDF / the collapsed tree. "
                        "The router labels are made with one value of it: change it only together with regenerating them")
    p.add_argument("--chunk-tokens", type=int, default=100)
    p.add_argument("--summary-tokens", type=int, default=100)
    p.add_argument("--cluster-tokens", type=int, default=CLUSTER_TOKENS,
                   help="most text of one cluster = input of one summary (RAPTOR's 3500). Must grow with --chunk-tokens, "
                        "otherwise a cluster holds only a few chunks; the summariser's context window must fit it")
    p.add_argument("--truncate-long-texts", action="store_true",
                   help="embed only the first 256 word pieces of a longer text (the encoder's own behaviour) instead of "
                        "keeping an embedding per window and comparing the query with each (best window counts); only "
                        "chunks of more than ~200 tokens are affected")
    p.add_argument("--cache-dir", default="indexes", help="where RAPTOR trees are cached")
    p.add_argument("--workers", type=int, default=8, help="questions processed concurrently")
    p.add_argument("--verbose", action="store_true")


def add_shard_arg(p: argparse.ArgumentParser) -> None:
    p.add_argument("--shard", default=None, metavar="i/N",
                   help="process only the i-th of N disjoint slices of the questions (run N processes in parallel "
                        "to use more CPU cores; results go to the same file). A final run without --shard "
                        "retries failures and writes the summary")


@dataclass
class Runtime:
    encoder: SBertEncoder
    builder: object
    generator: ChatLLM
    summarizer_model: str
    tag: str   # identifies the tree-building settings in cache keys
    settings: RetrievalSettings = field(default_factory=RetrievalSettings)


def tree_tag(encoder: str, summarizer_model: str, tree_layers: int, chunk_tokens: int, summary_tokens: int,
             cluster_tokens: int = CLUSTER_TOKENS, truncate_long_texts: bool = False) -> str:
    """Identifies the tree-building settings in the cache keys of ``load_or_build_tree``. Settings at their default are
    left out, so the tags (and the cached trees) of runs made before they existed stay valid."""
    tag = f"{encoder}|{summarizer_model}|L{tree_layers}|c{chunk_tokens}|s{summary_tokens}"
    if cluster_tokens != CLUSTER_TOKENS:
        tag += f"|m{cluster_tokens}"
    if truncate_long_texts:
        tag += "|trunc"
    return tag


def make_runtime(args, parallel_summaries: bool = False) -> Runtime:
    # raptor/*.py call logging.basicConfig(level=ERROR) on import, which makes a later basicConfig a no-op
    logging.basicConfig(format="%(asctime)s - %(message)s")
    logging.getLogger().setLevel(logging.INFO if args.verbose else logging.WARNING)
    if args.verbose:   # keep per-request HTTP lines out of the progress log
        for noisy in ("httpx", "httpcore", "openai"):
            logging.getLogger(noisy).setLevel(logging.WARNING)
    encoder = SBertEncoder(args.encoder, device=args.device, segment_long_texts=not args.truncate_long_texts)
    summarizer = ChatLLM.from_role("summarizer")
    builder = make_builder(
        encoder,
        LLMSummarizationModel(summarizer),
        num_layers=args.tree_layers,
        chunk_tokens=args.chunk_tokens,
        summary_tokens=args.summary_tokens,
        parallel_summaries=parallel_summaries,
        cluster_tokens=args.cluster_tokens,
    )
    tag = tree_tag(args.encoder, summarizer.spec.model, args.tree_layers, args.chunk_tokens, args.summary_tokens,
                   args.cluster_tokens, args.truncate_long_texts)
    return Runtime(encoder, builder, ChatLLM.from_role("backbone"), summarizer.spec.model, tag,
                   RetrievalSettings(top_k=args.top_k))

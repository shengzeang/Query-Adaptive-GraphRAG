"""Building (and caching) RAPTOR trees."""
import hashlib
import os
import pickle
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np
import tiktoken

from raptor import BaseSummarizationModel, ClusterTreeBuilder, ClusterTreeConfig, Node, Tree

from . import CLUSTER_TOKENS, EMB_KEY, NUM_TREE_LAYERS, SEGMENTS_KEY
from .data import doc_text
from .embedding import SBertEncoder


class BatchedClusterTreeBuilder(ClusterTreeBuilder):
    """ClusterTreeBuilder that embeds all leaf chunks in a single batched call and keeps the per-window embeddings of
    the nodes whose text is longer than the encoder reads (under ``SEGMENTS_KEY``; the retriever uses them)."""

    def multithreaded_create_leaf_nodes(self, chunks: List[str]) -> Dict[int, Node]:
        encoder = self.embedding_models[EMB_KEY]
        if hasattr(encoder, "encode_many_with_segments"):
            vectors, segments = encoder.encode_many_with_segments(chunks)
            nodes = {}
            for i, (t, v, s) in enumerate(zip(chunks, vectors, segments)):
                emb = {EMB_KEY: v} if s is None else {EMB_KEY: v, SEGMENTS_KEY: s}
                nodes[i] = Node(t, i, set(), emb)
            return nodes
        if hasattr(encoder, "encode_many"):
            vectors = encoder.encode_many(chunks)
            return {i: Node(t, i, set(), {EMB_KEY: v}) for i, (t, v) in enumerate(zip(chunks, vectors))}
        return super().multithreaded_create_leaf_nodes(chunks)

    def create_node(self, index, text, children_indices=None):
        index, node = super().create_node(index, text, children_indices)
        encoder = self.embedding_models[EMB_KEY]
        if hasattr(encoder, "segment_embeddings"):          # a summary is short; only an over-long text gets windows
            segments = encoder.segment_embeddings(text)
            if segments is not None:
                node.embeddings[SEGMENTS_KEY] = segments
        return index, node


def make_builder(
    encoder: SBertEncoder,
    summarizer: BaseSummarizationModel,
    num_layers: int = NUM_TREE_LAYERS,
    chunk_tokens: int = 100,
    summary_tokens: int = 100,
    parallel_summaries: bool = False,
    cluster_tokens: int = CLUSTER_TOKENS,
) -> BatchedClusterTreeBuilder:
    """``cluster_tokens``: the most text one cluster may hold, i.e. the input of one summary. RAPTOR re-clusters (and
    finally splits) a larger cluster, so with chunks of c tokens a cluster has at most cluster_tokens / c chunks."""
    config = ClusterTreeConfig(
        tokenizer=tiktoken.get_encoding("cl100k_base"),
        max_tokens=chunk_tokens,
        num_layers=num_layers,
        summarization_length=summary_tokens,
        summarization_model=summarizer,
        embedding_models={EMB_KEY: encoder},
        cluster_embedding_model=EMB_KEY,
        clustering_params={"max_length_in_cluster": cluster_tokens},
    )
    builder = BatchedClusterTreeBuilder(config)
    builder.parallel_summaries = parallel_summaries
    return builder


def corpus_text(ctxs: List[Dict]) -> str:
    return " ".join(doc_text(c) for c in ctxs)


def build_tree(builder: BatchedClusterTreeBuilder, text: str) -> Tree:
    # use_multithreading=True routes leaf creation through the batched override above
    return builder.build_from_text(text, use_multithreading=True)


def cache_path(cache_dir: str, namespace: str, key: str) -> Path:
    safe = hashlib.md5(key.encode()).hexdigest()[:16]
    return Path(cache_dir) / namespace / f"{safe}.pkl"


def load_or_build_tree(builder, text: str, cache_dir: Optional[str], namespace: str, key: str) -> Tree:
    """Trees are deterministic functions of (corpus, builder settings), so they are cached on disk and
    shared by all variants (RAPTOR / RAPTOR-QA / fixed levels) of an experiment."""
    if cache_dir:
        path = cache_path(cache_dir, namespace, key)
        if path.exists():
            with open(path, "rb") as f:
                return pickle.load(f)
    tree = build_tree(builder, text)
    if cache_dir:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".tmp")
        with open(tmp, "wb") as f:
            pickle.dump(tree, f)
        os.replace(tmp, path)
    return tree


def leaf_texts(tree: Tree) -> List[str]:
    return [n.text for n in tree.layer_to_nodes[0]]


def duplicate_embedding_stats(tree: Tree) -> Dict:
    """Groups of nodes with bit-identical embeddings, per layer.

    Before the fix in ``raptor/cluster_utils.py`` cluster members were looked up by embedding value, so ``k`` nodes
    sharing one embedding were each added ``k`` times to every cluster they belong to (``k*k`` entries instead of
    ``k``) and the summary prompt contained the same text repeatedly. Only layers that were clustered matter (every
    layer except the top one); a tree without such groups there is not affected.
    """
    layers = []
    for layer, nodes in sorted(tree.layer_to_nodes.items()):
        groups: Dict[bytes, List[int]] = {}
        for n in nodes:
            emb = n.embeddings.get(EMB_KEY, next(iter(n.embeddings.values())))
            groups.setdefault(np.asarray(emb).tobytes(), []).append(n.index)
        sizes = sorted((len(g) for g in groups.values() if len(g) > 1), reverse=True)
        layers.append({"layer": layer, "nodes": len(nodes), "dup_groups": len(sizes), "dup_nodes": sum(sizes),
                       "max_group": sizes[0] if sizes else 1})
    clustered = layers[:-1]
    return {"layers": layers, "affected": any(l["dup_groups"] for l in clustered),
            "max_group": max([l["max_group"] for l in clustered], default=1)}

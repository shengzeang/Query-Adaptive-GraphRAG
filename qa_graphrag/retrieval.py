"""Retrieval over a RAPTOR tree: tree traversal from level k (RAPTOR = top level, RAPTOR-QA = router-chosen level),
the collapsed tree, and flat baselines. All of them keep ``RetrievalSettings.top_k`` nodes (per layer when descending)."""
import os
import re
from dataclasses import dataclass, field
from typing import Callable, List, Optional

import numpy as np

from raptor import Tree, TreeRetriever, TreeRetrieverConfig
from raptor.utils import get_node_list

from . import EMB_KEY

RETRIEVAL_MODES = ("collapse", "traverse")
# How ``raptor`` and ``raptor-qa`` retrieve, chosen for the whole process: by default the layer-by-layer descent of the tree
# (``traverse``); ``RETRIEVAL=collapse`` ranks the nodes of all layers 0..start level together instead.
DEFAULT_RETRIEVAL = os.environ.get("RETRIEVAL", "traverse").strip() or "traverse"


@dataclass
class RetrievalSettings:
    top_k: int = 10                 # one k for every method: nodes kept per layer by tree traversal, nodes kept in total
                                    # by the collapsed tree and by BM25 / TF-IDF (so level 0 and BM25 see equally many chunks)
    max_tokens: int = 3500          # token budget of the retrieved context
    retrieval: str = DEFAULT_RETRIEVAL   # "traverse": descent from the start level; "collapse": top-k over the nodes of layers 0..start level

    def __post_init__(self):
        if self.retrieval not in RETRIEVAL_MODES:
            raise ValueError(f"RETRIEVAL must be one of {RETRIEVAL_MODES}, got {self.retrieval!r}")


@dataclass
class Retrieved:
    context: str
    level: Optional[int]            # effective start level (None for level-free methods)
    num_nodes: int


class TreeIndex:
    """A RAPTOR tree together with the retriever objects needed to query it."""

    def __init__(self, tree: Tree, encoder, settings: RetrievalSettings = None):
        self.tree = tree
        self.encoder = encoder
        self.settings = settings or RetrievalSettings()
        config = TreeRetrieverConfig(
            embedding_model=encoder,
            context_embedding_model=EMB_KEY,
            top_k=self.settings.top_k,
            selection_mode="top_k",
        )
        self.retriever = TreeRetriever(config, tree)
        self._pools = {}                # start level -> the nodes of layers 0..level (collapse mode), built once

    @property
    def max_level(self) -> int:
        return self.tree.num_layers

    def clamp(self, level: int) -> int:
        return max(0, min(int(level), self.max_level))

    def retrieve_from_level(self, query: str, level: int) -> Retrieved:
        """RAPTOR-QA retrieval: start at ``level`` and descend to the leaves (levels level..0)."""
        level = self.clamp(level)
        nodes, context = self._traverse(query, level)
        return Retrieved(context, level, len(nodes))

    def _traverse(self, query: str, level: int):
        layer_nodes = self.tree.layer_to_nodes[level]
        return self.retriever.retrieve_information(layer_nodes, query, level + 1, self.settings.max_tokens)

    def retrieve_tree(self, query: str) -> Retrieved:
        """RAPTOR's tree traversal: start at the top layer and descend to the leaves (= ``retrieve_from_level`` of
        the highest level, i.e. the "always the highest level" policy RAPTOR-QA is compared against)."""
        return self.retrieve_from_level(query, self.max_level)

    def retrieve_collapsed(self, query: str, level: Optional[int] = None) -> Retrieved:
        """RAPTOR's collapsed tree: top-k over all nodes of the tree, whatever their layer. With ``level`` only the nodes of
        layers 0..level compete (the layers a descent from ``level`` can reach); the top level is the whole tree and level 0
        the leaves, i.e. the same chunks as ``retrieve_from_level(query, 0)``."""
        nodes, context = self._collapse(query, level)
        return Retrieved(context, None if level is None else self.clamp(level), len(nodes))

    def _collapse(self, query: str, level: Optional[int]):
        pool = None
        if level is not None and self.clamp(level) < self.max_level:
            pool = self._pools.get(self.clamp(level))
            if pool is None:
                below = {n.index: n for k in range(self.clamp(level) + 1) for n in self.tree.layer_to_nodes[k]}
                pool = self._pools[self.clamp(level)] = get_node_list(below)
        return self.retriever.retrieve_information_collapse_tree(
            query, self.settings.top_k, self.settings.max_tokens, node_list=pool
        )

    def _start(self, query: str, level: int):
        """``(nodes, context)`` of RAPTOR / RAPTOR-QA with start level ``level``, in the mode of ``settings.retrieval``."""
        level = self.clamp(level)
        return self._collapse(query, level) if self.settings.retrieval == "collapse" else self._traverse(query, level)

    def retrieve_start(self, query: str, level: int) -> Retrieved:
        """What ``raptor`` (start = top level) and ``raptor-qa`` (start = the router's level) retrieve."""
        nodes, context = self._start(query, level)
        return Retrieved(context, self.clamp(level), len(nodes))

    def leaf_chunks(self) -> List[str]:
        return [n.text for n in self.tree.layer_to_nodes[0]]


# ------------------------------------------------------------------------ flat baselines
_TOKEN = re.compile(r"\w+")


def _tokenize(text: str) -> List[str]:
    return _TOKEN.findall(text.lower())


class FlatRetriever:
    """BM25 / TF-IDF over the leaf chunks (the same chunks RAPTOR starts from)."""

    def __init__(self, chunks: List[str], method: str, top_k: int = 10, max_tokens: int = 3500, count_tokens: Callable = None):
        self.chunks, self.method, self.top_k = chunks, method, top_k
        self.max_tokens = max_tokens
        self.count_tokens = count_tokens
        if method == "bm25":
            from rank_bm25 import BM25Okapi

            self.index = BM25Okapi([_tokenize(c) or ["_"] for c in chunks])
        elif method == "tfidf":
            from sklearn.feature_extraction.text import TfidfVectorizer

            self.vectorizer = TfidfVectorizer(tokenizer=_tokenize, lowercase=False, token_pattern=None)
            self.matrix = self.vectorizer.fit_transform(chunks)
        else:
            raise ValueError(method)

    def retrieve(self, query: str) -> Retrieved:
        if self.method == "bm25":
            scores = np.asarray(self.index.get_scores(_tokenize(query)))
        else:
            scores = (self.matrix @ self.vectorizer.transform([query]).T).toarray().ravel()
        order = np.argsort(-scores, kind="stable")[: self.top_k]
        picked, used = [], 0
        for i in order:
            n_tok = self.count_tokens(self.chunks[i]) if self.count_tokens else 0
            if picked and used + n_tok > self.max_tokens:
                break
            picked.append(self.chunks[i])
            used += n_tok
        return Retrieved("\n\n".join(picked), None, len(picked))

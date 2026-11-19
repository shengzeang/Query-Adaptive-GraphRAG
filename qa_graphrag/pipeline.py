"""QA-GraphRAG inference: encode -> route -> retrieve from the predicted level -> generate."""
import re
import time
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Sequence

import numpy as np

from .llm import ChatLLM
from .metrics import score_example
from .prompts import KGQA_PROMPT, extract_final_answer
from .retrieval import FlatRetriever, Retrieved, TreeIndex
from .router import MLPRouter

LEVEL_METHOD = re.compile(r"^level(\d+)$")
START_METHOD = re.compile(r"^start(\d+)$")
KNOWN_METHODS = ("bm25", "tfidf", "raptor", "raptor-collapsed", "raptor-qa")


def check_method(name: str) -> None:
    if name not in KNOWN_METHODS and not LEVEL_METHOD.match(name) and not START_METHOD.match(name):
        raise ValueError(f"unknown method '{name}'; use one of {KNOWN_METHODS}, level<k> or start<k>")


@dataclass
class Output:
    method: str
    prediction: str
    level: Optional[int] = None
    preference: Optional[List[float]] = None
    num_nodes: int = 0
    times: Dict[str, float] = field(default_factory=dict)
    context: str = ""
    raw: str = ""                   # the full model response (``prediction`` is the extracted answer for the KGQA prompt)


class QueryRunner:
    """Answers one query with any of the compared retrieval strategies over a single corpus.

    * ``bm25`` / ``tfidf``  flat top-k over the leaf chunks
    * ``raptor``            RAPTOR from the top layer. ``RetrievalSettings.retrieval`` (env ``RETRIEVAL``) decides how: "collapse"
                            (default) = top-k over all nodes; "traverse" = layer-by-layer descent (= ``level<max_level>``)
    * ``raptor-collapsed``  RAPTOR's collapsed tree (top-k over all nodes) whatever the mode; not in the default method lists
    * ``level<k>``          fixed start level k, always by descent (diagnostics)
    * ``start<k>``          fixed start level k retrieved as ``raptor-qa`` does it, in the mode of ``settings.retrieval``: what a
                            router label is (``run_all_levels``); the same as ``level<k>`` in "traverse" mode
    * ``raptor-qa``         RAPTOR-QA: the router picks the start level from the query embedding; retrieval as ``raptor``
                            from that level (collapse: top-k over the nodes of layers 0..level)
    """

    def __init__(self, index: TreeIndex, generator: ChatLLM, router: Optional[MLPRouter] = None, max_new_tokens: int = 256):
        self.index, self.generator, self.router = index, generator, router
        self.max_new_tokens = max_new_tokens
        self._flat: Dict[str, FlatRetriever] = {}

    def _flat_retriever(self, method: str) -> FlatRetriever:
        if method not in self._flat:
            s = self.index.settings
            tok = self.index.retriever.tokenizer
            self._flat[method] = FlatRetriever(
                self.index.leaf_chunks(), method, s.top_k, s.max_tokens, lambda t: len(tok.encode(t))
            )
        return self._flat[method]

    def retrieve(self, method: str, query: str):
        """Returns ``(Retrieved, preference or None, route_seconds)``."""
        check_method(method)
        if method in ("bm25", "tfidf"):
            return self._flat_retriever(method).retrieve(query), None, 0.0
        if method == "raptor":
            return self.index.retrieve_start(query, self.index.max_level), None, 0.0
        if method == "raptor-collapsed":
            return self.index.retrieve_collapsed(query), None, 0.0
        m = LEVEL_METHOD.match(method)
        if m:
            return self.index.retrieve_from_level(query, int(m.group(1))), None, 0.0
        m = START_METHOD.match(method)
        if m:
            return self.index.retrieve_start(query, int(m.group(1))), None, 0.0
        if self.router is None:
            raise ValueError("raptor-qa needs a router")
        t0 = time.perf_counter()
        level, pref = self.router.route(self.index.encoder.create_embedding(query))
        return self.index.retrieve_start(query, level), pref.tolist(), time.perf_counter() - t0

    def run(self, method: str, query: str, prompt_fn=None, max_new_tokens: Optional[int] = None) -> Output:
        t0 = time.perf_counter()
        retrieved, pref, t_route = self.retrieve(method, query)
        t1 = time.perf_counter()
        prompt = (prompt_fn or (lambda ctx, q: KGQA_PROMPT.format(context=ctx, question=q)))(retrieved.context, query)
        raw = self.generator.chat(prompt, max_tokens=max_new_tokens or self.max_new_tokens)
        t2 = time.perf_counter()
        # the default KGQA prompt asks for "REASONING: ... ANSWER: ...": only the answer is scored; a custom prompt
        # (GraphRAG-Bench) keeps the whole response, which its own evaluator parses
        prediction = raw if prompt_fn else extract_final_answer(raw)
        return Output(
            method, prediction, retrieved.level, pref, retrieved.num_nodes,
            {"route": t_route, "retrieve": t1 - t0 - t_route, "generate": t2 - t1, "total": t2 - t0},
            retrieved.context, raw,
        )

    def run_all_levels(self, query: str) -> List[Output]:
        """Answer from every start level 0..max_level (router training labels), retrieving the way ``raptor-qa`` will:
        the label of a level must come from the retrieval the router then chooses it for."""
        return [self.run(f"start{k}", query) for k in range(self.index.max_level + 1)]


def score_outputs(outputs: Sequence[Output], golds: Sequence[str]) -> List[Dict[str, float]]:
    return [score_example(o.prediction, golds) for o in outputs]

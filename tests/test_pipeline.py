"""Offline tests: no GPU, no network model downloads, no LLM endpoint (everything is stubbed)."""
import hashlib
import re
import sys
from pathlib import Path

import numpy as np
import pytest
import torch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from raptor import BaseEmbeddingModel, BaseSummarizationModel
from qa_graphrag import EMB_KEY
from qa_graphrag import bench_eval, metrics
from qa_graphrag.index import build_tree, corpus_text, duplicate_embedding_stats, make_builder
from qa_graphrag.pipeline import QueryRunner
from qa_graphrag.retrieval import FlatRetriever, RetrievalSettings, TreeIndex
from qa_graphrag.router import MLPRouter, RouterConfig, cross_validate, router_loss, train_router


class HashEncoder(BaseEmbeddingModel):
    """Deterministic bag-of-words hashing embedding (stands in for the sentence encoder)."""

    dim = 64

    def create_embedding(self, text):
        v = np.zeros(self.dim, dtype=np.float32)
        for w in text.lower().split():
            v[int(hashlib.md5(w.encode()).hexdigest(), 16) % self.dim] += 1.0
        return v / (np.linalg.norm(v) + 1e-8)

    def encode_many(self, texts, batch_size=128):
        return np.stack([self.create_embedding(t) for t in texts])


class FirstWordsSummarizer(BaseSummarizationModel):
    def summarize(self, context, max_tokens=150):
        return "SUMMARY " + " ".join(context.split()[:30])


class EchoLLM:
    """Returns the first sentence of the context that contains 'capital' (a fake reader)."""

    def chat(self, prompt, max_tokens=64, **kw):
        return "answer"


def make_corpus(n_docs=60):
    return [{"title": f"Doc {i}", "text": f"Entity{i} is a place. The capital of Country{i} is City{i}. " * 3} for i in range(n_docs)]


@pytest.fixture(scope="module")
def tree_and_encoder():
    enc = HashEncoder()
    builder = make_builder(enc, FirstWordsSummarizer(), num_layers=2)
    tree = build_tree(builder, corpus_text(make_corpus()))
    return tree, enc


# ---------------------------------------------------------------- router
def test_router_inference_is_deterministic():
    router = MLPRouter(RouterConfig(in_dim=16, num_levels=3, dropout=0.5))
    x = torch.randn(32, 16)
    router.train()  # predict() must still be deterministic and restore the mode
    a, pa = router.predict(x)
    b, pb = router.predict(x)
    assert (a == b).all() and np.allclose(pa, pb)
    assert router.training
    assert np.allclose(pa.sum(-1), 1.0, atol=1e-5)


def test_router_loss_matches_paper_formula():
    q = torch.tensor([[0.2, 0.5, 0.3]])
    p = torch.tensor([[1.0, 0.0, 1.0]])
    assert router_loss(q, p).item() == pytest.approx(1 - 0.5)


def test_router_learns_to_pick_the_best_level():
    rng = np.random.RandomState(0)
    X = rng.randn(600, 8).astype(np.float32)
    best = (X[:, 0] > 0).astype(int) * 2          # level 2 if x0>0 else level 0
    P = np.zeros((600, 3), dtype=np.float32)
    P[np.arange(600), best] = 1.0
    router, report = train_router(X, P, hidden=32, epochs=60, lr=1e-2, dropout=0.0, log=lambda *_: None)
    levels, _ = router.predict(X)
    assert (levels == best).mean() > 0.9
    assert report["heldout_router_score"] > report["heldout_reference"]["always_level_0"]


def test_cross_validate_scores_unseen_folds_with_a_separate_eval_label():
    rng = np.random.RandomState(0)
    X = rng.randn(300, 8).astype(np.float32)
    best = (X[:, 0] > 0).astype(int) * 2
    P = np.zeros((300, 3), dtype=np.float32)
    P[np.arange(300), best] = 1.0
    scores = cross_validate(X, P, n_folds=3, seed=1, hidden=16, epochs=40, dropout=0.0)
    assert len(scores) == 3 and np.mean(scores) > P[:, 0].mean() + 0.2
    assert scores == cross_validate(X, P, n_folds=3, seed=1, hidden=16, epochs=40, dropout=0.0)   # deterministic
    # trained on a useless label (all zeros), scored on the informative one: no better than chance level
    useless = cross_validate(X, np.zeros_like(P), P, n_folds=3, seed=1, hidden=16, epochs=10)
    assert np.mean(useless) < np.mean(scores) - 0.2


def _informative_and_tied(n_inf=300, n_tie=1200, seed=0):
    rng = np.random.RandomState(seed)
    X = rng.randn(n_inf + n_tie, 8).astype(np.float32)
    P = np.zeros((len(X), 3), dtype=np.float32)
    best = (X[:n_inf, 0] > 0).astype(int) * 2
    P[np.arange(n_inf), best] = 1.0                    # informative: exactly one level is right
    P[n_inf:] = rng.randint(0, 2, (n_tie, 1))          # ties: all levels right or all wrong
    return X, P


def test_skip_ties_drops_only_uninformative_training_questions():
    X, P = _informative_and_tied()
    _, rep = train_router(X, P, hidden=16, epochs=2, skip_ties=True, val_fraction=0.1, log=lambda *_: None)
    assert rep["n_ties_dropped"] > 900 and rep["n_train"] + rep["n_ties_dropped"] == 1350
    assert rep["n_heldout"] == 150                      # the held-out split keeps its ties
    _, rep = train_router(X, P, hidden=16, epochs=2, log=lambda *_: None)
    assert rep["n_ties_dropped"] == 0 and rep["n_train"] == 1350
    with pytest.raises(ValueError):
        train_router(X, np.ones_like(P), epochs=1, skip_ties=True, log=lambda *_: None)


def test_mse_loss_is_shift_invariant_and_learns_the_best_level():
    from qa_graphrag.router import centered_mse_loss

    logits, P = torch.randn(5, 3), torch.rand(5, 3)
    assert centered_mse_loss(logits, P).item() == pytest.approx(centered_mse_loss(logits + 7.0, P - 0.3).item(), abs=1e-5)
    X, P = _informative_and_tied()
    router, _ = train_router(X, P, hidden=32, epochs=60, dropout=0.0, loss="mse", skip_ties=True, log=lambda *_: None)
    levels, _ = router.predict(X[:300])
    assert (levels == (X[:300, 0] > 0).astype(int) * 2).mean() > 0.9
    with pytest.raises(ValueError):
        train_router(X, P, loss="nope")


def test_cross_validate_returns_the_choice_for_every_question():
    X, P = _informative_and_tied(150, 150)
    scores, choices = cross_validate(X, P, n_folds=3, hidden=8, epochs=3, return_choices=True)
    assert len(scores) == 3 and choices.shape == (300,) and set(choices) <= {0, 1, 2}


def test_cross_validate_train_fraction_is_nested_and_one_is_identity(monkeypatch):
    from qa_graphrag import router as router_mod

    X, P = _informative_and_tied(150, 150)
    seen = []
    real = router_mod.train_router

    def spy(Xt, Pt, **kw):
        seen.append(Xt.copy())
        return real(Xt, Pt, **kw)

    monkeypatch.setattr(router_mod, "train_router", spy)
    kw = dict(n_folds=3, seed=2, hidden=8, epochs=2)
    base = cross_validate(X, P, **kw)
    assert cross_validate(X, P, train_fraction=1.0, **kw) == base
    seen.clear()
    cross_validate(X, P, train_fraction=0.25, **kw)
    assert [len(x) for x in seen] == [50, 50, 50]        # 25% of the 200 training questions of every fold
    quarter = [set(map(tuple, x)) for x in seen]
    seen.clear()
    cross_validate(X, P, train_fraction=0.5, **kw)
    assert [len(x) for x in seen] == [100, 100, 100]
    assert all(q <= set(map(tuple, x)) for q, x in zip(quarter, seen))   # nested
    with pytest.raises(ValueError):
        cross_validate(X, P, train_fraction=0.0, **kw)


def test_router_checkpoint_roundtrip(tmp_path):
    r = MLPRouter(RouterConfig(8, 3))
    r.save(str(tmp_path / "r.pt"), {"encoder": "x"})
    r2 = MLPRouter.load(str(tmp_path / "r.pt"))
    x = torch.randn(4, 8)
    assert np.allclose(r.predict(x)[1], r2.predict(x)[1], atol=1e-6) and r2.meta["encoder"] == "x"


# ---------------------------------------------------------------- tree & retrieval
def test_tree_has_summary_layers(tree_and_encoder):
    tree, _ = tree_and_encoder
    assert tree.num_layers >= 1
    assert len(tree.layer_to_nodes[0]) > len(tree.layer_to_nodes[1])


def test_builder_is_reusable_after_small_corpus():
    enc = HashEncoder()
    builder = make_builder(enc, FirstWordsSummarizer(), num_layers=2)
    small = build_tree(builder, "Tiny corpus. " * 5)
    assert small.num_layers == 0 and builder.num_layers == 2   # configured value is restored


def test_level_retrieval_contains_requested_levels(tree_and_encoder):
    tree, enc = tree_and_encoder
    index = TreeIndex(tree, enc, RetrievalSettings(top_k=3, max_tokens=3500))
    q = "What is the capital of Country7?"
    ctx0 = index.retrieve_from_level(q, 0)
    assert ctx0.level == 0 and ctx0.num_nodes == 3 and "SUMMARY" not in ctx0.context
    top = index.max_level
    ctx_top = index.retrieve_from_level(q, top)
    assert ctx_top.level == top and "SUMMARY" in ctx_top.context
    assert ctx_top.num_nodes > ctx0.num_nodes                  # level k descends through levels k..0
    assert index.retrieve_from_level(q, 99).level == top        # clamped


def test_one_top_k_for_every_method_and_raptor_is_the_top_level_traversal(tree_and_encoder):
    tree, enc = tree_and_encoder
    index = TreeIndex(tree, enc, RetrievalSettings(top_k=4, max_tokens=3500, retrieval="traverse"))
    runner = QueryRunner(index, EchoLLM())
    q = "What is the capital of Country7?"
    assert runner.retrieve("level0", q)[0].num_nodes == 4                          # k leaves ...
    assert runner.retrieve("bm25", q)[0].num_nodes == runner.retrieve("tfidf", q)[0].num_nodes == 4   # ... as many as BM25
    assert runner.retrieve("raptor-collapsed", q)[0].num_nodes == 4
    top = runner.retrieve(f"level{index.max_level}", q)[0]
    raptor = runner.retrieve("raptor", q)[0]
    assert (raptor.context, raptor.level, raptor.num_nodes) == (top.context, index.max_level, top.num_nodes)
    assert RetrievalSettings().top_k == 10                                          # the default top-k


def test_collapse_retrieval_of_raptor_and_raptor_qa(tree_and_encoder):
    import os
    tree, enc = tree_and_encoder
    q = "What is the capital of Country7?"
    layer_of = {n.index: k for k, nodes in tree.layer_to_nodes.items() for n in nodes}
    if "RETRIEVAL" not in os.environ:
        assert RetrievalSettings().retrieval == "traverse"                          # the default; collapse is chosen below
    index = TreeIndex(tree, enc, RetrievalSettings(top_k=4, max_tokens=3500, retrieval="collapse"))
    runner = QueryRunner(index, EchoLLM(), MLPRouter(RouterConfig(enc.dim, index.max_level + 1)))
    whole = index.retrieve_collapsed(q)
    raptor = runner.retrieve("raptor", q)[0]
    assert (raptor.context, raptor.num_nodes, raptor.level) == (whole.context, 4, index.max_level)   # top-k over every node
    # a start level restricts the pool to layers 0..level; level 0 = the leaves, the same chunks as the descent from level 0
    leaves = index.retrieve_start(q, 0)
    assert leaves.context == index.retrieve_from_level(q, 0).context and "SUMMARY" not in leaves.context
    for level in range(index.max_level + 1):
        nodes, _ = index._start(q, level)
        assert len(nodes) == 4 and max(layer_of[n.index] for n in nodes) <= level
    assert runner.retrieve("raptor-qa", q)[0].num_nodes == 4
    # level<k> (router labels, diagnostics) always descends, whatever the mode
    traverse = TreeIndex(tree, enc, RetrievalSettings(top_k=4, max_tokens=3500, retrieval="traverse"))
    assert QueryRunner(index, EchoLLM()).retrieve(f"level{index.max_level}", q)[0].context == \
        traverse.retrieve_from_level(q, index.max_level).context
    assert QueryRunner(traverse, EchoLLM()).retrieve("raptor", q)[0].context == \
        traverse.retrieve_from_level(q, index.max_level).context
    with pytest.raises(ValueError):
        RetrievalSettings(retrieval="bfs")


def test_router_labels_are_made_with_the_retrieval_the_router_is_used_with(tree_and_encoder):
    tree, enc = tree_and_encoder
    q = "What is the capital of Country7?"
    for mode in ("collapse", "traverse"):
        index = TreeIndex(tree, enc, RetrievalSettings(top_k=4, max_tokens=3500, retrieval=mode))
        outs = QueryRunner(index, EchoLLM()).run_all_levels(q)
        assert len(outs) == index.max_level + 1
        for k, o in enumerate(outs):
            assert o.context == index.retrieve_start(q, k).context and o.level == k      # what raptor-qa retrieves from level k
        assert outs[0].context == index.retrieve_from_level(q, 0).context                # the leaves, in both modes
    # collapse: level k ranks the layers 0..k together; traverse: it descends through them, k nodes per layer
    collapse = TreeIndex(tree, enc, RetrievalSettings(top_k=4, max_tokens=3500, retrieval="collapse"))
    assert [o.num_nodes for o in QueryRunner(collapse, EchoLLM()).run_all_levels(q)] == [4] * (collapse.max_level + 1)
    assert QueryRunner(collapse, EchoLLM()).run("start1", q).level == 1


def test_router_remembers_the_retrieval_of_its_labels(tmp_path, capsys):
    from qa_graphrag.data import warn_router_retrieval
    r = MLPRouter(RouterConfig(8, 3))
    assert r.retrieval == "traverse"                                                  # no meta: made before it was recorded
    r.save(str(tmp_path / "c.pt"), {"retrieval": "collapse"})
    c = MLPRouter.load(str(tmp_path / "c.pt"))
    assert c.retrieval == "collapse"
    warn_router_retrieval({"g": c}, "collapse")
    assert capsys.readouterr().out == ""
    warn_router_retrieval({"g": c}, "traverse")
    assert "WARNING" in capsys.readouterr().out


def test_other_top_k_is_refused_and_warned_about(tmp_path, capsys):
    from qa_graphrag.data import append_jsonl, refuse_other_top_k, warn_router_retrieval
    path = tmp_path / "r.jsonl"
    refuse_other_top_k(path, 10)                                                       # no file: fine
    append_jsonl(path, {"id": "1", "top_k": 10})
    refuse_other_top_k(path, 10)
    with pytest.raises(SystemExit):
        refuse_other_top_k(path, 5)
    old = tmp_path / "old.jsonl"
    append_jsonl(old, {"id": "1"})                                                     # rows without the field are top-k 5
    refuse_other_top_k(old, 5)
    with pytest.raises(SystemExit):
        refuse_other_top_k(old, 10)
    r = MLPRouter(RouterConfig(8, 3))
    assert r.top_k == 5                                                                # no meta: made before it was recorded
    r.save(str(tmp_path / "k.pt"), {"top_k": 10, "retrieval": "traverse"})
    k = MLPRouter.load(str(tmp_path / "k.pt"))
    assert k.top_k == 10
    warn_router_retrieval({"g": k}, "traverse", 10)
    assert capsys.readouterr().out == ""
    warn_router_retrieval({"g": k}, "traverse", 5)
    assert "top-k 10" in capsys.readouterr().out


def test_mixed_retrieval_modes_are_refused(tmp_path):
    from qa_graphrag.data import append_jsonl, refuse_other_retrieval
    path = tmp_path / "r.jsonl"
    refuse_other_retrieval(path, "collapse")                                           # no file: fine
    append_jsonl(path, {"id": "1", "retrieval": "collapse"})
    refuse_other_retrieval(path, "collapse")
    with pytest.raises(SystemExit):
        refuse_other_retrieval(path, "traverse")
    old = tmp_path / "old.jsonl"
    append_jsonl(old, {"id": "1"})                                                     # rows without the field are traverse
    refuse_other_retrieval(old, "traverse")
    with pytest.raises(SystemExit):
        refuse_other_retrieval(old, "collapse")


def _load_script(name):
    import importlib.util

    spec = importlib.util.spec_from_file_location(name, Path(__file__).resolve().parent.parent / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_long_texts_are_embedded_window_by_window():
    from qa_graphrag.embedding import SBertEncoder, split_windows

    text = " ".join(f"w{i}" for i in range(1000))
    assert split_windows(text, 200, 254) == [text]                                     # fits: untouched
    parts = split_windows(text, 1000, 254)
    assert " ".join(parts).split() == text.split() and len(parts) == 5                 # every word kept, in order, no overlap
    assert all(len(p.split()) <= 254 for p in parts)

    class FakeModel:                                                                   # one word piece per word; the embedding is [n_words, 1]
        max_seq_length = 256

        def tokenizer(self, texts, **kw):
            return {"input_ids": [t.split() for t in texts]}

        def encode(self, texts, batch_size=1, show_progress_bar=False):
            return np.array([[len(t.split()), float(t.split()[0] == "w0")] for t in texts], dtype=np.float32)

    enc = object.__new__(SBertEncoder)
    enc.model, enc.segment_long_texts, enc._lock, enc._cache, enc._cache_size = FakeModel(), True, __import__("threading").Lock(), {}, 10
    enc.dim = 2
    short, long_ = "w0 a b", text
    vectors, segments = enc.encode_many_with_segments([short, long_])
    assert segments[0] is None and np.allclose(vectors[0], [3, 1])                      # a text that fits: exactly the model's embedding
    assert segments[1].shape == (5, 2) and np.allclose(segments[1][:, 0], [200] * 5)    # a long one: one embedding per window, none averaged away
    assert np.isclose(np.linalg.norm(vectors[1]), 1.0)                                  # its single vector (for clustering) is the normalised mean
    assert enc.segment_embeddings(short) is None and enc.segment_embeddings(long_).shape == (5, 2)
    enc.segment_long_texts = False
    assert enc.segment_embeddings(long_) is None
    assert np.allclose(enc.encode_many([long_])[0], [1000, 1])                          # truncation mode: the model sees the whole text (its own limit applies)
    assert enc.max_pieces == 254


def test_retrieval_compares_the_query_with_every_window_and_takes_the_best():
    from raptor.utils import SEGMENTS_SUFFIX, distances_from_embeddings, distances_to_nearest_segment
    from qa_graphrag import SEGMENTS_KEY
    assert SEGMENTS_KEY == EMB_KEY + SEGMENTS_SUFFIX
    q = np.array([1.0, 0.0])
    single = [np.array([0.0, 1.0]), np.array([1.0, 1.0])]
    assert np.allclose(distances_to_nearest_segment(q, single), distances_from_embeddings(q, single))   # same as the plain cosine distance
    windows = np.array([[0.0, 1.0], [3.0, 0.1], [-1.0, 0.0]])                                          # the middle window matches the query
    d = distances_to_nearest_segment(q, [single[0], windows, single[1]])
    cos = lambda a, b: a @ b / np.linalg.norm(a) / np.linalg.norm(b)
    assert np.allclose(d, [1 - 0.0, 1 - max(cos(q, w) for w in windows), 1 - cos(q, single[1])])
    assert d[1] < d[2] < d[0]
    mean = windows.mean(axis=0)
    assert d[1] < 1 - cos(q, mean)                                                                       # better than the mean would say


def test_tree_retriever_ranks_a_node_by_its_best_window(tree_and_encoder):
    from qa_graphrag import SEGMENTS_KEY
    tree, enc = tree_and_encoder
    query = "capital Country7 City7"
    index = TreeIndex(tree, enc, RetrievalSettings(top_k=1))
    before = index.retrieve_from_level(query, 0).context
    leaves = tree.layer_to_nodes[0]
    other = next(n for n in leaves if n.text not in before)
    # give an unrelated leaf a window that matches the query exactly while its own single vector stays unrelated
    other.embeddings[SEGMENTS_KEY] = np.stack([other.embeddings[EMB_KEY], enc.create_embedding(query)])
    try:
        after = TreeIndex(tree, enc, RetrievalSettings(top_k=1)).retrieve_from_level(query, 0)
        assert after.context.strip() == other.text.strip()
    finally:
        del other.embeddings[SEGMENTS_KEY]
    assert TreeIndex(tree, enc, RetrievalSettings(top_k=1)).retrieve_from_level(query, 0).context == before   # no segments: the original ranking


def test_cosine_distances_are_the_scipy_values():
    from scipy import spatial

    from raptor.utils import cosine_distances, distances_from_embeddings

    rng = np.random.default_rng(0)
    q = rng.normal(size=16)
    embs = [rng.normal(size=16).astype(np.float32) for _ in range(50)] + [np.zeros(16), 3 * q]
    expected = [spatial.distance.cosine(q, e) for e in embs]
    assert np.allclose(cosine_distances(q, embs), expected, equal_nan=True, atol=1e-9)
    assert np.isnan(cosine_distances(q, embs)[-2]) and np.isnan(expected[-2])                  # a zero vector: nan as before
    assert distances_from_embeddings(q, [list(e) for e in embs[:5]]) == pytest.approx(expected[:5])   # plain lists, returns a list
    assert isinstance(distances_from_embeddings(q, embs[:3]), list)
    assert len(cosine_distances(q, [])) == 0 and distances_from_embeddings(q, []) == []
    assert np.allclose(distances_from_embeddings(q, embs[:5], "L2"), [spatial.distance.euclidean(q, e) for e in embs[:5]])


def test_nearest_segment_distances_with_many_nodes_and_empty_nodes():
    from raptor.utils import distances_to_nearest_segment

    rng = np.random.default_rng(1)
    q = rng.normal(size=8)
    embs = [rng.normal(size=8) if i % 3 else rng.normal(size=(1 + i % 4, 8)) for i in range(300)]
    cos = lambda a, b: a @ b / np.linalg.norm(a) / np.linalg.norm(b)
    expected = [1 - max(cos(q, w) for w in np.atleast_2d(e)) for e in embs]
    assert np.allclose(distances_to_nearest_segment(q, embs), expected)
    assert distances_to_nearest_segment(q, []) == []
    assert distances_to_nearest_segment(q, [embs[1], np.empty((0, 8)), embs[2]])[1] == np.inf


def _big_layer_tree(n=600, dim=12, seed=0, windows_every=7):
    """A tree of one big layer and a small one (nodes with several windows every ``windows_every``)."""
    from raptor import Node, Tree
    from qa_graphrag import SEGMENTS_KEY

    rng = np.random.default_rng(seed)
    nodes = {}
    for i in range(n):
        emb = {EMB_KEY: rng.normal(size=dim).astype(np.float32)}
        if i % windows_every == 0:
            emb[SEGMENTS_KEY] = rng.normal(size=(2 + i % 3, dim)).astype(np.float32)
        nodes[i] = Node(f"leaf {i}", i, set(), emb)
    parents = {}
    for j in range(40):
        idx = n + j
        parents[idx] = Node(f"summary {j}", idx, set(range(j * 15, j * 15 + 15)), {EMB_KEY: rng.normal(size=dim).astype(np.float32)})
    all_nodes = {**nodes, **parents}
    return Tree(all_nodes, list(parents.values()), list(nodes.values()), 1, {0: list(nodes.values()), 1: list(parents.values())})


def test_large_layers_are_ranked_with_the_tree_matrix_like_the_plain_computation():
    from raptor import Node, TreeRetriever, TreeRetrieverConfig

    tree = _big_layer_tree()
    cfg = TreeRetrieverConfig(embedding_model=object.__new__(HashEncoder), context_embedding_model=EMB_KEY, top_k=10, selection_mode="top_k")
    matrix_retriever = TreeRetriever(cfg, tree)
    plain_retriever = TreeRetriever(cfg, tree)
    plain_retriever.LARGE_LAYER = 10 ** 9                                       # never uses the matrix
    matrix_retriever.LARGE_LAYER = 100
    rng = np.random.default_rng(5)
    for layer_nodes in (tree.layer_to_nodes[0], tree.layer_to_nodes[1], tree.layer_to_nodes[0][::3], list(tree.all_nodes.values())):
        for _ in range(5):
            q = rng.normal(size=12).astype(np.float32)
            a = np.asarray(matrix_retriever.node_distances(q, layer_nodes))
            b = np.asarray(plain_retriever.node_distances(q, layer_nodes))
            assert a.shape == b.shape == (len(layer_nodes),) and np.allclose(a, b, atol=1e-5)
            assert list(np.argsort(a)[:10]) == list(np.argsort(b)[:10])           # the same top-k
    assert matrix_retriever._matrix is not None and plain_retriever._matrix is None   # built lazily, only when a large layer is ranked
    foreign = [Node("x", 10 ** 6, set(), {EMB_KEY: np.ones(12, dtype=np.float32)})] * 150      # not part of the tree: plain path
    assert np.allclose(matrix_retriever.node_distances(q, foreign), 1 - 1 / np.sqrt(12) * (q.sum() / np.linalg.norm(q)), atol=1e-5)


def test_retrieval_of_a_big_tree_is_the_same_with_and_without_the_matrix():
    from raptor import TreeRetriever, TreeRetrieverConfig

    tree = _big_layer_tree(n=900, seed=3)
    q = np.random.default_rng(9).normal(size=12).astype(np.float32)
    texts = {}
    for name, limit in (("matrix", 100), ("plain", 10 ** 9)):
        cfg = TreeRetrieverConfig(embedding_model=object.__new__(HashEncoder), context_embedding_model=EMB_KEY, top_k=10, selection_mode="top_k")
        r = TreeRetriever(cfg, tree)
        r.LARGE_LAYER = limit
        r.create_embedding = lambda _text, q=q: q
        nodes, ctx = r.retrieve_information_collapse_tree("q", 10, 100000)
        nodes2, ctx2 = r.retrieve_information(tree.layer_to_nodes[1], "q", 2, 100000)
        texts[name] = (ctx, ctx2, [n.index for n in nodes], [n.index for n in nodes2])
    assert texts["matrix"] == texts["plain"]


def test_tree_index_builds_each_collapse_pool_once(tree_and_encoder):
    tree, enc = tree_and_encoder
    index = TreeIndex(tree, enc, RetrievalSettings(top_k=4, max_tokens=3500, retrieval="collapse"))
    q = "capital Country7 City7"
    first = index.retrieve_start(q, 0)
    pools = dict(index._pools)
    assert set(pools) == {0} and index.retrieve_start(q, 0).context == first.context and index._pools[0] is pools[0]


def test_builder_stores_windows_only_for_texts_that_do_not_fit():
    from qa_graphrag import SEGMENTS_KEY

    class Enc(HashEncoder):
        dim = 16

        def encode_many_with_segments(self, texts):
            vecs = np.stack([self.create_embedding(t) for t in texts])
            return vecs, [np.stack([self.create_embedding(t)] * 2) if len(t.split()) > 30 else None for t in texts]

        def segment_embeddings(self, text):
            return np.stack([self.create_embedding(text)] * 2) if len(text.split()) > 30 else None

    enc = Enc()
    builder = make_builder(enc, FirstWordsSummarizer(), num_layers=2, chunk_tokens=60)
    tree = build_tree(builder, corpus_text(make_corpus(30)))
    leaves = tree.layer_to_nodes[0]
    assert all((SEGMENTS_KEY in n.embeddings) == (len(n.text.split()) > 30) for n in leaves)
    assert any(SEGMENTS_KEY in n.embeddings for n in leaves) and any(SEGMENTS_KEY not in n.embeddings for n in leaves)
    summaries = [n for k, v in tree.layer_to_nodes.items() if k > 0 for n in v]
    assert summaries and all((SEGMENTS_KEY in n.embeddings) == (len(n.text.split()) > 30) for n in summaries)   # create_node does it for summaries too
    assert any(SEGMENTS_KEY in n.embeddings for n in summaries)
    assert all(n.embeddings[EMB_KEY].shape == (16,) for n in tree.all_nodes.values())               # clustering still gets one vector per node


def test_cluster_tokens_reach_the_clustering_and_the_tag():
    from qa_graphrag.runtime import tree_tag
    assert tree_tag("e", "m", 2, 100, 100) == "e|m|L2|c100|s100"                        # defaults: the tags of the cached trees stay valid
    assert tree_tag("e", "m", 2, 1200, 100, cluster_tokens=9600) == "e|m|L2|c1200|s100|m9600"
    assert tree_tag("e", "m", 2, 1200, 100, truncate_long_texts=True).endswith("|trunc")
    builder = make_builder(HashEncoder(), FirstWordsSummarizer(), num_layers=2, cluster_tokens=9600)
    assert builder.clustering_params == {"max_length_in_cluster": 9600}
    assert make_builder(HashEncoder(), FirstWordsSummarizer()).clustering_params == {"max_length_in_cluster": 3500}
    bi = _load_script("build_bench_index")
    assert [bi.bench_cluster_tokens(c) for c in (100, 200, 437, 1200)] == [3500, 3500, 3500, 9600]


def test_max_tokens_truncates_every_retrieval_mode(tree_and_encoder):
    tree, enc = tree_and_encoder
    index = TreeIndex(tree, enc, RetrievalSettings(top_k=5, max_tokens=60))
    tok = index.retriever.tokenizer
    for r in (index.retrieve_from_level("capital Country3", index.max_level), index.retrieve_collapsed("capital Country3")):
        assert len(tok.encode(r.context)) <= 60 + 100          # at most one node beyond the budget is never added


@pytest.mark.parametrize("method", ["bm25", "tfidf"])
def test_flat_baselines_find_the_matching_chunk(tree_and_encoder, method):
    tree, _ = tree_and_encoder
    chunks = [n.text for n in tree.layer_to_nodes[0]]
    r = FlatRetriever(chunks, method, top_k=2).retrieve("capital of Country7 City7")
    assert "City7" in r.context


def test_extract_final_answer():
    from qa_graphrag.prompts import extract_final_answer as ex
    assert ex("REASONING: A is the mother of B. B was born in Rome.\nANSWER: Rome") == "Rome"
    assert ex("REASONING: x\nANSWER:\n**Rome**\nbecause") == "Rome"                    # first non-empty line, markdown stripped
    assert ex("Answer: first\nREASONING: again\nANSWER: second") == "second"          # the last tag wins, case-insensitive
    assert ex("REASONING: it is Rome but the text is cut off") == ""                  # cut off while reasoning: not scored
    assert ex("Rome") == "Rome" and ex("  ") == ""                                    # a short untagged answer is kept
    assert ex("word " * 40) == ""                                                      # a long untagged text cannot inflate the substring metric
    assert ex("REASONING: Obama\nANSWER: Hawaii") == "Hawaii"                         # the reasoning is not part of the prediction


def test_prompts_have_their_placeholders_and_describe_the_context():
    from qa_graphrag.prompts import BENCH_TASK_INSTRUCTION, KGQA_PROMPT, build_bench_prompt
    p = KGQA_PROMPT.format(context="CTX-TEXT", question="Q-TEXT")
    assert "CTX-TEXT" in p and "Q-TEXT" in p and "{" not in p
    assert "summary" in p and "step by step" in p and "ANSWER:" in p
    ex = {"Question": "Which?", "Choices": {"A": "x", "B": "y"}}
    for task in BENCH_TASK_INSTRUCTION:
        b = build_bench_prompt(task, ex, "CTX-TEXT")
        assert "CTX-TEXT" in b and "RATIONALE:" in b and "ANSWER:" in b and "summary" in b and "{" not in b
        assert BENCH_TASK_INSTRUCTION[task] in b and "A: x" in b
        # TF has its own head without "do not hedge" / "never leave it empty" (they pushed the model towards False)
        assert ("never leave it empty" in b) == (task != "TF") and ("do not hedge" in b) == (task != "TF")
    from qa_graphrag.prompts import BENCH_ANSWER_FORMAT
    # the model copies the example literally: an example followed by a colon ("B:") came back as the answer "B:"
    assert not re.search(r"\b[A-D]:", BENCH_ANSWER_FORMAT["MC"]) and ":" not in BENCH_ANSWER_FORMAT["TF"]


def test_prompts_ask_for_reasoning_and_a_tagged_answer():
    from qa_graphrag import prompts as p
    ex = {'Question': 'Q?', 'Choices': {'A': 'x', 'B': 'y'}}
    assert "summary" in p.KGQA_PROMPT and "REASONING:" in p.KGQA_PROMPT
    b = p.build_bench_prompt('MC', ex, 'CTX')
    assert "summary" in b and "own knowledge" in b and "never leave it empty" in b and "e.g. B>" not in b
    assert p.extract_final_answer('REASONING: x\nANSWER: y') == "y"


def test_runner_scores_only_the_extracted_answer(tree_and_encoder):
    tree, enc = tree_and_encoder

    class Reasoner:
        def chat(self, prompt, max_tokens=64, **kw):
            return "REASONING: the answer might be Paris\nANSWER: Rome"

    runner = QueryRunner(TreeIndex(tree, enc), Reasoner())
    o = runner.run("bm25", "capital?")
    assert o.prediction == "Rome" and "Paris" in o.raw and metrics.score_example(o.prediction, ["Paris"])["acc"] == 0.0
    o = runner.run("bm25", "capital?", prompt_fn=lambda c, q: q)                      # a custom prompt keeps the whole response
    assert o.prediction == o.raw


def test_mixed_prompt_versions_are_refused(tmp_path):
    from qa_graphrag.data import append_jsonl, refuse_other_prompt
    path = tmp_path / "r.jsonl"
    refuse_other_prompt(path, "v2")                                                    # no file: fine
    append_jsonl(path, {"id": "1", "prompt": "v2"})
    refuse_other_prompt(path, "v2")
    append_jsonl(path, {"id": "2"})                                                    # rows without the field: an older prompt
    with pytest.raises(SystemExit):
        refuse_other_prompt(path, "v2")


def test_runner_routes_and_answers(tree_and_encoder):
    tree, enc = tree_and_encoder
    index = TreeIndex(tree, enc)
    router = MLPRouter(RouterConfig(enc.dim, 3))
    runner = QueryRunner(index, EchoLLM(), router)
    for method in ("bm25", "tfidf", "raptor", "raptor-collapsed", "level0", "level1", "raptor-qa"):
        out = runner.run(method, "What is the capital of Country7?")
        assert out.prediction == "answer" and out.times["total"] >= 0
    out = runner.run("raptor-qa", "What is the capital of Country7?")
    assert out.level in (0, 1, 2) and len(out.preference) == 3
    assert len(runner.run_all_levels("capital?")) == index.max_level + 1
    with pytest.raises(ValueError):
        runner.run("nonsense", "q")


# ---------------------------------------------------------------- metrics
def test_kgqa_metrics():
    s = metrics.score_example("The answer is Barack Obama.", ["Obama", "Barack Hussein Obama"])
    assert s["acc"] == 1.0 and s["recall"] == 1.0
    s = metrics.score_example("Paris", ["London"])
    assert s == {"acc": 0.0, "recall": 0.0}
    assert metrics.score_example("blue whale", ["the blue whale"])["acc"] == 1.0
    assert metrics.token_recall("yes", "no") == 0.0


# ---------------------------------------------------------------- LLM endpoint settings
def test_default_roles(monkeypatch):
    from qa_graphrag.settings import get_llm_spec

    for role in ("BACKBONE", "SUMMARIZER", "JUDGE"):
        for name in ("BASE_URL", "MODEL", "API_KEY", "THINKING"):
            monkeypatch.delenv(f"{role}_{name}", raising=False)
    monkeypatch.setenv("DEEPSEEK_API_KEY", "k")
    for role in ("backbone", "summarizer"):
        spec = get_llm_spec(role)
        assert spec.model == "Qwen/Qwen2.5-7B-Instruct" and spec.base_url == "http://localhost:8000/v1" and spec.extra_body == {}
    judge = get_llm_spec("judge")
    assert judge.model == "deepseek-flash" and judge.base_url == "https://api.deepseek.com"
    assert judge.extra_body == {"thinking": {"type": "disabled"}}


def test_deepseek_endpoints_disable_thinking(monkeypatch):
    from qa_graphrag.settings import get_llm_spec

    for k in ("BACKBONE_THINKING", "SUMMARIZER_THINKING", "JUDGE_THINKING"):
        monkeypatch.delenv(k, raising=False)
    monkeypatch.setenv("BACKBONE_BASE_URL", "https://api.deepseek.com")
    monkeypatch.setenv("BACKBONE_MODEL", "deepseek-flash")
    monkeypatch.setenv("BACKBONE_API_KEY", "k")
    monkeypatch.setenv("DEEPSEEK_API_KEY", "k")
    for role in ("backbone", "summarizer", "judge"):
        assert get_llm_spec(role).extra_body == {"thinking": {"type": "disabled"}}
    monkeypatch.setenv("BACKBONE_BASE_URL", "http://localhost:8000/v1")
    assert get_llm_spec("backbone").extra_body == {}
    monkeypatch.setenv("BACKBONE_BASE_URL", "https://api.deepseek.com")
    monkeypatch.setenv("BACKBONE_THINKING", "enabled")
    assert get_llm_spec("backbone").extra_body == {"thinking": {"type": "enabled"}}


# ---------------------------------------------------------------- multi-GPU helpers (replicas, shards)
def test_chat_llm_round_robin_over_replicas():
    from collections import Counter
    from types import SimpleNamespace

    from qa_graphrag.llm import ChatLLM
    from qa_graphrag.settings import LLMSpec

    llm = ChatLLM(LLMSpec(base_url="http://a:1/v1, http://b:2/v1,http://c:3/v1", model="m", api_key="k"))
    assert len(llm.clients) == 3 and llm.client is llm.clients[0]
    seen = Counter()
    for client in llm.clients:   # record which replica got the request
        client.chat = SimpleNamespace(completions=SimpleNamespace(create=lambda _c=client, **kw: (
            seen.update([str(_c.base_url)]),
            SimpleNamespace(choices=[SimpleNamespace(message=SimpleNamespace(content=" ok "))]))[1]))
    assert all(llm.chat("hi") == "ok" for _ in range(9))
    assert sorted(seen.values()) == [3, 3, 3]


def test_shards_are_disjoint_and_cover_everything():
    from qa_graphrag.data import longest_first, parse_shard, take_shard

    assert parse_shard(None) == (0, 1) and parse_shard("3/8") == (3, 8)
    for bad in ("8/8", "-1/4"):
        with pytest.raises(ValueError):
            parse_shard(bad)
    items = list(range(23))
    parts = [take_shard(items, (i, 5)) for i in range(5)]
    assert sorted(x for p in parts for x in p) == items and sum(map(len, parts)) == len(items)
    exs = [{"id": i, "ctxs": [{"text": "x" * n}]} for i, n in enumerate([3, 30, 10])]
    assert [e["id"] for e in longest_first(exs)] == [1, 2, 0]


def test_sampling_with_shards_partitions_the_sample(tmp_path, monkeypatch):
    import pyarrow as pa
    import pyarrow.parquet as pq

    from qa_graphrag import data

    for f in range(3):
        rows = {"id": [f"{f}-{r}" for r in range(40)], "text": [f"t{f}-{r}" for r in range(40)]}
        pq.write_table(pa.table(rows), tmp_path / f"part{f}.parquet")
    monkeypatch.setattr(data, "_download", lambda repo, name: str(tmp_path / name))

    def sample(shard):
        return data._sample_from_shards(
            "repo", "part{i}.parquet", 3, 30, 0, ["id"], lambda r: {"id": r["id"]}, ["text"],
            lambda light, rec: {**light, "text": rec["text"]}, min_shards=3, shard=shard)

    full = sample((0, 1))
    parts = [sample((i, 4)) for i in range(4)]
    assert len(full) == 30
    assert sorted(e["id"] for p in parts for e in p) == sorted(e["id"] for e in full)
    assert all(e["text"] == "t" + e["id"] for p in parts for e in p)


def test_append_jsonl_from_many_processes(tmp_path):
    import multiprocessing as mp

    from qa_graphrag.data import done_ids

    path = tmp_path / "out.jsonl"
    procs = [mp.Process(target=_write_records, args=(str(path), p)) for p in range(4)]
    [p.start() for p in procs]
    [p.join() for p in procs]
    assert len(done_ids(path)) == 4 * 50   # every line intact and parseable


def _write_records(path, p):
    from qa_graphrag.data import append_jsonl

    for i in range(50):
        append_jsonl(path, {"id": f"{p}-{i}", "pad": "x" * 20000})


def test_parallel_unordered_yields_everything():
    from qa_graphrag.llm import parallel_unordered

    assert sorted(parallel_unordered(lambda x: x * 2, range(20), workers=4)) == [x * 2 for x in range(20)]
    assert list(parallel_unordered(lambda x: x, [1, 2, 3], workers=1)) == [1, 2, 3]


def test_reclustering_terminates_when_gmm_returns_one_cluster(monkeypatch):
    """Upstream RAPTOR recursed forever when an over-long cluster was reclustered into itself."""
    from raptor import cluster_utils
    from raptor.tree_structures import Node

    words = "alpha beta gamma delta " * 30   # ~120 tokens per node
    nodes = [Node(f"{i} {words}", i, set(), {"EMB": np.random.RandomState(i).rand(8)}) for i in range(60)]
    monkeypatch.setattr(cluster_utils, "perform_clustering",
                        lambda emb, dim, threshold, verbose=False: [np.array([0.0]) for _ in range(len(emb))])
    clusters = cluster_utils.RAPTOR_Clustering.perform_clustering(nodes, "EMB", max_length_in_cluster=1000)
    assert sorted(n.index for c in clusters for n in c) == list(range(60))   # every node kept exactly once
    tok = cluster_utils.tiktoken.get_encoding("cl100k_base")
    assert len(clusters) > 1 and all(
        sum(len(tok.encode(n.text)) for n in c) <= 1000 or len(c) == 1 for c in clusters)


def test_nodes_with_identical_embeddings_are_not_multiplied():
    """Upstream matched cluster members by embedding value, so duplicated embeddings were added to every cluster
    containing any of them (1319 clusters for one chunk on textbook15)."""
    from raptor import cluster_utils

    rng = np.random.RandomState(0)
    centers = rng.randn(4, 16)
    emb = np.vstack([centers[i % 4] + 0.05 * rng.randn(16) for i in range(120)])
    emb[:20] = emb[0]                                   # 20 nodes with the very same embedding
    clusters = cluster_utils.perform_clustering(emb, dim=5, threshold=0.1)
    per_node = [len(c) for c in clusters]
    assert max(per_node) <= 4, per_node                 # a node belongs to a handful of clusters at most
    assert all(len(c) >= 1 for c in clusters)


def test_cluster_with_one_or_two_overlong_nodes_is_split_not_reclustered(monkeypatch):
    """UMAP raises 'n_components must be greater than 0' for 1-2 points; such a cluster can only be split."""
    from raptor import cluster_utils
    from raptor.tree_structures import Node

    def fake(emb, dim, threshold, verbose=False):
        if len(emb) - 2 < 1:
            raise ValueError("n_components must be greater than 0")
        return [np.array([0.0]) if i < 2 else np.array([1.0]) for i in range(len(emb))]

    monkeypatch.setattr(cluster_utils, "perform_clustering", fake)
    long_text = "alpha beta gamma delta " * 500        # ~2000 tokens: two of them exceed the 3500 limit
    nodes = [Node(long_text if i < 2 else "short text", i, set(), {"E": np.random.RandomState(i).rand(8)}) for i in range(12)]
    clusters = cluster_utils.RAPTOR_Clustering.perform_clustering(nodes, "E", max_length_in_cluster=3500)
    assert sorted(n.index for c in clusters for n in c) == list(range(12))


def test_duplicate_embedding_stats(tree_and_encoder):
    from raptor import Node, Tree

    clean = duplicate_embedding_stats(tree_and_encoder[0])
    assert not clean["affected"] and clean["max_group"] == 1

    v, w = np.ones(4, dtype=np.float32), np.arange(4, dtype=np.float32)
    leaves = {i: Node(f"t{i}", i, set(), {EMB_KEY: v if i < 3 else w + i}) for i in range(5)}   # 3 identical + 2 distinct
    top = {9: Node("s", 9, {0, 1}, {EMB_KEY: v})}
    layer_to_nodes = {0: list(leaves.values()), 1: list(top.values())}
    stats = duplicate_embedding_stats(Tree({**leaves, **top}, top, leaves, 1, layer_to_nodes))
    assert stats["affected"] and stats["max_group"] == 3
    assert stats["layers"][0] == {"layer": 0, "nodes": 5, "dup_groups": 1, "dup_nodes": 3, "max_group": 3}
    # duplicates only in the top (never clustered) layer do not count
    twin = {i: Node("s", i, set(), {EMB_KEY: v}) for i in (8, 9)}
    top_dup = Tree({**leaves, **twin}, twin, leaves, 1, {0: [leaves[3], leaves[4]], 1: list(twin.values())})
    assert not duplicate_embedding_stats(top_dup)["affected"]


def test_summarizer_shrinks_context_on_context_length_error():
    from types import SimpleNamespace

    from openai import BadRequestError

    from qa_graphrag.llm import LLMSummarizationModel

    def resp():
        return SimpleNamespace(status_code=400, headers={}, request=None)

    msg = ("This model's maximum context length is 8192 tokens. However, you requested 12080 tokens "
           "(11980 in the messages, 100 in the completion). Please reduce the length of the messages or completion.")
    calls = []

    class FakeLLM:
        def chat(self, prompt, max_tokens=256, **kw):
            calls.append(len(prompt))
            if len(prompt) > 8000:                       # pretend 1 char = 1 token
                raise BadRequestError(msg.replace("11980", str(len(prompt))), response=resp(), body=None)
            return "ok"

    out = LLMSummarizationModel(FakeLLM()).summarize("x" * 11980, max_tokens=100)
    assert out == "ok" and len(calls) == 2 and calls[1] < 8000 - 100
    class AlwaysBad:
        def chat(self, prompt, max_tokens=256, **kw):
            raise BadRequestError("some other 400", response=resp(), body=None)
    with pytest.raises(BadRequestError):                 # unrelated 400s are not swallowed
        LLMSummarizationModel(AlwaysBad()).summarize("x")

    class NeverFits:                                     # context error no matter how short the prompt gets
        n = 0

        def chat(self, prompt, max_tokens=256, **kw):
            NeverFits.n += 1
            raise BadRequestError(msg, response=resp(), body=None)

    text = "head of the text. " + "x" * 5000
    out = LLMSummarizationModel(NeverFits()).summarize(text, max_tokens=100)
    assert NeverFits.n == LLMSummarizationModel.MAX_SHRINKS + 1
    assert out and text.startswith(out) and len(out) <= 100 * LLMSummarizationModel.FALLBACK_CHARS_PER_TOKEN


# ---------------------------------------------------------------- native NQ rendering
def test_render_nq_document_drops_tags_and_keeps_structure():
    from qa_graphrag.data import render_nq_document

    toks = ["<H1>", "Walking", "Dead", "(", "season", "8", ")", "</H1>", "<P>", "It", "aired", "on", "March", "18", ",", "2018",
            ".", "The", "three", "-", "quarters", "rule", "'s", "here", "</P>", "<Table>", "<Tr>", "<Th>", "Starring", "</Th>",
            "<Td>", "Andrew", "Lincoln", "</Td>", "</Tr>", "</Table>"]
    is_html = [t.startswith("<") and t.endswith(">") for t in toks]
    text = render_nq_document("Page", {"token": toks, "is_html": is_html})
    assert "<" not in text
    assert text.splitlines() == [
        "Page", "Walking Dead (season 8)", "It aired on March 18, 2018. The three-quarters rule's here", "Starring | Andrew Lincoln",
    ]


# ---------------------------------------------------------------- GraphRAG-Bench evaluation
class FakeJudge:
    workers = 1

    def rationale(self, pred, gold):
        return 1.0 if pred == gold else 0.5

    def answer(self, pred, gold):
        return 1.0 if pred.lower() == gold.lower() else 0.0


def test_extract_feature_matches_official_parser():
    assert bench_eval.extract_feature("RATIONALE: because.\nANSWER: B\nextra") == ["because.", "B"]
    assert bench_eval.extract_feature("no marker here") == ("", "")


def test_bench_scoring_rules_and_ar_table():
    gold = {
        "MC": [{"Rationale": "r", "Answer": "B", "Level-1 Topic": "T"}],
        "MS": [{"Rationale": "r", "Answer": "ABC", "Level-1 Topic": "T"}, {"Rationale": "r", "Answer": "AB", "Level-1 Topic": "T"}],
        "FB": [{"Rationale": "r", "Answer": "method", "Level-1 Topic": "T"}],
    }
    preds = {
        "MC": ["RATIONALE: r\nANSWER: B"],
        "MS": ["RATIONALE: r\nANSWER: AB", "RATIONALE: x\nANSWER: AC"],
        "FB": ["RATIONALE: x\nANSWER: Method"],
    }
    res = bench_eval.run_eval(gold, preds, FakeJudge())
    d = res["details"]
    assert d["MC"][0]["answer_score"] == 1.0 and d["MC"][0]["ar_score"] == 1.0
    assert d["MS"][0]["answer_score"] == 0.5 and d["MS"][1]["answer_score"] == 0.0   # subset / wrong
    assert d["FB"][0]["answer_score"] == 1.0 and d["FB"][0]["ar_score"] == 0.5        # answer ok, rationale 0.5
    assert res["total"]["count"] == 4 and res["by_type"]["MS"]["count"] == 2
    assert bench_eval.calculate_ar_score(0, 0.5) == 0.25 and bench_eval.calculate_ar_score(0, 1) == 0.5

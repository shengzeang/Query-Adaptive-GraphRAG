"""How much do the retrieval levels overlap, and does the overlap explain the router labels?

For a sample of the questions of the router label files, this reloads each question's cached RAPTOR tree, repeats the
retrieval from every level (no LLM call, CPU only) and compares what the levels hand to the generator:

* **what a level retrieves**: nodes, leaf chunks, and how often the gold answer string is inside the context;
* **leaf overlap** between two levels (identical leaf sets, Jaccard, share of the lower level's leaves kept);
* **link to the labels**: how often the two levels' labels differ, split by leaf overlap and by whether the gold answer
  is present in both contexts. A label difference between levels whose contexts hold the same leaves and the same
  answer availability cannot come from retrieval; it comes from the extra summaries or from generation variation.
* **where the oracle gain comes from, and whether it can be learned**: the oracle's gain over the best fixed level is
  split into the questions whose levels differ in answer availability and the rest; a router that knew where the answer
  is shows how much of it that knowledge could capture. Then, from the question embedding alone (all the router sees):
  a logistic regression predicts "answer in the level-0 context" and "levels differ in availability" (AUC next to the
  label-shuffled AUC), and routers trained on the accuracy labels and on the noise-free availability labels are
  cross-validated against the best fixed level and against an uninformed router with the same level distribution.
  ``--no-learnability`` skips the training. Per-question results go to ``<out stem>_records.jsonl``.

    python scripts/measure_level_overlap.py --data data/router/{hotpotqa,nq,triviaqa}.jsonl --n 2000 \
        --cache-dir indexes --out outputs/level_overlap_full.json

Trees are looked up like ``gen_router_data.py`` stores them (namespace = the row's ``source``; key = ``<id>|<tree tag>``), so the encoder / tree settings and the summariser model
(``SUMMARIZER_MODEL`` / ``BACKBONE_MODEL``, or ``--summarizer-model``) must be those used to build the trees; questions
whose tree is not found are counted and skipped. Retrieval uses each row's own ``top_k`` (rows made before it was
recorded: 5) and the default token budget, i.e. the conditions of the labels. Query embeddings are recomputed, so a
near-tie in similarity can resolve differently than when the labels were made. Only levels the tree really has are
compared (the others are copies of the top one).
"""
import argparse
import json
import pickle
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np
from tqdm import tqdm

from qa_graphrag import NUM_TREE_LAYERS
from qa_graphrag.data import read_jsonl
from qa_graphrag.embedding import DEFAULT_ENCODER, SBertEncoder
from qa_graphrag.index import cache_path
from qa_graphrag.metrics import normalize_answer
from qa_graphrag.retrieval import RetrievalSettings, TreeIndex
from qa_graphrag.runtime import tree_tag
from qa_graphrag.settings import get_llm_spec

BUCKETS = ("same leaves", "jaccard >= 0.5", "jaccard > 0", "no common leaf")


def jaccard(a, b) -> float:
    union = len(a | b)
    return len(a & b) / union if union else 1.0


def kept_share(low, high) -> float:
    """Share of the leaves of ``low`` that ``high`` also retrieves."""
    return len(low & high) / len(low) if low else 1.0


def bucket(j: float) -> str:
    return BUCKETS[0] if j == 1 else BUCKETS[1] if j >= 0.5 else BUCKETS[2] if j > 0 else BUCKETS[3]


def answer_in(context: str, golds_norm) -> bool:
    ctx = normalize_answer(context)
    return any(g and g in ctx for g in golds_norm)


def question_record(index: TreeIndex, row: dict, source: str) -> dict:
    """What every real level retrieves for one question, plus the question's labels."""
    tree = index.tree
    leaf_ids = {n.index for n in tree.layer_to_nodes[0]}
    golds = [normalize_answer(a) for a in row["answers"]]
    levels = range(min(len(row["acc"]), tree.num_layers + 1))
    leaves, n_nodes, has_answer = [], [], []
    for k in levels:
        nodes, context = index._start(row["question"], k)      # in the retrieval mode of the labels (the index's settings)
        leaves.append(frozenset(n.index for n in nodes if n.index in leaf_ids))
        n_nodes.append(len(nodes))
        has_answer.append(answer_in(context, golds))
    return {"source": source, "id": str(row.get("id", "")), "question": row["question"],
            "num_levels": len(levels), "all_levels": len(row["acc"]), "leaves": leaves,
            "n_nodes": n_nodes, "has_answer": has_answer, "acc": list(row["acc"])[: len(levels)],
            "acc_all": list(row["acc"])}


def pct(x) -> str:
    return "   -  " if x is None else f"{100 * x:5.1f}%"


def summarize(records: list) -> dict:
    """Tables for a list of ``question_record`` dicts (one group of questions)."""
    K = max((r["all_levels"] for r in records), default=0)
    per_level = []
    for k in range(K):
        rs = [r for r in records if r["num_levels"] > k]
        per_level.append({
            "level": k, "n": len(rs),
            "nodes": float(np.mean([r["n_nodes"][k] for r in rs])) if rs else None,
            "leaves": float(np.mean([len(r["leaves"][k]) for r in rs])) if rs else None,
            "answer_in_context": float(np.mean([r["has_answer"][k] for r in rs])) if rs else None,
        })
    pairs, link = [], []
    for a in range(K):
        for b in range(a + 1, K):
            rs = [r for r in records if r["num_levels"] > b]
            if not rs:
                continue
            js = [jaccard(r["leaves"][a], r["leaves"][b]) for r in rs]
            pairs.append({
                "pair": [a, b], "n": len(rs), "same_leaves": float(np.mean([j == 1 for j in js])),
                "jaccard": float(np.mean(js)),
                "low_kept": float(np.mean([kept_share(r["leaves"][a], r["leaves"][b]) for r in rs])),
                "labels_differ": float(np.mean([r["acc"][a] != r["acc"][b] for r in rs])),
            })
            link += [{"bucket": bucket(j), "label_differs": r["acc"][a] != r["acc"][b],
                      "answer_differs": r["has_answer"][a] != r["has_answer"][b]} for j, r in zip(js, rs)]
    by_bucket = {}
    for name in BUCKETS:
        sel = [x for x in link if x["bucket"] == name]
        by_bucket[name] = {"n": len(sel), "labels_differ": float(np.mean([x["label_differs"] for x in sel])) if sel else None}
    by_answer = {}
    for name, flag in (("answer availability equal", False), ("answer availability differs", True)):
        sel = [x for x in link if x["answer_differs"] == flag]
        by_answer[name] = {"n": len(sel), "labels_differ": float(np.mean([x["label_differs"] for x in sel])) if sel else None}
    full = [r for r in records if r["num_levels"] == r["all_levels"] and r["all_levels"] > 1]   # trees with every level
    disagree = lambda rs: float(np.mean([len(set(r["acc"])) > 1 for r in rs])) if rs else None
    same = [r for r in full if len(set(r["has_answer"])) == 1]
    differ = [r for r in full if len(set(r["has_answer"])) > 1]
    questions = {
        "n": len(full), "answer_equal_at_all_levels": len(same) / len(full) if full else None,
        "labels_disagree": disagree(full), "labels_disagree_if_answer_equal": disagree(same),
        "labels_disagree_if_answer_differs": disagree(differ), "n_answer_differs": len(differ),
    }
    return {"n": len(records), "per_level": per_level, "pairs": pairs, "by_bucket": by_bucket, "by_answer": by_answer,
            "questions": questions}


def padded_matrix(rows: list, K: int) -> np.ndarray:
    """``[N, K]`` matrix; a row shorter than ``K`` repeats its last value (the labels do the same for missing levels)."""
    return np.array([list(r) + [r[-1]] * (K - len(r)) for r in rows], dtype=np.float32)


def oracle_decomposition(acc: np.ndarray, avail: np.ndarray) -> dict:
    """Where does the oracle's gain over the best fixed level come from?

    ``acc [N, K]`` are the label scores, ``avail [N, K]`` is 1 where the gold answer is inside that level's context.
    Per question the oracle gains ``max_k acc - acc[best fixed level]``. Questions whose levels differ in answer
    availability are the ones a retrieval-aware router could act on; for the others the contexts hold the answer at all
    levels or at none, so a label difference there is not about what was retrieved. The "availability oracle" is a
    router that knows ``avail`` and takes the best fixed level if it holds the answer, else the lowest level that does
    (if there is none, the best fixed level): it shows how much of the oracle gain such knowledge could capture.
    """
    n, K = acc.shape
    means = acc.mean(0)
    fixed = int(means.argmax())
    gain_q = acc.max(1) - acc[:, fixed]
    differs = avail.max(1) != avail.min(1)
    choice = np.full(n, fixed)
    for i in np.flatnonzero(~avail[:, fixed].astype(bool)):
        has = np.flatnonzero(avail[i])
        if len(has):
            choice[i] = has[0]
    informed = float(acc[np.arange(n), choice].mean())
    oracle = float(acc.max(1).mean())
    gain = oracle - float(means[fixed])
    return {
        "n": n, "level_means": means.round(4).tolist(), "best_fixed_level": fixed, "best_fixed": float(means[fixed]),
        "oracle": oracle, "oracle_gain": gain,
        "share_availability_differs": float(differs.mean()),
        "gain_from_availability_differs": float(gain_q[differs].sum() / n),
        "gain_from_availability_equal": float(gain_q[~differs].sum() / n),
        "availability_oracle": informed, "availability_oracle_gain": informed - float(means[fixed]),
        "answer_in_level0": float(avail[:, 0].mean()),
    }


def availability_auc(X: np.ndarray, y: np.ndarray, folds: int = 5, seed: int = 0, n_shuffles: int = 10) -> dict:
    """Cross-validated ROC AUC of a logistic regression from the question embedding to the binary ``y``, next to the
    AUC obtained on label-shuffled copies of ``y`` (what "no signal" looks like for this sample size)."""
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import roc_auc_score
    from sklearn.model_selection import StratifiedKFold, cross_val_predict

    y = np.asarray(y).astype(int)
    if y.min() == y.max() or min(y.sum(), len(y) - y.sum()) < folds:
        return {"positives": int(y.sum()), "n": int(len(y)), "auc": None, "shuffled_auc_mean": None, "shuffled_auc_sd": None}
    cv = StratifiedKFold(folds, shuffle=True, random_state=seed)

    def auc_of(labels):
        p = cross_val_predict(LogisticRegression(C=0.1, max_iter=500), X, labels, cv=cv, method="predict_proba")[:, 1]
        return float(roc_auc_score(labels, p))

    rng = np.random.RandomState(seed)
    shuffled = [auc_of(rng.permutation(y)) for _ in range(n_shuffles)]
    return {"positives": int(y.sum()), "n": int(len(y)), "auc": auc_of(y),
            "shuffled_auc_mean": float(np.mean(shuffled)), "shuffled_auc_sd": float(np.std(shuffled, ddof=1))}


def router_learnability(X: np.ndarray, acc: np.ndarray, avail: np.ndarray, folds: int, seed: int, epochs: int) -> list:
    """CV score (accuracy of the level the router picks, on questions it was not trained on) of routers trained on
    the accuracy labels and on the answer-availability labels. The latter have no generation noise, so they are the
    easier thing to learn: if even they do not beat the best fixed level, the question embedding does not tell
    which level to use. ``chance`` is what a router without information scores with the same level distribution."""
    from qa_graphrag.router import cross_validate

    K = acc.shape[1]
    setups = [("accuracy labels, Gumbel-Softmax loss (paper)", acc, dict(loss="gumbel")),
              ("accuracy labels, mse, skip ties", acc, dict(loss="mse", skip_ties=True)),
              ("answer-availability labels, mse, skip ties", avail, dict(loss="mse", skip_ties=True))]
    out = []
    for name, P_train, kw in setups:
        try:
            scores, choices = cross_validate(X, P_train, acc, n_folds=folds, seed=seed, return_choices=True, epochs=epochs, **kw)
        except ValueError as e:     # e.g. skip_ties when no training question tells the levels apart
            out.append({"setup": name, "error": str(e)})
            continue
        dist = np.bincount(choices, minlength=K) / len(choices)
        out.append({"setup": name, "cv": float(np.mean(scores)), "se": float(np.std(scores, ddof=1) / np.sqrt(len(scores))),
                    "level_distribution": dist.round(4).tolist(), "chance": float((dist * acc.mean(0)).sum())})
    return out


def print_decomposition(name: str, d: dict) -> None:
    lv = "  ".join(f"lvl{k} {m:.3f}" for k, m in enumerate(d["level_means"]))
    print(f"\n--- {name} ({d['n']} questions): {lv}")
    print(f"    oracle {d['oracle']:.3f} = best fixed (level {d['best_fixed_level']}) {d['best_fixed']:.3f} + {d['oracle_gain']:.3f}")
    print(f"    {d['share_availability_differs']:.1%} of the questions have contexts that differ in answer availability; "
          f"they carry {d['gain_from_availability_differs']:.3f} of the oracle gain, the other questions {d['gain_from_availability_equal']:.3f}")
    cap = d["availability_oracle_gain"] / d["oracle_gain"] if d["oracle_gain"] > 0 else float("nan")
    print(f"    a router that knew where the answer is would reach {d['availability_oracle']:.3f} "
          f"(+{d['availability_oracle_gain']:.3f}, {cap:.0%} of the oracle gain)")


def print_group(name: str, s: dict) -> None:
    print(f"\n=== {name}  ({s['n']} questions) ===")
    print("what a level retrieves:   level   n   nodes  leaves  answer in context")
    for p in s["per_level"]:
        if p["n"]:
            print(f"                          {p['level']:>5}{p['n']:>5}{p['nodes']:>8.1f}{p['leaves']:>8.1f}{pct(p['answer_in_context']):>14}")
    print("leaf overlap of two levels:  pair     n  same leaves  mean jaccard  low level's leaves kept  labels differ")
    for p in s["pairs"]:
        print(f"                           {p['pair'][0]}-{p['pair'][1]}{p['n']:>7}{pct(p['same_leaves']):>13}{p['jaccard']:>14.3f}"
              f"{pct(p['low_kept']):>24}{pct(p['labels_differ']):>15}")
    print("do the labels of two levels differ?  (all pairs pooled; pairs of one question are not independent)")
    for name_, v in {**s["by_bucket"], **s["by_answer"]}.items():
        print(f"    {name_:<30}{v['n']:>7} pairs   labels differ {pct(v['labels_differ'])}")
    q = s["questions"]
    if q["n"]:
        print(f"questions with every level ({q['n']}): the gold answer is in all or in none of the contexts for "
              f"{pct(q['answer_equal_at_all_levels'])}; labels disagree {pct(q['labels_disagree'])} overall, "
              f"{pct(q['labels_disagree_if_answer_equal'])} if answer availability is equal, "
              f"{pct(q['labels_disagree_if_answer_differs'])} if it differs ({q['n_answer_differs']} questions)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", nargs="+", required=True, help="router label files written by gen_router_data.py")
    ap.add_argument("--n", type=int, default=300, help="questions sampled per file (all if the file is smaller)")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--cache-dir", default="indexes")
    ap.add_argument("--encoder", default=DEFAULT_ENCODER)
    ap.add_argument("--device", default=None)
    ap.add_argument("--tree-layers", type=int, default=NUM_TREE_LAYERS)
    ap.add_argument("--chunk-tokens", type=int, default=100)
    ap.add_argument("--summary-tokens", type=int, default=100)
    ap.add_argument("--summarizer-model", default=None, help="model name inside the tree tag (default: from the environment)")
    ap.add_argument("--no-learnability", action="store_true", help="only the overlap tables (no router / classifier training)")
    ap.add_argument("--folds", type=int, default=5)
    ap.add_argument("--epochs", type=int, default=100)
    ap.add_argument("--out", default="outputs/level_overlap.json")
    args = ap.parse_args()

    tag = tree_tag(args.encoder, args.summarizer_model or get_llm_spec("summarizer").model, args.tree_layers,
                   args.chunk_tokens, args.summary_tokens)
    print(f"tree tag: {tag}")
    encoder = SBertEncoder(args.encoder, device=args.device)

    records, missing = [], {}
    for path in args.data:
        rows = read_jsonl(path)
        rows = random.Random(args.seed).sample(rows, min(args.n, len(rows)))
        for row in tqdm(rows, desc=Path(path).name, mininterval=10):
            source = row["source"]
            tree_path = cache_path(args.cache_dir, source, f"{row['id']}|{tag}")
            if not tree_path.exists():
                missing[source] = missing.get(source, 0) + 1
                continue
            with open(tree_path, "rb") as f:
                tree = pickle.load(f)
            index = TreeIndex(tree, encoder, RetrievalSettings(top_k=row.get("top_k", 5),
                                                               retrieval=row.get("retrieval", "traverse")))
            records.append(question_record(index, row, source))
    if missing:
        print(f"trees not found (skipped): {missing}")
    if not records:
        sys.exit(f"no trees found under {args.cache_dir}: check --cache-dir and the tree tag above (--summarizer-model)")

    result = {"tag": tag, "missing": missing}
    for name in sorted({r["source"] for r in records}) + ["ALL"]:
        group = records if name == "ALL" else [r for r in records if r["source"] == name]
        result[name] = summarize(group)
        print_group(name, result[name])
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    K = max(r["all_levels"] for r in records)
    acc = padded_matrix([r["acc_all"] for r in records], K)
    avail = padded_matrix([r["has_answer"] for r in records], K)
    sources = np.array([r["source"] for r in records])

    print("\n\n######## where does the oracle gain come from? (levels the tree lacks are padded like in the labels)")
    result["decomposition"] = {}
    for name in sorted(set(sources)) + ["ALL"]:
        sel = np.ones(len(records), dtype=bool) if name == "ALL" else sources == name
        result["decomposition"][name] = oracle_decomposition(acc[sel], avail[sel])
        print_decomposition(name, result["decomposition"][name])

    questions = [r["question"] for r in records]
    records_path = Path(args.out).with_name(Path(args.out).stem + "_records.jsonl")
    with open(records_path, "w", encoding="utf-8") as f:
        for r, a, v in zip(records, acc, avail):
            f.write(json.dumps({"id": r["id"], "source": r["source"], "question": r["question"], "acc": a.tolist(),
                                "answer_in_context": v.astype(int).tolist(), "num_levels": r["num_levels"]}, ensure_ascii=False) + "\n")
    print(f"\nper-question records: {records_path}")

    Path(args.out).write_text(json.dumps(result, indent=1))      # the tables so far survive a failure below
    if not args.no_learnability:
        print("\n\n######## can the question embedding tell which level to use?")
        X = encoder.encode_many(questions)
        differs = avail.max(1) != avail.min(1)
        result["auc"] = {}
        for name, y in (("answer is in the level-0 context", avail[:, 0] > 0), ("levels differ in answer availability", differs)):
            r = result["auc"][name] = availability_auc(X, y, args.folds, args.seed)
            if r["auc"] is None:
                print(f"  {name}: too few positives ({r['positives']}/{r['n']})")
            else:
                print(f"  predicting '{name}' ({r['positives']}/{r['n']} questions): AUC {r['auc']:.3f}   "
                      f"label-shuffled {r['shuffled_auc_mean']:.3f} +- {r['shuffled_auc_sd']:.3f}")
        best = result["decomposition"]["ALL"]
        print(f"\n  {args.folds}-fold CV, accuracy of the chosen level; best fixed level {best['best_fixed']:.4f}, "
              f"availability oracle {best['availability_oracle']:.4f}, oracle {best['oracle']:.4f}")
        result["routers"] = router_learnability(X, acc, avail, args.folds, args.seed, args.epochs)
        for r in result["routers"]:
            if "error" in r:
                print(f"  {r['setup']:<46} not trained: {r['error']}")
                continue
            print(f"  {r['setup']:<46} cv {r['cv']:.4f} +- {r['se']:.4f}  vs fixed {r['cv'] - best['best_fixed']:+.4f}  "
                  f"vs chance {r['cv'] - r['chance']:+.4f}  levels {'/'.join(f'{100 * d:.0f}' for d in r['level_distribution'])}%")
        print("  (chance = the score of a router without information that picks levels with the same distribution)")

    Path(args.out).write_text(json.dumps(result, indent=1))
    print(f"\nwritten: {args.out}")


if __name__ == "__main__":
    main()

"""Diagnostics and hyper-parameter search for the QA-GraphRAG router. It only reads the per-level labels written by
``gen_router_data.py`` (no LLM calls, no tree building).

1. **Diagnostics** (always printed first, ``--diagnose-only`` stops there): per data source the accuracy of every
   fixed level, the oracle, and how many questions can tell the levels apart at all. The oracle only gains on the
   questions whose levels disagree, and part of that gain is generation noise that no router can learn. A second
   table splits the same numbers by the number of summary layers of the question's tree (``max_level``): a tree with
   fewer layers than levels has copies of its top level, so those levels are equal by construction.
2. **Search**: every configuration is scored by K-fold cross-validation (mean accuracy obtained when following the
   router's choice on questions it was not trained on), with identical folds for all configurations. Trial order:
   the default configuration of ``train_router.py``; then the default hyper-parameters under every other
   objective (``--losses`` x ``--skip-ties``); then random grid points. The table shows what each change gains
   over the default, and the level distribution flags routers that collapsed onto one level.

    # Generalist
    python scripts/tune_router.py --data data/router/hotpotqa.jsonl data/router/nq.jsonl data/router/triviaqa.jsonl \
        --trials 60 --out outputs/router_tuning/generalist.json
    python scripts/tune_router.py --data ... --diagnose-only

3. **Learning curve** (``--learning-curve``): for the default configuration and the best configuration of each loss,
   the CV score when every fold is trained on 25% / 50% / 75% / 100% of its training questions (nested subsets;
   the test folds never change, so the scores are paired fold by fold). It tells whether labelling more questions
   is worth the GPU time: still rising, or flat. With 5 folds the verdict is a rule of thumb, not a test.

Objectives: ``gumbel`` is the paper's loss; ``mse`` regresses the per-level scores (centred per question);
``skip-ties 1`` trains only on questions whose levels do not all score the same.

Only tune on labels that are not part of a test set (the Generalist labels come from train / web data). Top configurations
often differ by less than the fold-to-fold noise (``se``); among those within one ``se`` of the best, prefer the
simplest. The printed flags are for ``train_router.py``.
"""
import argparse
import hashlib
import itertools
import json
import random
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np
import torch

from qa_graphrag.data import read_jsonl
from qa_graphrag.embedding import DEFAULT_ENCODER, SBertEncoder
from qa_graphrag.router import LOSSES, MLPRouter, cross_validate

DEFAULTS = dict(hidden=64, n_layers=3, dropout=0.5, lr=1e-2, weight_decay=5e-5, tau=1.0, batch_size=128)
SPACE = dict(
    hidden=[32, 64, 128, 256],
    n_layers=[2, 3, 4],
    dropout=[0.0, 0.2, 0.5, 0.7],
    lr=[3e-3, 1e-2, 3e-2],
    weight_decay=[0.0, 5e-5, 5e-4, 5e-3],
    tau=[0.5, 1.0, 2.0],
    batch_size=[64, 128, 256],
)
# fine-tuning (--init): architecture and dropout come from the checkpoint
FT_DEFAULTS = dict(lr=1e-3, weight_decay=5e-5, tau=1.0, batch_size=128, epochs=30)
FT_SPACE = dict(
    lr=[1e-4, 3e-4, 1e-3, 3e-3, 1e-2],
    weight_decay=[0.0, 5e-5, 5e-4],
    tau=[0.5, 1.0, 2.0],
    batch_size=[16, 32, 64, 128],
    epochs=[10, 30, 60],
)


def diagnose(P: np.ndarray, sources) -> list:
    """Per-source (and overall) statistics of the per-level scores ``P [N, K]``."""
    sources = np.asarray(sources)
    groups = [(s, sources == s) for s in sorted(set(sources))] + [("ALL", np.ones(len(P), dtype=bool))]
    out = []
    for name, m in groups:
        p = P[m]
        lo, hi = p.min(1), p.max(1)
        level_means = p.mean(0)
        out.append({
            "source": name, "n": int(m.sum()), "level_means": level_means.round(4).tolist(),
            "best_fixed_level": int(level_means.argmax()), "best_fixed": float(level_means.max()),
            "oracle": float(hi.mean()),
            "all_levels_equal": float((lo == hi).mean()),
            "all_levels_correct": float((lo == 1).mean()), "all_levels_wrong": float((hi == 0).mean()),
            "levels_disagree": float((hi > lo).mean()),
        })
    # what a router that only recognises the data source would reach (best fixed level per source, in-sample)
    per_source = sum(g["n"] * g["best_fixed"] for g in out[:-1]) / len(P) if len(out) > 2 else out[-1]["best_fixed"]
    out[-1]["source_aware_fixed"] = float(per_source)
    return out


def print_diagnosis(rows: list) -> None:
    K = len(rows[0]["level_means"])
    print(f"\n{'source':<11}{'n':>6}  " + "".join(f"{'lvl' + str(k):>7}" for k in range(K))
          + f"{'best':>8}{'oracle':>8}{'equal':>8}{'all-ok':>8}{'all-bad':>8}{'differ':>8}")
    for r in rows:
        print(f"{r['source']:<11}{r['n']:>6}  " + "".join(f"{v:>7.3f}" for v in r["level_means"])
              + f"{r['best_fixed']:>8.3f}{r['oracle']:>8.3f}{r['all_levels_equal']:>8.1%}"
              + f"{r['all_levels_correct']:>8.1%}{r['all_levels_wrong']:>8.1%}{r['levels_disagree']:>8.1%}")
    a = rows[-1]
    print(f"\noracle - best fixed level = {a['oracle'] - a['best_fixed']:.3f}; only the {a['levels_disagree']:.1%} of "
          f"questions whose levels disagree can contribute to it, and some of that is generation noise.")
    if "source_aware_fixed" in a:
        print(f"best fixed level per source = {a['source_aware_fixed']:.3f} (what recognising the source alone gives)")


def diagnose_depth(P: np.ndarray, sources, max_levels) -> dict:
    """Break the labels down by the number of summary layers of the question's tree (``max_level``).

    ``gen_router_data.py`` pads a tree that has fewer layers than there are levels by repeating its top level, so a
    tree with ``max_level = m`` really offers ``m + 1`` different levels: ``m = 0`` forces all levels to be equal, and
    ``m = 1`` forces levels 1 and 2 to be equal. Those ties come from the tree's shape, not from the question, and the
    shape is known when the router runs. ``padding_violations`` counts questions where a padded level is NOT a copy of
    the top real level (0 means the labels follow that rule).
    """
    sources, max_levels = np.asarray(sources), np.asarray(max_levels)
    K = P.shape[1]
    rows = []
    for name, m in [(s, sources == s) for s in sorted(set(sources))] + [("ALL", np.ones(len(P), dtype=bool))]:
        for depth in sorted(set(max_levels[m])):
            sel = m & (max_levels == depth)
            p = P[sel]
            rows.append({
                "source": name, "max_level": int(depth), "n": int(sel.sum()), "share": float(sel.sum() / m.sum()),
                "level_means": p.mean(0).round(4).tolist(), "oracle": float(p.max(1).mean()),
                "all_levels_equal": float((p.max(1) == p.min(1)).mean()),
                "levels_disagree": float((p.max(1) > p.min(1)).mean()),
            })
    violations = int(sum((P[i, int(d) + 1:] != P[i, int(d)]).any() for i, d in enumerate(max_levels) if d < K - 1))
    return {"rows": rows, "padding_violations": violations}


def print_depth_diagnosis(depth: dict) -> None:
    rows = depth["rows"]
    K = len(rows[0]["level_means"])
    print(f"\nby tree depth (max_level = number of summary layers; levels above it are copies of the top one)\n"
          f"{'source':<11}{'max_level':>10}{'n':>6}{'share':>8}  " + "".join(f"{'lvl' + str(k):>7}" for k in range(K))
          + f"{'oracle':>8}{'equal':>8}{'differ':>8}")
    for r in rows:
        print(f"{r['source']:<11}{r['max_level']:>10}{r['n']:>6}{r['share']:>8.1%}  "
              + "".join(f"{v:>7.3f}" for v in r["level_means"])
              + f"{r['oracle']:>8.3f}{r['all_levels_equal']:>8.1%}{r['levels_disagree']:>8.1%}")
    allr = [r for r in rows if r["source"] == "ALL"]
    forced = sum(r["n"] for r in allr if r["max_level"] == 0)
    partial = sum(r["n"] for r in allr if 0 < r["max_level"] < K - 1)
    n = sum(r["n"] for r in allr)
    print(f"\n{forced / n:.1%} of the questions have no summary layer (all levels equal by construction) and "
          f"{partial / n:.1%} have fewer layers than levels (the top levels are copies).")
    if depth["padding_violations"]:
        print(f"WARNING: {depth['padding_violations']} questions whose padded levels differ from the top real level: "
              f"the labels were not made by the current gen_router_data.py")


def normalise(cfg: dict) -> dict:
    return {**cfg, "tau": 1.0} if cfg["loss"] == "mse" else cfg   # tau only exists in the Gumbel-Softmax loss


def make_trials(defaults: dict, space: dict, labels, losses, ties, n: int, seed: int):
    """Default configuration, then the default hyper-parameters under every other objective, then random grid points."""
    space = {**space, "label": list(labels), "loss": list(losses), "skip_ties": list(ties)}
    first = {**defaults, "label": "acc" if "acc" in labels else labels[0],
             "loss": "gumbel" if "gumbel" in losses else losses[0], "skip_ties": 0 if 0 in ties else ties[0]}
    trials = [first]
    for loss, skip in itertools.product(losses, ties):
        cfg = normalise({**first, "loss": loss, "skip_ties": skip})
        if cfg not in trials:
            trials.append(cfg)
    rest = []
    for v in itertools.product(*space.values()):
        cfg = normalise(dict(zip(space, v)))
        if cfg not in trials and cfg not in rest:
            rest.append(cfg)
    random.Random(seed).shuffle(rest)
    return (trials + rest)[: max(n, 1)]


def paired(a, b):
    """Mean and standard error of the fold-by-fold differences ``a - b``."""
    d = np.asarray(a, dtype=float) - np.asarray(b, dtype=float)
    return float(d.mean()), float(d.std(ddof=1) / np.sqrt(len(d)))


def curve_verdict(folds_by_fraction: dict, baseline: float) -> str:
    """One-line reading of a learning curve ``{fraction: [score per fold]}``.

    The step looked at is a doubling of the data (the fraction closest to half of the largest one -> the largest):
    a 25% step is too small to separate from noise. "rising" when it gains more than 2 paired standard errors (and
    at least 0.001), otherwise "flat". ``baseline`` is the accuracy of the best fixed level.
    """
    fr = sorted(folds_by_fraction)
    last = fr[-1]
    prev = min(fr[:-1], key=lambda f: abs(f - last / 2))
    d, se = paired(folds_by_fraction[last], folds_by_fraction[prev])
    top = np.asarray(folds_by_fraction[last], dtype=float)
    top_se = float(top.std(ddof=1) / np.sqrt(len(top)))
    step = f"{prev:.0%} -> {last:.0%} of the training questions: {d:+.4f} +- {se:.4f}"
    if d > 2 * se and d > 0.001:
        verdict = f"still rising ({step}): more labelled questions are likely to help"
    else:
        verdict = f"flat ({step}): more questions of the same kind are unlikely to help"
    gap = float(top.mean()) - baseline
    return verdict + (f"; with all of them the router is {gap:+.4f} vs the best fixed level"
                      + (" (within one se of it)" if abs(gap) <= top_se else ""))


def pick_curve_configs(results: list) -> list:
    """The default trial plus the best trial of every loss (deduplicated)."""
    picks = [results[0]]
    for loss in sorted({r["config"]["loss"] for r in results}):
        best = max((r for r in results if r["config"]["loss"] == loss), key=lambda r: r["cv_score"])
        if all(best["config"] != p["config"] for p in picks):
            picks.append(best)
    return picks


def encode_questions(questions, encoder_name, device, cache_dir: Path) -> np.ndarray:
    key = hashlib.md5((encoder_name + "\n" + "\n".join(questions)).encode()).hexdigest()[:16]
    path = cache_dir / f"emb_{key}.npy"
    if path.exists():
        return np.load(path)
    X = SBertEncoder(encoder_name, device=device).encode_many(questions)
    cache_dir.mkdir(parents=True, exist_ok=True)
    np.save(path, X)
    return X


def learning_curves(args, results, default_cfg, run_cv, P_acc, n_questions) -> list:
    """CV the default and the best config of each loss on growing parts of every fold's training questions.

    The 100% point is the search result itself (identical folds and seed), so only the smaller fractions are run.
    The test folds are always the natural distribution; "train q" and "with disagreement" are approximate.
    """
    baseline = float(P_acc.mean(0).max())
    informative = float((P_acc.max(1) > P_acc.min(1)).mean())
    n_train = n_questions * (args.folds - 1) / args.folds
    print(f"\nlearning curve: best fixed level {baseline:.4f}; {informative:.1%} of the questions have levels that disagree")
    fractions = sorted({f for f in args.curve_fractions if 0 < f < 1} | {1.0})
    curves = []
    for r in pick_curve_configs(results):
        by_fraction = {1.0: r["folds"]}
        for f in fractions[:-1]:
            by_fraction[f] = run_cv(r["config"], train_fraction=f)
        print(f"\n  {short(r['config'], default_cfg)}")
        print(f"  {'fraction':>9}{'train q':>9}{'w/ disagreement':>17}{'cv':>10}{'se':>8}{'paired gain vs previous':>26}")
        prev = None
        for f in fractions:
            sc = by_fraction[f]
            gain = "" if prev is None else "{:+.4f} +- {:.4f}".format(*paired(sc, by_fraction[prev]))
            print(f"  {f:>9.0%}{f * n_train:>9.0f}{f * n_train * informative:>17.0f}{np.mean(sc):>10.4f}"
                  f"{np.std(sc, ddof=1) / np.sqrt(len(sc)):>8.4f}{gain:>26}")
            prev = f
        verdict = curve_verdict(by_fraction, baseline)
        print(f"  -> {verdict}", flush=True)
        curves.append({"config": r["config"], "folds": {str(f): v for f, v in by_fraction.items()}, "verdict": verdict})
    return curves


def short(cfg: dict, base: dict) -> str:
    """The settings of ``cfg`` that differ from the default trial."""
    d = {k: v for k, v in cfg.items() if base.get(k) != v}
    return json.dumps(d) if d else "(default)"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", nargs="+", required=True)
    ap.add_argument("--init", default=None, help="router checkpoint: tune its fine-tuning instead")
    ap.add_argument("--labels", nargs="+", default=["acc"], choices=["acc", "recall"],
                    help="training labels to try (the score is always accuracy)")
    ap.add_argument("--losses", nargs="+", default=list(LOSSES), choices=LOSSES)
    ap.add_argument("--skip-ties", nargs="+", type=int, default=[0, 1], choices=[0, 1],
                    help="1 = train only on questions whose levels do not all score the same")
    ap.add_argument("--diagnose-only", action="store_true")
    ap.add_argument("--learning-curve", action="store_true",
                    help="after the search, CV the default and the best config of each loss on growing parts of the data")
    ap.add_argument("--curve-fractions", nargs="+", type=float, default=[0.25, 0.5, 0.75],
                    help="training fractions of the learning curve (100%% comes from the search itself)")
    ap.add_argument("--trials", type=int, default=40)
    ap.add_argument("--folds", type=int, default=5)
    ap.add_argument("--epochs", type=int, default=100, help="max epochs of the Generalist search (early stopping applies)")
    ap.add_argument("--val-fraction", type=float, default=0.1, help="inner split train_router uses to pick the epoch")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--encoder", default=DEFAULT_ENCODER)
    ap.add_argument("--device", default=None)
    ap.add_argument("--top", type=int, default=8)
    ap.add_argument("--out", default="outputs/router_tuning/tuning.json")
    args = ap.parse_args()

    rows = [r for p in args.data for r in read_jsonl(p)]
    out = Path(args.out)
    P = {lab: np.array([r[lab] for r in rows], dtype=np.float32) for lab in ("acc", "recall")}
    diagnosis = diagnose(P["acc"], [r.get("source", "all") for r in rows])
    print_diagnosis(diagnosis)
    depth = None
    if all("max_level" in r for r in rows):
        depth = diagnose_depth(P["acc"], [r.get("source", "all") for r in rows], [r["max_level"] for r in rows])
        print_depth_diagnosis(depth)
    else:
        print("\n(no tree-depth breakdown: some label rows have no max_level)")
    diagnosis = {"by_source": diagnosis, "by_depth": depth}
    if args.diagnose_only:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps({"diagnosis": diagnosis}, indent=1))
        return

    X = encode_questions([r["question"] for r in rows], args.encoder, args.device, out.parent)
    K = P["acc"].shape[1]
    print(f"\n{len(rows)} questions, {args.folds}-fold CV")

    init_state, fixed = None, {}
    if args.init:
        base = MLPRouter.load(args.init)
        if base.meta.get("encoder") not in (None, args.encoder):
            raise ValueError(f"checkpoint was trained with encoder {base.meta['encoder']}")
        init_state = base.state_dict()
        fixed = dict(hidden=base.config.hidden, n_layers=base.config.n_layers, dropout=base.config.dropout)
        trials = make_trials(FT_DEFAULTS, FT_SPACE, args.labels, args.losses, args.skip_ties, args.trials, args.seed)
    else:
        trials = make_trials({**DEFAULTS, "epochs": args.epochs}, {**SPACE, "epochs": [args.epochs]}, args.labels,
                             args.losses, args.skip_ties, args.trials, args.seed)
    print(f"{len(trials)} configurations" + (f" (fine-tuning {args.init}, fixed: {fixed})" if args.init else ""))

    def run_cv(cfg, **extra):
        kw = {**fixed, **{k: v for k, v in cfg.items() if k not in ("label", "skip_ties")}, "skip_ties": bool(cfg["skip_ties"])}
        return cross_validate(X, P[cfg["label"]], P["acc"], n_folds=args.folds, seed=args.seed,
                              val_fraction=args.val_fraction, init_state=init_state, **extra, **kw)

    results = []
    for i, cfg in enumerate(trials):
        t0 = time.time()
        scores, choices = run_cv(cfg, return_choices=True)
        mean, se = float(np.mean(scores)), float(np.std(scores, ddof=1) / np.sqrt(len(scores)))
        dist = np.bincount(choices, minlength=K) / len(choices)
        results.append({"trial": i, "config": {**fixed, **cfg}, "cv_score": mean, "se": se, "folds": scores,
                        "level_distribution": dist.round(4).tolist()})
        best = max(r["cv_score"] for r in results)
        print(f"[{i + 1}/{len(trials)}] cv {mean:.4f} +- {se:.4f}  levels {'/'.join(f'{100 * d:.0f}' for d in dist)}%  "
              f"(best {best:.4f}, {time.time() - t0:.0f}s)  {short(cfg, trials[0])}", flush=True)
        out.parent.mkdir(parents=True, exist_ok=True)   # rewritten after every trial: Ctrl-C keeps the results so far
        out.write_text(json.dumps({"args": vars(args), "diagnosis": diagnosis, "default_trial": results[0],
                                   "ranked": sorted(results, key=lambda r: -r["cv_score"])}, indent=1))

    ranked = sorted(results, key=lambda r: -r["cv_score"])
    if args.learning_curve:
        curves = learning_curves(args, results, trials[0], run_cv, P["acc"], len(X))
        out.write_text(json.dumps({"args": vars(args), "diagnosis": diagnosis, "default_trial": results[0],
                                   "ranked": ranked, "learning_curve": curves}, indent=1))

    print(f"\ndefault configuration: cv {results[0]['cv_score']:.4f} +- {results[0]['se']:.4f}")
    print(f"top {min(args.top, len(ranked))} of {len(ranked)}:")
    for r in ranked[: args.top]:
        print(f"  cv {r['cv_score']:.4f} +- {r['se']:.4f}  levels {'/'.join(f'{100 * d:.0f}' for d in r['level_distribution'])}%  {r['config']}")
    c = ranked[0]["config"]
    flags = (f"--lr {c['lr']} --weight-decay {c['weight_decay']} --tau {c['tau']} --batch-size {c['batch_size']} "
             f"--epochs {c['epochs']} --label {c['label']} --loss {c['loss']}" + (" --skip-ties" if c["skip_ties"] else ""))
    flags += f" --init {args.init}" if args.init else f" --hidden {c['hidden']} --n-layers {c['n_layers']} --dropout {c['dropout']}"
    print(f"\nbest -> train_router.py flags:\n  {flags}\nall results: {out}")


if __name__ == "__main__":
    main()

"""Count how many cached RAPTOR trees contain nodes with identical embeddings.

Before the clustering fix, cluster members were looked up by embedding value: ``k`` nodes sharing one embedding were
each added ``k`` times to every cluster they belong to, so the summary prompt held the same text ``k*k`` times instead
of ``k``. A tree is *affected* if one of its clustered layers (every layer except the top one) has such a group. Trees
without one are identical before and after the fix (up to UMAP/GMM randomness). Level 0 (the chunks) never changes.

    python scripts/count_duplicate_embeddings.py --cache-dir indexes
    python scripts/count_duplicate_embeddings.py --cache-dir indexes --namespaces nq triviaqa --list-out affected.txt

Trees are read from ``<cache-dir>/<namespace>/*.pkl`` (one namespace per dataset). The files are named by a hash of the question id, so this reports counts and file paths, not question ids.
It does not tell how much the summaries (and so the labels) changed, only whether they could have.
"""
import argparse
import json
import pickle
import sys
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from tqdm import tqdm

from qa_graphrag.index import duplicate_embedding_stats

BUCKETS = [("2", 2, 2), ("3-5", 3, 5), ("6-20", 6, 20), (">20", 21, 10 ** 9)]


def scan(path: str) -> dict:
    try:
        with open(path, "rb") as f:
            tree = pickle.load(f)
        s = duplicate_embedding_stats(tree)
    except Exception as e:   # truncated / foreign pickles are reported, not fatal
        return {"path": path, "error": f"{type(e).__name__}: {e}"}
    leaves = s["layers"][0]
    return {"path": path, "affected": s["affected"], "max_group": s["max_group"], "num_layers": tree.num_layers,
            "leaves": leaves["nodes"], "dup_leaves": leaves["dup_nodes"],
            "dup_layers": [l["layer"] for l in s["layers"][:-1] if l["dup_groups"]]}


def pct(a, b):
    return f"{100 * a / b:.1f}%" if b else "-"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--cache-dir", default="indexes")
    ap.add_argument("--namespaces", nargs="*", default=None, help="default: every sub-directory of --cache-dir")
    ap.add_argument("--workers", type=int, default=8)
    ap.add_argument("--list-out", default=None, help="write the paths of the affected trees here")
    ap.add_argument("--json-out", default=None, help="write the per-namespace summary here")
    args = ap.parse_args()

    root = Path(args.cache_dir)
    namespaces = args.namespaces or sorted(p.name for p in root.iterdir() if p.is_dir())
    files = {ns: sorted(str(p) for p in (root / ns).glob("*.pkl")) for ns in namespaces}
    allp = [p for ps in files.values() for p in ps]
    if not allp:
        sys.exit(f"no trees under {root}/{{{','.join(namespaces)}}}/*.pkl")
    with ProcessPoolExecutor(args.workers) as ex:
        results = dict(zip(allp, tqdm(ex.map(scan, allp, chunksize=8), total=len(allp), mininterval=10)))

    summary, affected_paths = {}, []
    print(f"{'namespace':<18}{'trees':>7}{'affected':>10}{'':>8}{'leaves in dup groups':>22}   largest group (trees: " +
          " / ".join(b[0] for b in BUCKETS) + ")")
    for ns, ps in files.items():
        rs = [results[p] for p in ps]
        ok = [r for r in rs if "error" not in r]
        bad = [r for r in ok if r["affected"]]
        sizes = Counter(next(n for n, lo, hi in BUCKETS if lo <= r["max_group"] <= hi) for r in bad)
        leaves, dup = sum(r["leaves"] for r in ok), sum(r["dup_leaves"] for r in ok)
        summary[ns] = {"trees": len(ok), "unreadable": len(rs) - len(ok), "affected": len(bad), "leaves": leaves,
                       "leaves_in_dup_groups": dup, "max_group_buckets": {n: sizes.get(n, 0) for n, _, _ in BUCKETS},
                       "affected_in_layers": dict(Counter(l for r in bad for l in r["dup_layers"]))}
        affected_paths += [r["path"] for r in bad]
        print(f"{ns:<18}{len(ok):>7}{len(bad):>10}{pct(len(bad), len(ok)):>8}{pct(dup, leaves):>22}   "
              + " / ".join(str(sizes.get(n, 0)) for n, _, _ in BUCKETS)
              + (f"   [{len(rs) - len(ok)} unreadable]" if len(rs) != len(ok) else ""))
    if args.list_out:
        Path(args.list_out).write_text("\n".join(affected_paths) + ("\n" if affected_paths else ""))
        print(f"affected trees: {len(affected_paths)} -> {args.list_out}")
    if args.json_out:
        Path(args.json_out).write_text(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()

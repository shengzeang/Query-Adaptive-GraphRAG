"""Train / fine-tune the QA-GraphRAG router from ``gen_router_data.py`` output.

    # Generalist: HotpotQA + NQ + TriviaQA (6000 questions)
    python scripts/train_router.py --data data/router/hotpotqa.jsonl data/router/nq.jsonl \
        data/router/triviaqa.jsonl --out checkpoints/generalist.pt
"""
import argparse
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import numpy as np
import torch

from qa_graphrag.data import read_jsonl
from qa_graphrag.embedding import DEFAULT_ENCODER, SBertEncoder
from qa_graphrag.router import LOSSES, MLPRouter, reference_scores, train_router


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", nargs="+", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--init", default=None, help="router checkpoint to fine-tune")
    ap.add_argument("--label", default="acc", choices=["acc", "recall"], help="per-level score used as P")
    ap.add_argument("--encoder", default=DEFAULT_ENCODER)
    ap.add_argument("--device", default=os.environ.get("ENCODER_DEVICE") or None,
                    help="device of the sentence encoder that embeds the questions (default: $ENCODER_DEVICE, else cuda if "
                         "available). cpu is fine: it is a few thousand short questions, once. The router trains on the CPU")
    ap.add_argument("--hidden", type=int, default=64)
    ap.add_argument("--n-layers", type=int, default=3)
    ap.add_argument("--dropout", type=float, default=0.5)
    ap.add_argument("--lr", type=float, default=1e-2)
    ap.add_argument("--weight-decay", type=float, default=5e-5)
    ap.add_argument("--epochs", type=int, default=100)
    ap.add_argument("--batch-size", type=int, default=128)
    ap.add_argument("--val-fraction", type=float, default=0.1)
    ap.add_argument("--tau", type=float, default=1.0)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--loss", default="gumbel", choices=LOSSES, help="gumbel: paper Eq. (2); mse: per-level regression")
    ap.add_argument("--skip-ties", action="store_true",
                    help="train only on questions whose levels do not all score the same")
    args = ap.parse_args()

    rows = [r for p in args.data for r in read_jsonl(p)]
    modes = {r.get("retrieval", "traverse") for r in rows}      # how the labels' start levels retrieved (rows without it: traverse)
    if len(modes) != 1:
        raise ValueError(f"the data mixes labels made with different retrieval modes {sorted(modes)}: a level means something "
                         f"else in each, train on one")
    retrieval = modes.pop()
    top_ks = {r.get("top_k", 5) for r in rows}                  # rows made before it was recorded: 5
    if len(top_ks) != 1:
        raise ValueError(f"the data mixes labels made with different top-k {sorted(top_ks)}: train on one")
    top_k = top_ks.pop()
    X = SBertEncoder(args.encoder, device=args.device).encode_many([r["question"] for r in rows])
    P = np.array([r[args.label] for r in rows], dtype=np.float32)
    print(f"{len(rows)} training questions (labels made with retrieval '{retrieval}', top-k {top_k}); score per level: {reference_scores(torch.tensor(P))}")

    init_state = None
    hidden, n_layers, dropout = args.hidden, args.n_layers, args.dropout
    if args.init:
        base = MLPRouter.load(args.init)
        if base.meta.get("encoder") not in (None, args.encoder):
            raise ValueError(f"checkpoint was trained with encoder {base.meta['encoder']}")
        if base.retrieval != retrieval:
            raise ValueError(f"--init was trained on labels of retrieval '{base.retrieval}', the data holds '{retrieval}'")
        if base.top_k != top_k:
            raise ValueError(f"--init was trained on labels of top-k {base.top_k}, the data holds top-k {top_k}")
        init_state = base.state_dict()
        hidden, n_layers, dropout = base.config.hidden, base.config.n_layers, base.config.dropout

    router, report = train_router(
        X, P, hidden=hidden, n_layers=n_layers, dropout=dropout, lr=args.lr, weight_decay=args.weight_decay,
        epochs=args.epochs, batch_size=args.batch_size, val_fraction=args.val_fraction, tau=args.tau,
        seed=args.seed, init_state=init_state, loss=args.loss, skip_ties=args.skip_ties,
    )
    meta = {"encoder": args.encoder, "data": args.data, "retrieval": retrieval, "top_k": top_k, "label": args.label, "loss": args.loss, "skip_ties": args.skip_ties, "n": len(rows), "init": args.init,
            "heldout_router_score": report["heldout_router_score"], "heldout_reference": report["heldout_reference"]}
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    router.save(args.out, meta)
    Path(args.out).with_suffix(".json").write_text(json.dumps({**meta, "history": report["history"]}, indent=1))
    print(json.dumps({k: report[k] for k in ("best_epoch", "heldout_router_score", "heldout_reference", "n_train", "n_ties_dropped", "n_heldout")}, indent=1))


if __name__ == "__main__":
    main()

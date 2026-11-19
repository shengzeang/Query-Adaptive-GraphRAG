"""The QA-GraphRAG router (paper Sec. 5.2): a 3-layer MLP that maps a query embedding to a
preference score over the K retrieval start levels.

Training uses Gumbel-Softmax to relax the hard level selection, with the loss
``1 - sum(P * Q~)`` (Eq. 2), where ``P`` holds the accuracy obtained when retrieval starts at each
level. At inference the router is deterministic: ``argmax`` of the logits.
"""
from dataclasses import asdict, dataclass
from typing import Dict, List, Optional, Sequence, Tuple

import numpy as np
import torch
import torch.nn.functional as F
from torch import nn


@dataclass
class RouterConfig:
    in_dim: int
    num_levels: int
    hidden: int = 64
    n_layers: int = 3
    dropout: float = 0.5


class MLPRouter(nn.Module):
    def __init__(self, config: RouterConfig):
        super().__init__()
        self.config = config
        dims = [config.in_dim] + [config.hidden] * (config.n_layers - 1) + [config.num_levels]
        self.linears = nn.ModuleList(nn.Linear(a, b) for a, b in zip(dims[:-1], dims[1:]))
        self.act = nn.PReLU()
        self.dropout = nn.Dropout(config.dropout)
        gain = nn.init.calculate_gain("relu")
        for layer in self.linears:
            nn.init.xavier_uniform_(layer.weight, gain=gain)
            nn.init.zeros_(layer.bias)

    def logits(self, x: torch.Tensor) -> torch.Tensor:
        for i, layer in enumerate(self.linears):
            x = layer(x)
            if i < len(self.linears) - 1:
                x = self.dropout(self.act(x))
        return x

    def forward(self, x: torch.Tensor, tau: float = 1.0) -> torch.Tensor:
        """Training-time output Q~: Gumbel-Softmax sample over the levels."""
        return F.gumbel_softmax(self.logits(x), tau=tau, hard=False, dim=-1)

    @torch.no_grad()
    def predict(self, x) -> Tuple[np.ndarray, np.ndarray]:
        """Deterministic inference. Returns ``(levels [N], preference scores [N, K])``."""
        was_training = self.training
        self.eval()
        x = torch.as_tensor(np.asarray(x), dtype=torch.float32, device=next(self.parameters()).device)
        if x.dim() == 1:
            x = x.unsqueeze(0)
        pref = F.softmax(self.logits(x), dim=-1)
        self.train(was_training)
        return pref.argmax(-1).cpu().numpy(), pref.cpu().numpy()

    def route(self, query_embedding) -> Tuple[int, np.ndarray]:
        levels, pref = self.predict(query_embedding)
        return int(levels[0]), pref[0]

    def save(self, path: str, meta: Optional[Dict] = None) -> None:
        torch.save({"config": asdict(self.config), "state_dict": self.state_dict(), "meta": meta or {}}, path)

    @property
    def retrieval(self) -> str:
        """The RAPTOR retrieval mode of the labels it was trained on (checkpoints made before it was recorded: traverse)."""
        return getattr(self, "meta", {}).get("retrieval", "traverse")

    @property
    def top_k(self) -> int:
        """The top-k of the labels it was trained on (checkpoints made before it was recorded: 5)."""
        return getattr(self, "meta", {}).get("top_k", 5)

    @classmethod
    def load(cls, path: str, device: str = "cpu") -> "MLPRouter":
        blob = torch.load(path, map_location=device)
        router = cls(RouterConfig(**blob["config"]))
        router.load_state_dict(blob["state_dict"])
        router.meta = blob.get("meta", {})
        return router.to(device).eval()


def router_loss(q_tilde: torch.Tensor, P: torch.Tensor) -> torch.Tensor:
    """Eq. (2): ``loss = 1 - (P * Q~)``, with the element-wise product summed over the levels."""
    return (1.0 - (P * q_tilde).sum(dim=-1)).mean()


def centered_mse_loss(logits: torch.Tensor, P: torch.Tensor) -> torch.Tensor:
    """Regression objective: the router's logits should reproduce how much better or worse each level is than the
    question's average level. Both sides are centred per question, because the argmax (the only thing inference uses)
    is invariant to an additive shift, and how easy a question is overall says nothing about the best level."""
    return ((logits - logits.mean(-1, keepdim=True)) - (P - P.mean(-1, keepdim=True))).pow(2).mean()


LOSSES = ("gumbel", "mse")


@torch.no_grad()
def expected_score(router: MLPRouter, X: torch.Tensor, P: torch.Tensor) -> float:
    """Mean accuracy obtained when following the router's (deterministic) choice."""
    levels, _ = router.predict(X)
    chosen = P[torch.arange(len(P)), torch.as_tensor(levels)]
    return float(chosen.mean())


def reference_scores(P: torch.Tensor) -> Dict[str, float]:
    out = {f"always_level_{k}": float(P[:, k].mean()) for k in range(P.shape[1])}
    out["oracle"] = float(P.max(dim=1).values.mean())
    return out


def train_router(
    X: np.ndarray,
    P: np.ndarray,
    hidden: int = 64,
    n_layers: int = 3,
    dropout: float = 0.5,
    lr: float = 1e-2,
    weight_decay: float = 5e-5,
    epochs: int = 100,
    batch_size: int = 128,
    val_fraction: float = 0.1,
    tau: float = 1.0,
    seed: int = 0,
    patience: int = 20,
    init_state: Optional[Dict] = None,
    loss: str = "gumbel",
    skip_ties: bool = False,
    log=print,
) -> Tuple[MLPRouter, Dict]:
    """Train a router on query embeddings ``X [N, d]`` and per-level scores ``P [N, K]``.

    The best epoch is chosen on a held-out split by the mean score of the router's argmax choice.

    ``loss``: ``"gumbel"`` is the paper's Eq. (2) with Gumbel-Softmax; ``"mse"`` regresses the per-level scores
    (see ``centered_mse_loss``). ``skip_ties`` leaves out of the *training* split the questions on which every level
    scores the same (all correct or all wrong): they carry no information about which level is best, but under a
    0/1 label they are most of the data. The held-out split keeps them (they add the same constant to every epoch).
    """
    if loss not in LOSSES:
        raise ValueError(f"loss must be one of {LOSSES}, got {loss!r}")
    g = torch.Generator().manual_seed(seed)
    torch.manual_seed(seed)
    X_t, P_t = torch.as_tensor(X, dtype=torch.float32), torch.as_tensor(P, dtype=torch.float32)
    n = len(X_t)
    perm = torch.randperm(n, generator=g)
    n_val = int(round(n * val_fraction)) if val_fraction > 0 else 0
    val_idx, train_idx = perm[:n_val], perm[n_val:]
    n_ties = 0
    if skip_ties:
        informative = P_t[train_idx].max(-1).values > P_t[train_idx].min(-1).values
        n_ties = int((~informative).sum())
        train_idx = train_idx[informative]
        if len(train_idx) == 0:
            raise ValueError("skip_ties: every training question scores the same at all levels")

    router = MLPRouter(RouterConfig(X_t.shape[1], P_t.shape[1], hidden, n_layers, dropout))
    if init_state is not None:
        router.load_state_dict(init_state)
    optimizer = torch.optim.Adam(router.parameters(), lr=lr, weight_decay=weight_decay)

    best = {"score": -1.0, "state": None, "epoch": -1}
    history = []
    stale = 0
    for epoch in range(1, epochs + 1):
        router.train()
        order = train_idx[torch.randperm(len(train_idx), generator=g)]
        total = 0.0
        for start in range(0, len(order), batch_size):
            idx = order[start : start + batch_size]
            if loss == "gumbel":
                batch_loss = router_loss(router(X_t[idx], tau=tau), P_t[idx])
            else:
                batch_loss = centered_mse_loss(router.logits(X_t[idx]), P_t[idx])
            optimizer.zero_grad()
            batch_loss.backward()
            optimizer.step()
            total += batch_loss.item() * len(idx)
        eval_idx = val_idx if n_val > 0 else train_idx
        score = expected_score(router, X_t[eval_idx], P_t[eval_idx])
        history.append({"epoch": epoch, "train_loss": total / max(len(order), 1), "val_score": score})
        if epoch == 1 or epoch % 10 == 0:
            log(f"epoch {epoch:3d}  loss {history[-1]['train_loss']:.4f}  held-out score {score:.4f}")
        if score > best["score"]:
            best = {"score": score, "state": {k: v.clone() for k, v in router.state_dict().items()}, "epoch": epoch}
            stale = 0
        else:
            stale += 1
            if stale >= patience:
                break
    router.load_state_dict(best["state"])
    router.eval()
    report = {
        "best_epoch": best["epoch"],
        "heldout_router_score": best["score"],
        "heldout_reference": reference_scores(P_t[val_idx if n_val > 0 else train_idx]),
        "n_train": int(len(train_idx)),
        "n_ties_dropped": n_ties,
        "n_heldout": int(n_val),
        "history": history,
    }
    return router, report


def cross_validate(
    X: np.ndarray,
    P_train: np.ndarray,
    P_eval: Optional[np.ndarray] = None,
    n_folds: int = 5,
    seed: int = 0,
    return_choices: bool = False,
    train_fraction: float = 1.0,
    **train_kwargs,
):
    """K-fold score of a router configuration.

    ``train_router`` picks its best epoch on an internal held-out split, so its own ``heldout_router_score`` is
    optimistic. Here every fold is scored on questions the training run never saw (neither for gradient steps nor
    for epoch selection). ``P_eval`` (default ``P_train``) lets the router be trained on one label (e.g. recall)
    and scored on another (accuracy). Folds depend only on ``seed``, so different configurations are compared on
    identical splits.

    With ``return_choices`` the result is ``(scores, levels)`` where ``levels[i]`` is the level the router (not
    trained on question ``i``) picked for it, e.g. to notice a router that collapsed onto a single level.

    ``train_fraction < 1`` trains each fold on that fraction of its training questions (for learning curves). The
    subsets are nested (a larger fraction contains the smaller ones) and the test folds do not change, so the scores
    of different fractions are paired fold by fold. ``1.0`` gives exactly the same result as not passing it.
    """
    if not 0 < train_fraction <= 1:
        raise ValueError(f"train_fraction must be in (0, 1], got {train_fraction}")
    P_eval = P_train if P_eval is None else P_eval
    folds = np.array_split(np.random.RandomState(seed).permutation(len(X)), n_folds)
    scores, choices = [], np.zeros(len(X), dtype=int)
    for k, test_idx in enumerate(folds):
        train_idx = np.concatenate([f for j, f in enumerate(folds) if j != k])
        if train_fraction < 1:
            order = np.random.RandomState(seed * 1000 + k).permutation(train_idx)
            train_idx = order[: max(int(round(train_fraction * len(order))), 10)]
        router, _ = train_router(X[train_idx], P_train[train_idx], seed=seed, log=lambda *_: None, **train_kwargs)
        scores.append(expected_score(router, torch.as_tensor(X[test_idx], dtype=torch.float32),
                                     torch.as_tensor(P_eval[test_idx], dtype=torch.float32)))
        choices[test_idx] = router.predict(X[test_idx])[0]
    return (scores, choices) if return_choices else scores

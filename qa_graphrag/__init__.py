"""QA-GraphRAG: query-adaptive retrieval-level routing on top of RAPTOR.

Level convention used everywhere in this package: level 0 = raw text chunks (the leaves of the
RAPTOR tree); level ``k`` = start retrieval at tree layer ``k`` and descend to the leaves, i.e. the
context contains knowledge from layers ``k, k-1, ..., 0``. A tree with ``L`` summary layers has
levels ``0..L``; a requested level above ``L`` is clamped to ``L``.
"""
import os as _os
from pathlib import Path as _Path

# tiktoken downloads its vocabulary on first use. If the repository still ships the archived
# cache (legacy/artifacts/data-gym-cache) use it, so the code also works on offline machines.
_legacy_cache = _Path(__file__).resolve().parent.parent / "legacy" / "artifacts" / "data-gym-cache"
if "TIKTOKEN_CACHE_DIR" not in _os.environ and "DATA_GYM_CACHE_DIR" not in _os.environ and _legacy_cache.is_dir():
    _os.environ["TIKTOKEN_CACHE_DIR"] = str(_legacy_cache)

NUM_TREE_LAYERS = 2   # summary layers above the leaves (paper: three knowledge levels 0/1/2)
NUM_LEVELS = NUM_TREE_LAYERS + 1
EMB_KEY = "EMB"       # key of the embedding inside ``Node.embeddings``
SEGMENTS_KEY = EMB_KEY + "_segments"   # per-window embeddings of a text longer than the encoder reads (raptor.utils.SEGMENTS_SUFFIX)
CLUSTER_TOKENS = 3500  # RAPTOR's cap on the text of one cluster = the input of one summary (upstream default)

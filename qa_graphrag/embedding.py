"""Sentence embedding used for RAPTOR nodes, retrieval and as the router input."""
import math
import threading
from typing import List, Optional, Sequence, Tuple

import numpy as np

from raptor import BaseEmbeddingModel

DEFAULT_ENCODER = "sentence-transformers/all-MiniLM-L6-v2"  # the encoder named in the paper (Sec. 3.2)


def split_windows(text: str, n_pieces: int, limit: int) -> List[str]:
    """Cut a text of ``n_pieces`` word pieces into the fewest equally long word windows that fit ``limit`` pieces each
    (10% slack, since the pieces are not spread evenly over the words). A text that fits is returned as it is."""
    if n_pieces <= limit:
        return [text]
    words = text.split()
    k = min(len(words), math.ceil(n_pieces * 1.1 / limit))
    if k <= 1:
        return [text]
    size = math.ceil(len(words) / k)
    return [" ".join(words[i:i + size]) for i in range(0, len(words), size)]


class SBertEncoder(BaseEmbeddingModel):
    """Sentence-BERT encoder. The model reads at most ``max_seq_length`` word pieces (256 for all-MiniLM-L6-v2) and silently
    ignores the rest of a longer text, so a 1200-token chunk would be embedded by its first fifth only.

    With ``segment_long_texts`` (default) such a text is cut into windows that fit and every window is embedded
    (``segment_embeddings``). The tree stores all of them on the node and the retriever compares the query with every
    window and takes the best (``raptor.utils.distances_to_nearest_segment``). ``create_embedding`` / ``encode_many``
    return ONE vector per text, the normalised mean of its windows: it is only used where a single point per node is
    needed (clustering). Texts that fit are embedded exactly as before, so questions, summaries and short chunks are
    not affected."""

    def __init__(self, model_name: str = DEFAULT_ENCODER, device: str = None, cache_size: int = 20000,
                 segment_long_texts: bool = True):
        from sentence_transformers import SentenceTransformer

        self.model_name = model_name
        self.model = SentenceTransformer(model_name, device=device)
        self.dim = self.model.get_sentence_embedding_dimension()
        self.segment_long_texts = segment_long_texts
        self._lock = threading.Lock()
        self._cache = {}
        self._cache_size = cache_size

    @property
    def max_pieces(self) -> int:
        """Word pieces of a text the model reads (its limit minus [CLS] and [SEP])."""
        return max((self.model.max_seq_length or 512) - 2, 1)

    def _windows(self, texts: Sequence[str]) -> List[List[str]]:
        counts = [len(ids) for ids in self.model.tokenizer(list(texts), add_special_tokens=False, truncation=False,
                                                             verbose=False)["input_ids"]]
        return [split_windows(t, n, self.max_pieces) for t, n in zip(texts, counts)]

    def _encode(self, texts: Sequence[str], batch_size: int = 128) -> Tuple[np.ndarray, List[Optional[np.ndarray]]]:
        """``(one vector per text, per text: the (windows, dim) embeddings or None if the text fits)``."""
        texts = list(texts)
        if not texts:
            return np.empty((0, self.dim), dtype=np.float32), []
        if not self.segment_long_texts:
            return self.model.encode(texts, batch_size=batch_size, show_progress_bar=len(texts) > 1000), [None] * len(texts)
        parts = self._windows(texts)
        flat = [w for p in parts for w in p]
        emb = self.model.encode(flat, batch_size=batch_size, show_progress_bar=len(flat) > 1000)
        vectors = np.empty((len(texts), emb.shape[1]), dtype=emb.dtype)
        segments, pos = [], 0
        for i, p in enumerate(parts):
            block = emb[pos:pos + len(p)]
            pos += len(p)
            if len(p) == 1:
                vectors[i] = block[0]
                segments.append(None)
            else:
                mean = block.mean(axis=0)
                vectors[i] = mean / (np.linalg.norm(mean) or 1.0)
                segments.append(block)
        return vectors, segments

    def create_embedding(self, text: str) -> np.ndarray:
        cached = self._cache.get(text)
        if cached is not None:
            return cached
        with self._lock:
            emb = self._encode([text], batch_size=1)[0][0]
        if len(self._cache) < self._cache_size:
            self._cache[text] = emb
        return emb

    def encode_many(self, texts: Sequence[str], batch_size: int = 128) -> np.ndarray:
        return self.encode_many_with_segments(texts, batch_size)[0]

    def encode_many_with_segments(self, texts: Sequence[str], batch_size: int = 128):
        with self._lock:
            return self._encode(texts, batch_size)

    def segment_embeddings(self, text: str) -> Optional[np.ndarray]:
        """The (windows, dim) embeddings of a text that does not fit the model, ``None`` if it fits (or segmenting is off)."""
        if not self.segment_long_texts:
            return None
        with self._lock:
            return self._encode([text], batch_size=1)[1][0]

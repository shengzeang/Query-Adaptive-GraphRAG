"""Thin wrapper around OpenAI-compatible chat endpoints (vLLM servers, DeepSeek, ...)."""
import itertools
import logging
import random
import re
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Callable, Iterator, List, Optional, Sequence

from openai import BadRequestError
from tenacity import (before_sleep_log, retry, retry_if_not_exception_type, stop_after_attempt,
                      wait_random_exponential)

from raptor import BaseSummarizationModel

from .settings import LLMSpec, get_llm_spec

logger = logging.getLogger(__name__)


class ChatLLM:
    """Chat client. ``spec.base_url`` may hold several comma-separated endpoints (e.g. one vLLM server per
    GPU); requests are spread over them round-robin, and a retried request goes to the next endpoint."""

    def __init__(self, spec: LLMSpec):
        from openai import OpenAI

        self.spec = spec
        urls = [u.strip() for u in spec.base_url.split(",") if u.strip()]
        self.clients = [
            OpenAI(base_url=u, api_key=spec.api_key, timeout=spec.timeout, max_retries=0) for u in urls
        ]
        self.client = self.clients[0]
        # itertools.count().__next__ is atomic under the GIL -> thread-safe round robin
        self._counter = itertools.count(random.randrange(len(self.clients)))

    @classmethod
    def from_role(cls, role: str) -> "ChatLLM":
        return cls(get_llm_spec(role))

    @retry(
        retry=retry_if_not_exception_type(BadRequestError),   # a 400 (e.g. context too long) never succeeds on retry
        wait=wait_random_exponential(min=1, max=30),
        stop=stop_after_attempt(8),
        before_sleep=before_sleep_log(logger, logging.WARNING),
        reraise=True,
    )
    def chat(
        self,
        prompt: str,
        max_tokens: int = 256,
        temperature: float = 0.0,
        system: Optional[str] = "You are a helpful assistant.",
    ) -> str:
        messages = ([{"role": "system", "content": system}] if system else []) + [
            {"role": "user", "content": prompt}
        ]
        kwargs = dict(
            model=self.spec.model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        if self.spec.extra_body:
            kwargs["extra_body"] = self.spec.extra_body
        client = self.clients[next(self._counter) % len(self.clients)]
        response = client.chat.completions.create(**kwargs)
        return (response.choices[0].message.content or "").strip()


def parallel_map(fn: Callable, items: Sequence, workers: int = 8) -> List:
    """Order-preserving thread-pool map (the LLM calls are I/O bound)."""
    if workers <= 1 or len(items) <= 1:
        return [fn(x) for x in items]
    with ThreadPoolExecutor(max_workers=workers) as pool:
        return list(pool.map(fn, items))


def parallel_unordered(fn: Callable, items: Sequence, workers: int = 8) -> Iterator:
    """Run ``fn`` over ``items`` in a thread pool and yield results as they finish, in completion order.

    Tasks start in the order of ``items``, so put the slowest ones first. Unlike processing fixed-size
    batches this never idles workers while waiting for the slowest item of a batch.
    """
    items = list(items)
    if workers <= 1 or len(items) <= 1:
        for x in items:
            yield fn(x)
        return
    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = [pool.submit(fn, x) for x in items]
        for future in as_completed(futures):
            yield future.result()


_CONTEXT_ERROR = re.compile(r"maximum context length is (\d+) tokens.*?requested (\d+) tokens \((\d+) in the messages")


class LLMSummarizationModel(BaseSummarizationModel):
    """RAPTOR summariser backed by a chat endpoint (same prompt as upstream RAPTOR).

    RAPTOR bounds a cluster by 3500 cl100k tokens, but the served model counts differently (Qwen splits every
    digit, for example) and a cluster can hold a few very long nodes, so the prompt can exceed the context window.
    In that case the context is cut to what fits, using the token count the server reports, and retried. If it
    still does not fit after MAX_SHRINKS retries, the head of the text is returned as the "summary" instead of
    raising, so one stubborn cluster cannot abort the whole tree build."""

    MAX_SHRINKS = 4
    FALLBACK_CHARS_PER_TOKEN = 3

    def __init__(self, llm: ChatLLM):
        self.llm = llm

    def summarize(self, context, max_tokens=150):
        for attempt in range(self.MAX_SHRINKS + 1):
            prompt = f"Write a summary of the following, including as many key details as possible: {context}:"
            try:
                return self.llm.chat(prompt, max_tokens=max_tokens)
            except BadRequestError as e:
                m = _CONTEXT_ERROR.search(str(e))
                if not m:
                    raise
                if attempt == self.MAX_SHRINKS:
                    logger.warning("summary input still too long after %d shrinks: using the head of the text as "
                                   "the summary", self.MAX_SHRINKS)
                    return context[: max_tokens * self.FALLBACK_CHARS_PER_TOKEN].strip()
                limit, _, prompt_tokens = (int(x) for x in m.groups())
                keep = 0.95 * (limit - max_tokens - 64) / prompt_tokens   # 64: chat template + system prompt
                logger.warning("summary input too long (%d prompt tokens, limit %d): keeping %.0f%% of it",
                               prompt_tokens, limit, 100 * keep)
                context = context[: int(len(context) * keep)]

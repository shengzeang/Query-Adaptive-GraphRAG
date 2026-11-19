"""Model endpoints, read from environment variables only (no secrets in the repository).

Three LLM roles, each an OpenAI-compatible chat endpoint:

* ``backbone``   - answers questions (paper: Qwen2.5-7B-Instruct). Serve it with e.g.
                   ``vllm serve Qwen/Qwen2.5-7B-Instruct --port 8000``.
* ``summarizer`` - writes the RAPTOR summaries. Falls back to the backbone settings.
* ``judge``      - GraphRAG-Bench evaluation. Defaults to the DeepSeek API.

For a role ``R`` the variables are ``R_BASE_URL``, ``R_MODEL``, ``R_API_KEY``; the judge also accepts
``DEEPSEEK_API_KEY``. Defaults: backbone and summarizer = Qwen2.5-7B-Instruct on a local vLLM server,
judge = DeepSeek ``deepseek-flash``. Any role can be pointed at another OpenAI-compatible endpoint.

DeepSeek models think by default, which would multiply the output tokens and ignore ``temperature``.
Thinking is therefore switched off for the judge and for every role whose endpoint is a DeepSeek one
(override with ``<ROLE>_THINKING=enabled``).
"""
import os
from dataclasses import dataclass, field
from typing import Dict, Optional


@dataclass
class LLMSpec:
    base_url: str
    model: str
    api_key: str
    extra_body: Dict = field(default_factory=dict)
    timeout: float = 600.0


_DEFAULTS = {
    "backbone": dict(base_url="http://localhost:8000/v1", model="Qwen/Qwen2.5-7B-Instruct", api_key="EMPTY"),
    "judge": dict(base_url="https://api.deepseek.com", model="deepseek-flash", api_key=None),
}


def _env(role: str, name: str) -> Optional[str]:
    return os.environ.get(f"{role.upper()}_{name}")


def get_llm_spec(role: str) -> LLMSpec:
    if role not in ("backbone", "summarizer", "judge"):
        raise ValueError(f"unknown LLM role: {role}")
    base_role = "backbone" if role == "summarizer" else role
    defaults = _DEFAULTS[base_role]

    def pick(name: str):
        value = _env(role, name)
        if value is None and role == "summarizer":
            value = _env("backbone", name)
        return value if value is not None else defaults.get(name.lower())

    api_key = pick("API_KEY")
    if role == "judge" and not api_key:
        api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        raise RuntimeError(
            f"No API key for the '{role}' LLM: set {role.upper()}_API_KEY"
            + (" or DEEPSEEK_API_KEY" if role == "judge" else "")
        )
    base_url, model = pick("BASE_URL"), pick("MODEL")
    thinking = pick("THINKING") or ("disabled" if role == "judge" or "deepseek" in base_url.lower() else None)
    extra_body = {"thinking": {"type": thinking}} if thinking else {}
    return LLMSpec(base_url=base_url, model=model, api_key=api_key, extra_body=extra_body)

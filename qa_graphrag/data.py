"""Dataset loaders. Everything is downloaded from the Hugging Face Hub on demand.

Common example schema of the KGQA-style datasets::

    {"id": str, "question": str, "answers": [str, ...], "ctxs": [{"title": str, "text": str}, ...]}
"""
import fcntl
import json
import os
import random
import re
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple

BENCH_REPO = "jeremycp3/GraphRAG-Bench"
BENCH_TASKS = ["FB", "MC", "MS", "TF", "OE"]
NUM_TEXTBOOKS = 20

# split used for evaluation / source of the router training questions
KGQA_SOURCES = {
    "hotpotqa": dict(repo="hotpotqa/hotpot_qa", eval_files=["distractor/validation-00000-of-00001.parquet"],
                     train_files=["distractor/train-00000-of-00002.parquet", "distractor/train-00001-of-00002.parquet"]),
    "2wikimqa": dict(repo="framolfese/2WikiMultihopQA", eval_files=["data/validation-00000-of-00001.parquet"], train_files=[]),
    "musique": dict(repo="dgslibisey/MuSiQue", eval_files=["musique_ans_v1.0_dev.jsonl"], train_files=[]),
}
# Router-training sources in their native, full form (paper Sec. 5.2.1)
NQ_REPO = "google-research-datasets/natural_questions"       # whole Wikipedia page per question
NQ_TRAIN_SHARDS = 287
TRIVIA_REPO = "mandarjoshi/trivia_qa"                          # config `rc`: Wikipedia pages + web pages per question
TRIVIA_TRAIN_SHARDS = 26
ROUTER_SOURCES = ("hotpotqa", "nq", "triviaqa")


# --------------------------------------------------------------------------- io helpers
def read_jsonl(path) -> List[Dict]:
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def append_jsonl(path, record: Dict) -> None:
    """Append one record; safe when several shard processes write to the same file."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    line = json.dumps(record, ensure_ascii=False) + "\n"
    with open(path, "a", encoding="utf-8") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        try:
            f.write(line)
            f.flush()
        finally:
            fcntl.flock(f, fcntl.LOCK_UN)


def parse_shard(spec: Optional[str]) -> Tuple[int, int]:
    """``"i/N"`` -> ``(i, N)``; ``None`` -> ``(0, 1)`` (no sharding)."""
    if not spec:
        return 0, 1
    i, n = (int(x) for x in spec.split("/"))
    if not 0 <= i < n:
        raise ValueError(f"bad shard {spec!r}: need 0 <= i < N")
    return i, n


def take_shard(items: List, shard: Tuple[int, int]) -> List:
    """Disjoint round-robin slice of ``items``; the union over all shards is ``items``."""
    i, n = shard
    return list(items)[i::n]


def longest_first(examples: List[Dict]) -> List[Dict]:
    """Largest corpora first: they dominate the run time, so starting them early avoids a long tail
    where only a few huge documents are still being processed."""
    return sorted(examples, key=lambda e: -sum(len(c.get("text", "")) for c in e["ctxs"]))


def write_jsonl(path, records: Iterable[Dict]) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def done_ids(path) -> Set[str]:
    if not os.path.exists(path):
        return set()
    return {str(r["id"]) for r in read_jsonl(path)}


def refuse_other_prompt(path, current: str) -> None:
    """Exit if the result file holds rows made with another prompt version (rows without the field: an older prompt).
    Several versions in one file would make the results incomparable; resuming only works within one version."""
    if not os.path.exists(path):
        return
    previous = {r.get("prompt", "none") for r in read_jsonl(path)}
    if previous - {current}:
        raise SystemExit(f"{path} was made with prompt version {sorted(previous)}, the code uses '{current}': write to "
                         f"another --out (or delete the file) instead of mixing versions")


def refuse_other_retrieval(path, current: str) -> None:
    """Exit if the result file holds rows made with another RAPTOR retrieval mode (rows without the field: ``traverse``,
    the only mode before ``RETRIEVAL`` existed). Resuming would silently skip the questions answered the old way."""
    if not os.path.exists(path):
        return
    previous = {r.get("retrieval", "traverse") for r in read_jsonl(path)}
    if previous - {current}:
        raise SystemExit(f"{path} was made with RAPTOR retrieval {sorted(previous)}, the code uses '{current}': write to "
                         f"another --out (or delete the file), or set RETRIEVAL={sorted(previous)[0]}")


def refuse_other_top_k(path, current: int) -> None:
    """Exit if the result file holds rows made with another ``--top-k`` (rows without the field: 5, the fixed value before it
    existed). It changes every method, and resuming would silently skip the questions answered with the other value."""
    if not os.path.exists(path):
        return
    previous = {r.get("top_k", 5) for r in read_jsonl(path)}
    if previous - {current}:
        raise SystemExit(f"{path} was made with --top-k {sorted(previous)}, not {current}: write to another --out "
                         f"(or delete the file) instead of mixing top-k values")


def warn_router_retrieval(routers: dict, current: str, top_k: int = None) -> None:
    """Say so when a router was trained on labels made with another retrieval mode (or top-k) than the one it is used with:
    its levels then mean something else (a start level of the descent is not a start level of the collapsed tree)."""
    for name, router in routers.items():
        if router.retrieval != current:
            print(f"WARNING: router '{name}' was trained on labels of RETRIEVAL={router.retrieval}, but this run retrieves "
                  f"with RETRIEVAL={current}: the router is used with a retrieval it was not trained for")
        if top_k is not None and router.top_k != top_k:
            print(f"WARNING: router '{name}' was trained on labels of top-k {router.top_k}, but this run uses top-k {top_k}: "
                  f"the router is used with a retrieval it was not trained for")


def _download(repo: str, filename: str) -> str:
    from huggingface_hub import hf_hub_download

    return hf_hub_download(repo_id=repo, filename=filename, repo_type="dataset")


def doc_text(ctx: Dict) -> str:
    """How a paragraph is rendered inside the per-question corpus."""
    return f"{ctx['title']}\n\n{ctx['text']}\n\n" if ctx.get("title") else f"{ctx['text']}\n\n"


# --------------------------------------------------------------------------- KGQA datasets
def _from_hotpot_style(row) -> Dict:
    ctx = row["context"]
    return {
        "id": str(row["id"]),
        "question": row["question"],
        "answers": [row["answer"]],
        "ctxs": [
            {"title": t, "text": " ".join(s).strip()} for t, s in zip(list(ctx["title"]), list(ctx["sentences"]))
        ],
    }


def _read_parquet_rows(path: str, columns: Optional[List[str]] = None):
    import pandas as pd

    return pd.read_parquet(path, columns=columns).to_dict("records")


def load_kgqa(name: str, split: str = "eval", n: Optional[int] = None, seed: int = 0) -> List[Dict]:
    """Load (and randomly subsample to ``n`` examples) HotpotQA / 2WikiMQA / MuSiQue."""
    if name not in KGQA_SOURCES:
        raise ValueError(f"unknown dataset {name}; choose from {list(KGQA_SOURCES)}")
    spec = KGQA_SOURCES[name]
    files = spec["eval_files"] if split == "eval" else spec["train_files"]
    if not files:
        raise ValueError(f"{name} has no '{split}' split configured")
    examples: List[Dict] = []
    for fname in files:
        path = _download(spec["repo"], fname)
        if name == "musique":
            for row in read_jsonl(path):
                if not row.get("answerable", True):
                    continue
                examples.append(
                    {
                        "id": row["id"],
                        "question": row["question"],
                        "answers": [row["answer"]] + list(row.get("answer_aliases") or []),
                        "ctxs": [{"title": p["title"], "text": p["paragraph_text"]} for p in row["paragraphs"]],
                    }
                )
        else:
            examples.extend(_from_hotpot_style(r) for r in _read_parquet_rows(path))
    return subsample(examples, n, seed)


def split_specialist_and_test(name: str, n_specialist: int = 200, n_test: Optional[int] = 1000, seed: int = 0):
    """Deterministic split of a KGQA evaluation set into the examples used to fine-tune the
    Specialist router (``n_specialist``) and the disjoint test examples (``n_test``).

    The Specialist examples are removed from the test set, so no test question is ever seen by any router.
    """
    examples = load_kgqa(name, split="eval", n=None)
    order = random.Random(seed).sample(range(len(examples)), len(examples))
    specialist = [examples[i] for i in order[:n_specialist]]
    test = [examples[i] for i in order[n_specialist:]]
    if n_test is not None:
        test = test[:n_test]
    return specialist, test


def subsample(items: List, n: Optional[int], seed: int = 0) -> List:
    if n is None or n >= len(items):
        return list(items)
    return random.Random(seed).sample(items, n)


# --------------------------------------------------------------------------- native NQ / TriviaQA
_NQ_LINE_BREAK = {
    "</p>", "</h1>", "</h2>", "</h3>", "</h4>", "</h5>", "</h6>", "</li>", "</tr>", "</table>",
    "</ul>", "</ol>", "</dd>", "</dt>", "</dl>", "</caption>",
}
_NQ_CELL_END = {"</td>", "</th>"}


def render_nq_document(title: str, tokens: Dict[str, list]) -> str:
    """Plain text of a Natural Questions Wikipedia page.

    NQ stores the page as a token stream in which HTML tags are separate tokens. Tags are dropped; the
    end of a block element (paragraph, heading, list item, table row) becomes a line break and table
    cells are separated by `` | ``, so the page keeps its structure for chunking.
    """
    parts: List[str] = []
    for tok, is_html in zip(tokens["token"], tokens["is_html"]):
        if not is_html:
            parts.append(tok)
            continue
        t = tok.lower()
        if t in _NQ_LINE_BREAK:
            parts.append("\n")
        elif t in _NQ_CELL_END:
            parts.append("|")
    text = " ".join(parts)
    text = re.sub(r" ([,.;:!?%)\]}])", r"\1", text)
    text = re.sub(r"([(\[{$]) ", r"\1", text)
    text = re.sub(r" ([-–—/]) ", r"\1", text)                  # NQ tokenises "three-quarters" as "three - quarters"
    text = re.sub(r" ('s|'d|'ll|'re|'ve|'m|n't)\b", r"\1", text)
    text = re.sub(r'"[ \t]+([^"\n]*?)[ \t]+"', r'"\1"', text)   # paired double quotes
    text = re.sub(r"[ \t]*\n[ \t]*", "\n", text)
    text = re.sub(r"(?:[ \t]*\|[ \t]*)+\n", "\n", text)       # trailing cell separators
    text = re.sub(r"\n{2,}", "\n", text).strip()
    return f"{title}\n{text}" if title else text


def _nq_short_answers(annotations: Dict) -> List[str]:
    answers: List[str] = []
    for sa in annotations["short_answers"]:
        for t in sa["text"]:
            t = t.strip()
            if t and t not in answers:
                answers.append(t)
    return answers


def _sample_from_shards(
    repo: str, shard_fmt: str, num_shards: int, n: int, seed: int,
    light_columns: List[str], light_fn, heavy_columns: List[str], heavy_fn,
    pool_factor: int = 2, min_shards: int = 3, shard: Tuple[int, int] = (0, 1),
) -> List[Dict]:
    """Randomly sample ``n`` examples of a big sharded parquet dataset without downloading all of it.

    Shards are visited in a seeded random order; each is scanned with the cheap ``light_columns`` only
    (``light_fn`` returns a record, or None to reject the row) until the candidate pool holds
    ``pool_factor * n`` rows (and at least ``min_shards`` shards were read). ``n`` candidates are then
    drawn uniformly, then ``shard`` selects this process's slice, and only the heavy columns (the
    documents) of that slice are read.
    """
    import pyarrow.parquet as pq
    from collections import defaultdict

    rng = random.Random(seed)
    pool, seen = [], set()
    for read, file_idx in enumerate(rng.sample(range(num_shards), num_shards), start=1):
        path = _download(repo, shard_fmt.format(i=file_idx))
        pf = pq.ParquetFile(path)
        for rg in range(pf.num_row_groups):
            for row, rec in enumerate(pf.read_row_group(rg, columns=light_columns).to_pylist()):
                light = light_fn(rec)
                if light is not None and light["id"] not in seen:   # a few question ids occur twice
                    seen.add(light["id"])
                    pool.append((path, rg, row, light))
        if read >= min_shards and len(pool) >= pool_factor * n:
            break
    picked = take_shard(rng.sample(pool, min(n, len(pool))), shard)

    groups = defaultdict(list)
    for k, (path, rg, row, light) in enumerate(picked):
        groups[(path, rg)].append((k, row, light))
    out: List[Optional[Dict]] = [None] * len(picked)
    for (path, rg), items in groups.items():
        table = pq.ParquetFile(path).read_row_group(rg, columns=heavy_columns).take([row for _, row, _ in items])
        for (k, _, light), rec in zip(items, table.to_pylist()):
            out[k] = heavy_fn(light, rec)
    return out


def load_nq_train(n: int = 2000, seed: int = 0, shard: Tuple[int, int] = (0, 1)) -> List[Dict]:
    """Natural Questions (full version, ``google-research-datasets/natural_questions``).

    Questions with at least one short answer; the corpus of a question is its complete Wikipedia page.
    """
    def light(rec):
        answers = _nq_short_answers(rec["annotations"])
        if not answers:
            return None
        return {"id": str(rec["id"]), "question": rec["question"]["text"], "answers": answers}

    def heavy(light_rec, rec):
        doc = rec["document"]
        return {**light_rec, "ctxs": [{"title": "", "text": render_nq_document(doc["title"], doc["tokens"])}]}

    return _sample_from_shards(
        NQ_REPO, "default/train-{i:05d}-of-00287.parquet", NQ_TRAIN_SHARDS, n, seed,
        ["id", "question", "annotations"], light, ["document.title", "document.tokens"], heavy, shard=shard,
    )


def load_triviaqa_train(n: int = 2000, seed: int = 0, shard: Tuple[int, int] = (0, 1)) -> List[Dict]:
    """TriviaQA (``mandarjoshi/trivia_qa``, config ``rc``).

    The corpus of a question is all of its evidence: the Wikipedia pages of the answer entities and the
    web pages returned by the search engine, each as one document.
    """
    def light(rec):
        ans = rec["answer"]
        answers = list(dict.fromkeys([ans["value"]] + list(ans["aliases"])))
        return {"id": str(rec["question_id"]), "question": rec["question"], "answers": [a for a in answers if a]}

    def heavy(light_rec, rec):
        ctxs = []
        wiki, web = rec["entity_pages"], rec["search_results"]
        for title, text in zip(wiki["title"], wiki["wiki_context"]):
            if text and text.strip():
                ctxs.append({"title": title, "text": text.strip()})
        for title, text in zip(web["title"], web["search_context"]):
            if text and text.strip():
                ctxs.append({"title": title, "text": text.strip()})
        return {**light_rec, "ctxs": ctxs}

    return _sample_from_shards(
        TRIVIA_REPO, "rc/train-{i:05d}-of-00026.parquet", TRIVIA_TRAIN_SHARDS, n, seed,
        ["question_id", "question", "answer"], light, ["entity_pages", "search_results"], heavy, shard=shard,
    )


def load_router_source(name: str, n: int = 2000, seed: int = 0, shard: Tuple[int, int] = (0, 1)) -> List[Dict]:
    """Questions used to build the router training data (paper Sec. 5.2.1): ``n`` random training
    questions of HotpotQA (distractor setting), NQ and TriviaQA, each with its native, full evidence.
    ``shard=(i, N)`` returns only the i-th of N disjoint slices of that sample."""
    if name == "hotpotqa":
        return take_shard(load_kgqa("hotpotqa", split="train", n=n, seed=seed), shard)
    if name == "nq":
        return load_nq_train(n, seed, shard)
    if name == "triviaqa":
        return load_triviaqa_train(n, seed, shard)
    raise ValueError(f"unknown router source {name}; choose from {ROUTER_SOURCES}")


# --------------------------------------------------------------------------- GraphRAG-Bench
def load_bench_questions(task: str, limit: Optional[int] = None) -> List[Dict]:
    """GraphRAG-Bench questions of one task (FB / MC / MS / TF / OE), in the official order."""
    rows = read_jsonl(_download(BENCH_REPO, f"questions/{task}.jsonl"))
    return rows[:limit] if limit else rows


def load_bench_textbook(i: int) -> str:
    path = _download(BENCH_REPO, f"textbooks/textbook{i}/textbook{i}.md")
    return Path(path).read_text(encoding="utf-8")

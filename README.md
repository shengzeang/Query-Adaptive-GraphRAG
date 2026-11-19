# QA-GraphRAG / RAPTOR-QA reproduction

This repository reproduces **RAPTOR-QA**, i.e. [RAPTOR](https://github.com/parthsarthi03/raptor) plus the
query-adaptive *retrieval-level router* of the QA-GraphRAG paper, and the main
experiments of the paper for it: KGQA datasets (MuSiQue / 2WikiMQA / HotpotQA) and
GraphRAG-Bench (FB / MC / MS / TF / OE), compared with BM25, TF-IDF and vanilla RAPTOR.

## Idea in 30 seconds

* RAPTOR builds a tree: level 0 = raw text chunks, higher levels = recursive summaries.
* Level convention used in this code base: *retrieving from level k* means start at tree layer k, then
  descend to the leaves (context = layers k..0). Level 0 is plain chunk retrieval; higher levels add more
  abstract knowledge.
* The **router** (`qa_graphrag/router.py`) is a 3-layer MLP on the query embedding that outputs a preference
  score per level. Training uses Gumbel-Softmax and the loss `1 - sum(P * Q~)` (paper Eq. 2), where `P` is the
  accuracy obtained when retrieval starts at each level. Inference is deterministic (`argmax`) and the
  query is routed once before a single retrieval.

## Layout

```
qa_graphrag/            the reproduction code
  router.py             MLPRouter, loss, training loop
  pipeline.py           QueryRunner: encode -> route -> retrieve -> generate (BM25 / TF-IDF / RAPTOR / level-k / start-k / RAPTOR-QA)
  retrieval.py          TreeIndex (RAPTOR retrieval: collapse / traverse) and flat BM25 / TF-IDF baselines
  index.py              tree building + on-disk cache
  data.py               dataset loaders (all downloaded from the Hugging Face Hub), consistency guards
  metrics.py            KGQA Accuracy / Recall
  bench_eval.py         GraphRAG-Bench evaluation (port of the official evaluator.py)
  prompts.py, llm.py, settings.py, embedding.py, runtime.py
scripts/
  run_all.sh            the whole pipeline in resumable stages (serve ... bench), see below
  gen_router_data.py    per-level labels for router training
  train_router.py       Generalist router
  run_kgqa.py           KGQA experiments (MuSiQue / 2WikiMQA / HotpotQA)
  build_bench_index.py  shared RAPTOR tree over the 20 GraphRAG-Bench textbooks
  run_bench.py          GraphRAG-Bench experiments (generation + official scoring)
  compare_runs.py       question-by-question comparison of two bench runs or of two routers (--pair)
  tune_router.py        router diagnostics and hyper-parameter search (reads the labels only)
  analyze_failures.py, measure_level_overlap.py, measure_chunk_size.py, count_duplicate_embeddings.py
                        offline analyses (CPU only, no LLM calls)
raptor/                 upstream RAPTOR package with fixes and additions (see "Changes to the upstream raptor package")
tests/                  offline unit tests (`pytest tests`)
```

## Setup

```bash
git clone https://github.com/shengzeang/Query-Adaptive-GraphRAG.git
cd Query-Adaptive-GraphRAG
pip install -r requirements.txt
cp .env.example .env   # then edit; `set -a; source .env; set +a`
```

Three OpenAI-compatible LLM endpoints are configured through environment variables (see `.env.example`):

| role | used for | default |
|---|---|---|
| `BACKBONE_*` | answers the questions | local vLLM serving `Qwen/Qwen2.5-7B-Instruct` |
| `SUMMARIZER_*` | RAPTOR summaries | same as backbone (Qwen2.5-7B-Instruct) |
| `JUDGE_*` / `DEEPSEEK_API_KEY` | GraphRAG-Bench judge | DeepSeek v4.1 flash |

Embeddings (query, nodes, router input) use `sentence-transformers/all-MiniLM-L6-v2` (384-d).

## Methods and settings that must stay consistent

| method | meaning |
|---|---|
| `bm25`, `tfidf` | flat chunk retrieval baselines (top-k chunks) |
| `raptor` | vanilla RAPTOR retrieval over the whole tree |
| `raptor-qa` | the router picks the start level, then RAPTOR retrieval from that level (`--routers name=ckpt`) |
| `level<k>`, `start<k>` | fixed start level k (diagnostics; `start<k>` uses the configured `RETRIEVAL` mode and is what the router labels are computed with) |

| setting (env) | values | effect |
|---|---|---|
| `RETRIEVAL` | `collapse` (default) / `traverse` | `collapse`: top-k over all nodes of the layers k..0; `traverse`: layer-by-layer descent keeping k nodes per layer |
| `TOP_K` | default 5 | nodes kept (per layer for `traverse`, in total for `collapse`, BM25 and TF-IDF) |
| `BENCH_CHUNK` | default 200 | GraphRAG-Bench chunk size in tokens (1200 = the benchmark paper's size) |

The router labels depend on `RETRIEVAL` and `TOP_K`. A router must be **trained and used with the same
values** it was labelled with. Every label / result row records them (rows without the fields count as `traverse` /
5), checkpoints store `retrieval` and `top_k`, and the scripts refuse to mix values in one output file and warn when a router
is used with other settings. So give every combination its own directories:

```bash
RETRIEVAL=traverse TOP_K=10 DATA=data/router_t10 CKPT=checkpoints_t10 OUT_KGQA=outputs/kgqa_t10 OUT_BENCH=outputs/bench_t10 \
  bash scripts/run_all.sh labels train kgqa bench
```

The cached trees (`indexes/`) do not depend on any of them and are reused.

## Run: RAPTOR and RAPTOR-QA (Generalist), KGQA and GraphRAG-Bench

All stages are in `scripts/run_all.sh` (`serve stop check labels train kgqa bench_index bench | all`). Every
stage is sharded over the GPUs / cores and resumable (re-running skips finished questions and cached trees); logs go to
`logs/`. Answers and RAPTOR summaries come from Qwen2.5-7B-Instruct on local vLLM replicas; only the GraphRAG-Bench judge
calls DeepSeek flash (`DEEPSEEK_API_KEY`, needed by `check` and `bench` only).

```bash
# 0. servers: GPUS=8 vLLM replicas on ports 8000..8007 (one per GPU); stop them first if their context window must change
bash scripts/run_all.sh serve
export DEEPSEEK_API_KEY=...
bash scripts/run_all.sh check                      # reachability of every endpoint, thinking mode off for DeepSeek
SMOKE=1 bash scripts/run_all.sh all                # tiny end-to-end run (outputs under *_smoke/)

# 1. router (Generalist): labels from HotpotQA / NQ / TriviaQA, then training  -> checkpoints/generalist.pt
bash scripts/run_all.sh labels train

# 2. KGQA: raptor and raptor-qa (Generalist) on MuSiQue / 2WikiMQA / HotpotQA  -> outputs/kgqa/<dataset>_summary.json
KGQA_METHODS="raptor raptor-qa" bash scripts/run_all.sh kgqa

# 3. GraphRAG-Bench: tree over the 20 textbooks, then raptor and raptor-qa (Generalist)  -> outputs/bench/summary.json
bash scripts/run_all.sh bench_index
BENCH_METHODS="raptor raptor-qa" BENCH_ROUTERS="generalist=checkpoints/generalist.pt" bash scripts/run_all.sh bench

bash scripts/run_all.sh stop
```

The same with a different setting (collapse is the default; see the table above), e.g. the GraphRAG-Bench paper's chunk size
with `TOP_K=10` and the first experiments' retrieval:

```bash
export RETRIEVAL=traverse TOP_K=10 BENCH_CHUNK=1200
export DATA=data/router_t10 CKPT=checkpoints_t10 OUT_KGQA=outputs/kgqa_t10 OUT_BENCH=outputs/bench_t10_c1200
bash scripts/run_all.sh stop; bash scripts/run_all.sh serve     # the context window follows TOP_K / BENCH_CHUNK (up to 32768)
bash scripts/run_all.sh labels train kgqa bench_index bench
```

Without `KGQA_*` / `BENCH_*` the `kgqa` and `bench` stages also run BM25 and TF-IDF; `all` runs everything.

Variables of `run_all.sh` (all optional; the header of the script has the full list):

| variable | default | meaning |
|---|---|---|
| `GPUS`, `SHARDS`, `WORKERS`, `BENCH_SHARDS`, `BENCH_WORKERS`, `JUDGE_WORKERS` | 8, 8, 8, 20, 256, 64 | parallelism |
| `KGQA_METHODS`, `KGQA_ROUTERS` | all four methods, `generalist=$CKPT/generalist.pt` | restrict the `kgqa` stage / use other `name=checkpoint` routers |
| `BENCH_METHODS`, `BENCH_ROUTERS`, `BENCH_TASKS` | all four methods, `generalist=$CKPT/generalist.pt`, all five tasks (`FB MC MS TF OE`) | restrict the `bench` stage |
| `ENCODER_DEVICE` | auto | `cpu` puts the sentence encoder on the CPU (see "Troubleshooting") |
| `BACKBONE_*`, `SUMMARIZER_*`, `VLLM_*` | see `.env.example` / script header | other backbones, vLLM command and settings |

### Comparing routers (checkpoints) on GraphRAG-Bench

Each router becomes its own method directory `raptor-qa_<name>` under `$OUT_BENCH`; already finished questions are
skipped, so adding a router to an existing run only generates and scores the new one:

```bash
BENCH_METHODS=raptor-qa BENCH_ROUTERS="old=checkpoints/generalist.pt new=checkpoints_t10/generalist.pt" \
  bash scripts/run_all.sh bench
python scripts/compare_runs.py outputs/bench outputs/bench --pair raptor-qa_old raptor-qa_new   # question by question
```

(Routers trained with other `RETRIEVAL` / `TOP_K` produce a warning when used with the current setting.) Two runs, e.g. two
settings on the same tree, are compared with `python scripts/compare_runs.py outputs/bench_a outputs/bench_b`.

### Reading the results

* KGQA: `$OUT_KGQA/<dataset>.jsonl` (one row per question and method) and `<dataset>_summary.json`: Accuracy (gold answer
  contained in the output) and Recall (token recall) x100 per method, plus the distribution of levels chosen by the router.
* GraphRAG-Bench: `$OUT_BENCH/<method>/` holds the predictions in the official format and `eval_details.json`;
  `$OUT_BENCH/summary.json` the scores per task (rationale / answer / AR score, official protocol). `summary.json` is merged
  with an existing one, so partial runs add to it.

### Step by step, without `run_all.sh`

```bash
# router training labels: 2000 questions from each source (HotpotQA train, NQ, TriviaQA)
for s in hotpotqa nq triviaqa; do
  python scripts/gen_router_data.py --source $s --n 2000 --out data/router/$s.jsonl --workers 16
done
# Generalist router (all three sources)
python scripts/train_router.py --data data/router/{hotpotqa,nq,triviaqa}.jsonl --out checkpoints/generalist.pt
# KGQA
for d in musique 2wikimqa hotpotqa; do
  python scripts/run_kgqa.py --dataset $d --n 1000 --methods bm25 tfidf raptor raptor-qa \
      --routers generalist=checkpoints/generalist.pt
done
# GraphRAG-Bench
python scripts/build_bench_index.py --out indexes/graphrag_bench_c200.pkl --workers 32   # 200-token chunks
python scripts/run_bench.py --tree indexes/graphrag_bench_c200.pkl --methods bm25 tfidf raptor raptor-qa \
    --routers generalist=checkpoints/generalist.pt
```

`--top-k`, `--chunk-tokens` and the other options are shared by the scripts (`python scripts/<script>.py --help`; the
environment variables `RETRIEVAL` and `ENCODER_DEVICE` are read by the python code, `TOP_K` is passed as
`--top-k` by `run_all.sh`). Use `--limit 5 --tasks FB MC` on `run_bench.py` and `--n 20` on `run_kgqa.py` for a quick smoke test.


### Changes to the upstream `raptor` package

The `raptor/` package is the upstream code with these changes (the reproduction depends on them; vanilla upstream behaviour
differs in the first two defaults):

* `RetrievalAugmentation` defaults to `collapse_tree=False` (layer-by-layer traversal); `ClusterTreeConfig` defaults to
  `reduction_dimension=2`.
* Clustering fixes: cluster members are index based (identical embeddings no longer duplicate texts), no `RecursionError`
  on pathological clusters (`split_by_length`, bounded re-clustering), UMAP `n_neighbors >= 2`, GMM `reg_covar=1e-5`.
* `TreeBuilder`: parallel summaries (`parallel_summaries`), `merge_trees`, `num_layers` restored on load.
* `TreeRetriever.node_distances` and `utils.distances_to_nearest_segment` (segment embeddings for long nodes).
* `raptor/NewRetrievalAugmentation.py`: `Builder` / `Retriever` with `BuilderConfig` / `RetrieverConfig` used by `qa_graphrag`.
* Logging is lowered to ERROR.

Notes

* Every question gets its own tree (built from its own evidence, cached in `indexes/` and shared by all
  methods). The first 200 questions of each dataset's seeded shuffle are held out of the test set (not used here, but it keeps the test questions identical to earlier runs).
* Router-training data uses each dataset in its native, full form (no synthetic distractors):
  HotpotQA = the 10 distractor-setting paragraphs; NQ = the complete Wikipedia page of the question
  (`google-research-datasets/natural_questions`, questions with a short answer, HTML tokens removed);
  TriviaQA = all evidence of the `rc` config (Wikipedia pages + web search results). These corpora are
  much longer than HotpotQA's (median about 7k tokens for NQ and 14k for TriviaQA, up to 60k-200k+), so
  generating labels for NQ / TriviaQA takes many more summary calls; raw NQ / TriviaQA shards are
  downloaded on demand (about 2 GB / 1 GB of parquet for 2000 questions).
* `run_kgqa.py` reports Accuracy (gold answer contained in the output) and Recall (token recall) x100 per
  method, plus the distribution of levels chosen by the router (`outputs/kgqa/<dataset>_summary.json`).
  Per-query times are only meaningful with `--workers 1`.
* `run_bench.py` writes predictions in the official GraphRAG-Bench format and scores them with the official
  protocol (rationale / answer / AR score); `--no-eval` and `--eval-only` split generation from scoring.
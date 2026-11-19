# QA-GraphRAG: Query-Adaptive Plug-and-Play Retrieval Integration for Graph-based Retrieval-Augmented Generation

This repository contains the implementation of QA-GraphRAG based on RAPTOR in the paper *"QA-GraphRAG: Query-Adaptive Plug-and-Play Retrieval Integration for Graph-based Retrieval-Augmented Generation"*.

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

| role                           | used for              | default                                       |
| ------------------------------ | --------------------- | --------------------------------------------- |
| `BACKBONE_*`                   | answers the questions | local vLLM serving `Qwen/Qwen2.5-7B-Instruct` |
| `SUMMARIZER_*`                 | RAPTOR summaries      | same as backbone (Qwen2.5-7B-Instruct)        |
| `JUDGE_*` / `DEEPSEEK_API_KEY` | GraphRAG-Bench judge  | DeepSeek v4.1 flash                           |

Embeddings (query, nodes, router input) use `sentence-transformers/all-MiniLM-L6-v2` (384-d).

## Methods and settings that must stay consistent

The defaults are `RETRIEVAL=traverse` (layer-by-layer descent of the tree), `TOP_K=10` and `BENCH_CHUNK=200`. The router labels depend on `RETRIEVAL` and `TOP_K`. A router must be **trained and used with the same values** it was labelled with. Every label / result row records them (rows without the fields count as `traverse`/5), checkpoints store `retrieval` and `top_k`, and the scripts refuse to mix values in one output file and warn when a router is used with other settings. So give every combination its own directories:

```bash
RETRIEVAL=collapse TOP_K=5 DATA=data/router_collapse_k5 CKPT=checkpoints_collapse_k5 OUT_KGQA=outputs/kgqa_collapse_k5 OUT_BENCH=outputs/bench_collapse_k5 \
  bash scripts/run_all.sh labels train kgqa bench
```

The cached trees (`indexes/`) do not depend on any of them and are reused.

## Run: RAPTOR and RAPTOR-QA (Generalist), KGQA and GraphRAG-Bench

All stages are in `scripts/run_all.sh` (`serve stop check labels train kgqa bench_index bench | all`). Every stage is sharded over the GPUs / cores and resumable (re-running skips finished questions and cached trees); logs go to `logs/`. Answers and RAPTOR summaries come from Qwen2.5-7B-Instruct on local vLLM replicas; only the GraphRAG-Bench judge calls DeepSeek flash (`DEEPSEEK_API_KEY`, needed by `check` and `bench` only).

```bash
# 0. servers: GPUS=8 vLLM replicas on ports 8000..8007 (one per GPU); stop them first if their context window must change
bash scripts/run_all.sh serve
export DEEPSEEK_API_KEY=...
bash scripts/run_all.sh check                      
SMOKE=1 bash scripts/run_all.sh all # tiny end-to-end run (outputs under *_smoke/)

# 1. router (Generalist): labels from HotpotQA / NQ / TriviaQA, then training  -> checkpoints/generalist.pt
bash scripts/run_all.sh labels train

# 2. KGQA: raptor and raptor-qa (Generalist) on MuSiQue / 2WikiMQA / HotpotQA  -> outputs/kgqa/<dataset>_summary.json
bash scripts/run_all.sh kgqa

# 3. GraphRAG-Bench: tree over the 20 textbooks, then raptor and raptor-qa (Generalist)  -> outputs/bench/summary.json
bash scripts/run_all.sh bench_index
bash scripts/run_all.sh bench

bash scripts/run_all.sh stop
```

By default only `raptor` and `raptor-qa` are run. The BM25 / TF-IDF baselines are added with
`KGQA_METHODS="bm25 tfidf raptor raptor-qa"` and `BENCH_METHODS="bm25 tfidf raptor raptor-qa"` (or `--methods bm25 tfidf raptor raptor-qa`
when calling `run_kgqa.py` / `run_bench.py` directly). `KGQA_ROUTERS` / `BENCH_ROUTERS` (`name=checkpoint` pairs, default
`generalist=$CKPT/generalist.pt`) select the routers used by `raptor-qa`.

### Reading the results

* KGQA: `$OUT_KGQA/<dataset>.jsonl` (one row per question and method) and `<dataset>_summary.json`: Accuracy (gold answer contained in the output) and Recall (token recall) x100 per method, plus the distribution of levels chosen by the router.
* GraphRAG-Bench: `$OUT_BENCH/<method>/` holds the predictions in the official format and `eval_details.json`;
  `$OUT_BENCH/summary.json` the scores per task (rationale / answer / AR score, official protocol; the log shows only the Answer score). `summary.json` is merged with an existing one, so partial runs add to it.

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
  python scripts/run_kgqa.py --dataset $d --n 1000 --methods raptor raptor-qa \
      --routers generalist=checkpoints/generalist.pt
done
# GraphRAG-Bench
python scripts/build_bench_index.py --out indexes/graphrag_bench_c200.pkl --workers 32   # 200-token chunks
python scripts/run_bench.py --tree indexes/graphrag_bench_c200.pkl --methods raptor raptor-qa \
    --routers generalist=checkpoints/generalist.pt
```

`--top-k`, `--chunk-tokens` and the other options are shared by the scripts (`python scripts/<script>.py --help`; the
environment variables `RETRIEVAL` and `ENCODER_DEVICE` are read by the python code, `TOP_K` is passed as
`--top-k` by `run_all.sh`). Use `--limit 5 --tasks FB MC` on `run_bench.py` and `--n 20` on `run_kgqa.py` for a quick smoke test.


### Changes to the upstream `raptor` package

The `raptor/` package is the upstream code with these changes (the reproduction depends on them; vanilla upstream behaviour differs in the first two defaults):

* `RetrievalAugmentation` defaults to `collapse_tree=False` (layer-by-layer traversal); `ClusterTreeConfig` defaults to
  `reduction_dimension=2`.
* Clustering fixes: cluster members are index based (identical embeddings no longer duplicate texts), no `RecursionError` on pathological clusters (`split_by_length`, bounded re-clustering), UMAP `n_neighbors >= 2`, GMM `reg_covar=1e-5`.
* `TreeBuilder`: parallel summaries (`parallel_summaries`), `merge_trees`, `num_layers` restored on load.
* `utils.distances_from_embeddings`: cosine distances are computed in a vectorized float64 batch rather than with one
  SciPy call per node; the other distance metrics are unchanged. Numerical kernels release the GIL. `np.einsum` avoids
  BLAS thread-pool overhead / oversubscription when many queries run concurrently.
* `TreeRetriever.node_distances` and `utils.distances_to_nearest_segment`: long nodes are ranked by their closest window;
  window similarities and per-node maxima are vectorized. Layers / pools with fewer than 4096 nodes are stacked on demand.
* For layers / pools with at least 4096 nodes, `TreeRetriever` lazily builds a normalized float32 matrix of the whole tree
  once, under a lock, and reuses it across queries. All windows of a node are stored together. Near-ties can rank differently
  from float64 because of rounding. The matrix adds about 193 MB for a 124.5k-node, 384-dimensional tree (more with extra
  windows), shared by threads of the same retriever but not by processes. The first large query pays the construction cost;
  create a new `TreeRetriever` after changing tree embeddings. The sorted all-node list is also cached.
* `qa_graphrag.retrieval.TreeIndex` caches each collapse pool (layers 0 through the chosen level) instead of rebuilding it
  for every query. Both traversal and collapse benefit from the vectorized ranking above.
* `raptor/NewRetrievalAugmentation.py`: `Builder` / `Retriever` with `BuilderConfig` / `RetrieverConfig` used by `qa_graphrag`.

### Notes

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
* `run_bench.py` writes predictions in the official GraphRAG-Bench format and scores them with the official   protocol (rationale / answer / AR score).
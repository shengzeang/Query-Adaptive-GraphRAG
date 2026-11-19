#!/usr/bin/env bash
# Reproduce the main experiments of RAPTOR-QA (paper Tables 4 and 5).
#
# LLM roles (all OpenAI-compatible endpoints, see .env.example):
#   answering + RAPTOR summaries : Qwen2.5-7B-Instruct served locally by vLLM (the paper's backbone).
#                                  One replica per GPU (default 8 x V100 32G), requests are spread round-robin.
#   GraphRAG-Bench judge         : DeepSeek flash (official evaluation protocol), key from DEEPSEEK_API_KEY
#
#   bash scripts/run_all.sh serve             # 0. start GPUS vLLM replicas (ports 8000..8007), waits until ready
#   export DEEPSEEK_API_KEY=sk-...            # only needed by the `check` and `bench` stages
#   bash scripts/run_all.sh check             # 1. connectivity check of every endpoint
#   SMOKE=1 bash scripts/run_all.sh all       # 2. tiny end-to-end run to validate the pipeline
#   bash scripts/run_all.sh all               # 3. the full experiments
#   bash scripts/run_all.sh stop              # 4. stop the vLLM replicas
#
# Stages (run any subset, in order):  serve stop check labels train kgqa bench_index bench | all
#   serve       launch the vLLM replicas (not part of `all`; idempotent)
#   labels      router training data: 2000 questions each of HotpotQA(train) / NQ / TriviaQA, answered from every level
#   train       Generalist router (HotpotQA + NQ + TriviaQA)
#   kgqa        Table 4: BM25 / TF-IDF / RAPTOR / RAPTOR-QA on MuSiQue, 2WikiMQA, HotpotQA
#   bench_index shared RAPTOR tree over the 20 GraphRAG-Bench textbooks (chunks of $BENCH_CHUNK tokens, default 200;
#               BENCH_CHUNK=1200 for the GraphRAG-Bench paper's size: cluster cap, context budget and the
#               replicas' context window (VLLM_MAX_LEN, set when BENCH_CHUNK is exported for `serve` too) follow it)
#   bench       Table 5: generation for FB/MC/MS/TF/OE + official scoring (judge = DeepSeek flash)
#
# Common switches (environment variables; see the comments below and README.md):
#   RETRIEVAL=collapse|traverse   how raptor / raptor-qa retrieve (default collapse); labels, checkpoints and results depend on it
#   TOP_K=5                       nodes per layer (traverse) / in total (collapse, BM25, TF-IDF); same dependency as RETRIEVAL
#   DATA / CKPT / OUT_KGQA / OUT_BENCH   directories of labels / checkpoints / KGQA results / bench results
#   KGQA_METHODS / KGQA_ROUTERS   restrict the kgqa stage, e.g. RAPTOR and RAPTOR-QA only: KGQA_METHODS="raptor raptor-qa"
#                                 (KGQA_ROUTERS: name=checkpoint pairs, default generalist=$CKPT/generalist.pt)
#   BENCH_CHUNK=200               GraphRAG-Bench chunk size in tokens (1200 = the benchmark paper's size)
#   BENCH_METHODS / BENCH_ROUTERS / BENCH_TASKS   restrict the bench stage (methods, name=ckpt routers, tasks FB MC MS TF OE)
#   ENCODER_DEVICE=cpu            put the sentence encoder on the CPU (e.g. CUDA OOM next to a vLLM replica)
#   SMOKE=1                       tiny end-to-end run, outputs under *_smoke/
#
# Performance layout (8 GPUs, 64 CPU cores; every knob below can be overridden through the environment):
#   * GPU: one independent vLLM replica per GPU (tensor parallelism is pointless for a 7B model that fits in 32 GB
#     and would only add NVLink/PCIe traffic). BACKBONE_BASE_URL becomes "http://localhost:8000/v1,...:8007/v1".
#   * CPU: RAPTOR tree building (UMAP + GMM) is CPU-bound. `labels` and `kgqa` therefore run SHARDS
#     processes on disjoint slices of the questions (one per GPU for the sentence encoder), followed by one final
#     unsharded pass that retries failures and writes the summaries.
#
# V100 notes (compute capability 7.0: no bf16, no FlashAttention-2, no FP8, and NO prefix caching / chunked prefill:
# their Triton kernel fails to compile on Volta and kills the engine, so neither flag is passed): vLLM runs with --dtype half and the
# V0 engine (VLLM_USE_V1=0), the last engine that supports Volta, e.g. `pip install vllm==0.9.2 transformers==4.53.2`.
# This setup comes from the vLLM docs/issues and was NOT tested on a V100 here. If your vLLM build differs, change
# VLLM_CMD / VLLM_ENV / VLLM_EXTRA_ARGS (e.g. a Volta fork) instead of editing this file.
#
# Every stage is resumable: re-running skips finished questions and cached trees. Logs go to logs/.
# Other backbones: BACKBONE_BASE_URL / BACKBONE_MODEL / BACKBONE_API_KEY (and SUMMARIZER_* to use a different
# model for the summaries) are respected, e.g. a larger Qwen served by vLLM or any hosted OpenAI-compatible API.
set -euo pipefail
cd "$(dirname "$0")/.."

[[ $# -eq 0 ]] && { awk 'NR>1 && /^#/ {print; next} NR>1 {exit}' "$0"; exit 0; }

# ------------------------------------------------------------------ configuration (override via env)
STAGES=("$@")
[[ "${STAGES[0]}" == "all" ]] && STAGES=(check labels train kgqa bench_index bench)
for s in "${STAGES[@]}"; do   # the DeepSeek key is only needed by the stages that call the judge
  if [[ "$s" == "check" || "$s" == "bench" ]]; then
    : "${DEEPSEEK_API_KEY:?stage $s needs the judge: export DEEPSEEK_API_KEY=...}"
  fi
done

GPUS="${GPUS:-8}"                          # number of local vLLM replicas (one per GPU)
VLLM_BASE_PORT="${VLLM_BASE_PORT:-8000}"
default_urls() { local i out=""; for ((i = 0; i < GPUS; i++)); do out+="${out:+,}http://localhost:$((VLLM_BASE_PORT + i))/v1"; done; echo "$out"; }

export BACKBONE_BASE_URL="${BACKBONE_BASE_URL:-$(default_urls)}"   # comma-separated = several replicas
export BACKBONE_MODEL="${BACKBONE_MODEL:-Qwen/Qwen2.5-7B-Instruct}"
export BACKBONE_API_KEY="${BACKBONE_API_KEY:-EMPTY}"
export JUDGE_BASE_URL="${JUDGE_BASE_URL:-https://api.deepseek.com}"
export JUDGE_MODEL="${JUDGE_MODEL:-deepseek-flash}"
PY="${PY:-python}"
CORES="$(nproc 2>/dev/null || echo 8)"
BENCH_CHUNK="${BENCH_CHUNK:-200}"    # chunk size (tokens) of the GraphRAG-Bench tree; the KGQA / router trees use 100
# TOP_K: nodes kept per layer by tree traversal, and in total by the collapsed tree / BM25 / TF-IDF (default 5, the value of the
# first experiments). It changes the router labels, so labels / checkpoints / results of another TOP_K need their own DATA, CKPT,
# OUT_KGQA and OUT_BENCH (the scripts refuse to mix them); the cached trees do not depend on it.
TOP_K="${TOP_K:-5}"
# context budget of the bench runs: room for TOP_K leaves of BENCH_CHUNK tokens plus 2 x TOP_K summaries (~100 tokens each) and some
# slack, never below the KGQA 3500 (TOP_K=5, BENCH_CHUNK=1200 -> 7500 tokens; TOP_K=10 -> 14500)
BENCH_MAX_TOKENS="${BENCH_MAX_TOKENS:-$(( TOP_K * (BENCH_CHUNK + 200) + 500 > 3500 ? TOP_K * (BENCH_CHUNK + 200) + 500 : 3500 ))}"

# vLLM replica settings. Qwen2.5-7B fp16 = ~15 GB. vLLM 0.6.x was measured to occupy ~29.4 GiB of a 31.75 GiB V100 at a
# requested 0.88, i.e. ~4.5% more than requested (graphs/context), which left too little for the sentence-encoder
# processes on the same card (CUDA out of memory). At 0.78 the card has ~6 GiB free and still ~7 GB of KV cache (~57
# KB/token, >100k tokens, enough for 64 sequences of 1-2k tokens). Several encoders per GPU (BENCH_SHARDS > 8)
# need ~2.3 GiB each: lower VLLM_GPU_UTIL further or set ENCODER_DEVICE=cpu.
# VLLM_MAX_LEN: 8192, or 16384 for large GraphRAG-Bench chunks (BENCH_CHUNK > 300: summaries of 8 chunks, contexts of
# 5 chunks + summaries), or 32768 (the most Qwen2.5 supports) when the bench context budget (+25% for the served model
# counting more tokens than the retriever, + the prompt and the answer) does not fit 16384, e.g. TOP_K=10 with BENCH_CHUNK=1200.
# Replicas that are already up keep their old value: `stop` them before `serve`.
VLLM_CMD="${VLLM_CMD:-vllm serve}"
VLLM_ENV="${VLLM_ENV:-VLLM_USE_V1=0}"
VLLM_MAX_LEN="${VLLM_MAX_LEN:-$(( BENCH_MAX_TOKENS * 5 / 4 + 1500 > 16384 ? 32768 : (BENCH_CHUNK > 300 ? 16384 : 8192) ))}"
VLLM_MAX_SEQS="${VLLM_MAX_SEQS:-64}"
VLLM_GPU_UTIL="${VLLM_GPU_UTIL:-0.78}"
VLLM_EXTRA_ARGS="${VLLM_EXTRA_ARGS:-}"
VLLM_WAIT_S="${VLLM_WAIT_S:-1200}"

# Sharded stages: SHARDS processes x WORKERS concurrent questions each. Every question issues a few (labels: up to
# dozens, for the summaries of one tree layer) concurrent requests, so the replicas stay saturated.
if [[ "${SMOKE:-0}" == "1" ]]; then SHARDS="${SHARDS:-2}"; else SHARDS="${SHARDS:-$GPUS}"; fi
WORKERS="${WORKERS:-8}"                          # questions in flight per shard process
BENCH_WORKERS="${BENCH_WORKERS:-$((GPUS * 32))}" # bench generation is a single process: only light CPU work per question
JUDGE_WORKERS="${JUDGE_WORKERS:-64}"
# Clustering (UMAP/numba) would otherwise start one thread per core in every process. Thread budget (not
# benchmarked; raise it if the CPU is idle during the run):
THREADS="${THREADS:-$(( CORES / SHARDS / 2 > 0 ? CORES / SHARDS / 2 : 1 ))}"   # per shard process
export NUMBA_NUM_THREADS="$THREADS" OMP_NUM_THREADS="$THREADS" MKL_NUM_THREADS="$THREADS" OPENBLAS_NUM_THREADS="$THREADS"
# bench_index: one shard per textbook (20), or 1 in SMOKE mode (a single textbook); threads = cores / shards
if [[ "${SMOKE:-0}" == "1" ]]; then BENCH_SHARDS="${BENCH_SHARDS:-1}"; else BENCH_SHARDS="${BENCH_SHARDS:-20}"; fi
BENCH_THREADS="${BENCH_THREADS:-$(( CORES / BENCH_SHARDS > 0 ? CORES / BENCH_SHARDS : 1 ))}"

export HF_HUB_DISABLE_PROGRESS_BARS=1 TOKENIZERS_PARALLELISM=false

if [[ "${SMOKE:-0}" == "1" ]]; then
  N_ROUTER=24; N_TEST=10; BENCH_LIMIT=3; BENCH_TEXTBOOKS="--textbooks 5"; EPOCHS=20
  RUN=smoke; echo ">>> SMOKE mode: tiny sizes, outputs under *_smoke/"
else
  N_ROUTER=2000; N_TEST=1000; BENCH_LIMIT=""; BENCH_TEXTBOOKS=""; EPOCHS=100
  RUN=""
fi
suffix() { [[ -n "$RUN" ]] && echo "_$RUN" || true; }
# DATA / CKPT / OUT_KGQA / OUT_BENCH can be overridden, e.g. CKPT=checkpoints_t10 OUT_BENCH=outputs/bench_t10_c1200
# RETRIEVAL (also read by the python code): how raptor / raptor-qa retrieve, collapse (default) | traverse (the first experiments);
# one output directory must not mix them either (bm25 / tfidf rows are not affected). The router labels (`labels`),
# the checkpoints and the KGQA results depend on it too: with the default (collapse) they go to their own directories, e.g.
#   DATA=data/router_collapse CKPT=checkpoints_collapse OUT_KGQA=outputs/kgqa_collapse bash scripts/run_all.sh labels train kgqa
# (the cached trees in $IDX do not depend on it and are reused: only the answers are generated again)
DATA="${DATA:-data/router$(suffix)}"; CKPT="${CKPT:-checkpoints$(suffix)}"; IDX="indexes$(suffix)"
OUT_KGQA="${OUT_KGQA:-outputs/kgqa$(suffix)}"; OUT_BENCH="${OUT_BENCH:-outputs/bench$(suffix)}"
BENCH_TREE="$IDX/graphrag_bench_c${BENCH_CHUNK}.pkl"
LIMIT_ARG=""; [[ -n "$BENCH_LIMIT" ]] && LIMIT_ARG="--limit $BENCH_LIMIT"
# BENCH_TASKS="TF" (or "TF MC"): generate and score only these bench tasks (default: all five)
TASKS_ARG=""; [[ -n "${BENCH_TASKS:-}" ]] && TASKS_ARG="--tasks $BENCH_TASKS"
mkdir -p logs "$DATA" "$CKPT" "$IDX"
log() { echo; echo "=================== $* ($(date -u '+%F %T') UTC)"; }

# run_sharded <log-name> <command...>: the command must accept --shard i/N. Starts SHARDS copies in parallel
# (shard i pinned to GPU i for its sentence encoder), then runs it once more without --shard to retry failures
# and to produce the summaries.
run_sharded() {
  local name="$1"; shift
  if (( SHARDS > 1 )); then
    local pids=() i rc=0
    for ((i = 0; i < SHARDS; i++)); do
      CUDA_VISIBLE_DEVICES=$((i % GPUS)) "$@" --shard "$i/$SHARDS" >> "logs/$name.shard$i.log" 2>&1 &
      pids+=($!)
    done
    echo "$SHARDS shards running, progress: tail -f logs/$name.shard*.log"
    for p in "${pids[@]}"; do wait "$p" || rc=1; done
    (( rc == 0 )) || echo "WARNING: some shards failed, see logs/$name.shard*.log (the final pass retries them)"
  fi
  "$@" 2>&1 | tee -a "logs/$name.log"
}

# ------------------------------------------------------------------ stages
stage_serve() {
  log "serve: $GPUS vLLM replicas of $BACKBONE_MODEL on ports $VLLM_BASE_PORT..$((VLLM_BASE_PORT + GPUS - 1))"
  local i port
  for ((i = 0; i < GPUS; i++)); do
    port=$((VLLM_BASE_PORT + i))
    if curl -sf --noproxy '*' "http://localhost:$port/v1/models" >/dev/null 2>&1; then echo "replica $i already up"; continue; fi
    # shellcheck disable=SC2086
    env CUDA_VISIBLE_DEVICES=$i $VLLM_ENV nohup $VLLM_CMD "$BACKBONE_MODEL" --port "$port" --dtype half \
        --max-model-len "$VLLM_MAX_LEN" --max-num-seqs "$VLLM_MAX_SEQS" --gpu-memory-utilization "$VLLM_GPU_UTIL" \
        $VLLM_EXTRA_ARGS > "logs/vllm_$i.log" 2>&1 &
    echo $! > "logs/vllm_$i.pid"
  done
  # --noproxy: a proxy in the environment must not intercept the local health check
  local waited=0
  for ((i = 0; i < GPUS; i++)); do
    port=$((VLLM_BASE_PORT + i))
    until curl -sf --noproxy '*' "http://localhost:$port/v1/models" >/dev/null 2>&1; do
      if [[ -e "logs/vllm_$i.pid" ]] && ! kill -0 "$(cat "logs/vllm_$i.pid")" 2>/dev/null; then
        echo "replica $i (GPU $i) exited during startup, last log lines:"; tail -n 15 "logs/vllm_$i.log"; exit 1
      fi
      if (( waited >= VLLM_WAIT_S )); then echo "replica $i not ready after ${VLLM_WAIT_S}s, see logs/vllm_$i.log"; exit 1; fi
      (( waited % 30 == 0 )) && echo "  waiting for replica $i ... ${waited}s (loading model / capturing CUDA graphs; tail -f logs/vllm_$i.log)"
      sleep 5; waited=$((waited + 5))
    done
    echo "replica $i ready (port $port)"
  done
}

stage_stop() {
  log "stop: vLLM replicas"
  local f
  for f in logs/vllm_*.pid; do
    [[ -e "$f" ]] || continue
    kill "$(cat "$f")" 2>/dev/null || true
    rm -f "$f"
  done
}

stage_check() {
  log "check: endpoints and thinking mode"
  $PY - <<'EOF'
import time
from qa_graphrag.llm import ChatLLM
for role in ("backbone", "judge"):
    llm = ChatLLM.from_role(role)
    for client in llm.clients:
        t = time.time()
        r = client.chat.completions.create(
            model=llm.spec.model, max_tokens=64, temperature=0,
            messages=[{"role": "user", "content": "Reply with the single word: ready"}], extra_body=llm.spec.extra_body)
        u = r.usage
        reasoning = getattr(r.choices[0].message, "reasoning_content", None)
        print(f"{role:9s} {client.base_url} model={llm.spec.model} extra_body={llm.spec.extra_body} -> "
              f"{r.choices[0].message.content!r} ({u.prompt_tokens} in / {u.completion_tokens} out, {time.time()-t:.1f}s)")
        assert not reasoning, "thinking mode is ON: output tokens would be billed for reasoning"
EOF
}

stage_labels() {
  for src in hotpotqa nq triviaqa; do
    log "labels: $src ($N_ROUTER questions x 3 levels, top-k $TOP_K, $SHARDS shards)"
    run_sharded "labels_$src" $PY scripts/gen_router_data.py --source "$src" --n "$N_ROUTER" --out "$DATA/$src.jsonl" \
        --cache-dir "$IDX" --workers "$WORKERS" --top-k "$TOP_K"
  done
}

stage_train() {
  log "train: Generalist router (HotpotQA + NQ + TriviaQA)"
  $PY scripts/train_router.py --data "$DATA"/hotpotqa.jsonl "$DATA"/nq.jsonl "$DATA"/triviaqa.jsonl \
      --epochs "$EPOCHS" --out "$CKPT/generalist.pt" 2>&1 | tee logs/train_generalist.log
}

stage_kgqa() {
  # KGQA_METHODS / KGQA_ROUTERS: default all four methods with the Generalist router (from the `train` stage); e.g.
  # KGQA_METHODS="raptor raptor-qa" for RAPTOR and RAPTOR-QA only. KGQA_ROUTERS: name=checkpoint pairs.
  local methods="${KGQA_METHODS:-bm25 tfidf raptor raptor-qa}"
  local routers="${KGQA_ROUTERS:-generalist=$CKPT/generalist.pt}"
  local d
  for d in musique 2wikimqa hotpotqa; do
    log "kgqa (Table 4): $d (methods: $methods; top-k $TOP_K, $SHARDS shards)"
    # shellcheck disable=SC2086
    run_sharded "kgqa_$d" $PY scripts/run_kgqa.py --dataset "$d" --n "$N_TEST" \
        --methods $methods --routers $routers \
        --cache-dir "$IDX" --workers "$WORKERS" --top-k "$TOP_K" --out "$OUT_KGQA"
  done
}

stage_bench_index() {
  # One process per textbook: the trees of different books are independent, the clustering (GMM/BIC search) is
  # mostly single-threaded, and the books differ 4x in size, so more processes balance better than more threads.
  log "bench_index: RAPTOR tree over the GraphRAG-Bench textbooks ($BENCH_SHARDS shards x $BENCH_THREADS threads; the final pass merges the cached trees)"
  (
    export NUMBA_NUM_THREADS="$BENCH_THREADS" OMP_NUM_THREADS="$BENCH_THREADS" MKL_NUM_THREADS="$BENCH_THREADS" OPENBLAS_NUM_THREADS="$BENCH_THREADS"
    SHARDS="$BENCH_SHARDS"
    # shellcheck disable=SC2086
    run_sharded bench_index $PY scripts/build_bench_index.py --out "$BENCH_TREE" --cache-dir "$IDX" \
        --chunk-tokens "$BENCH_CHUNK" --workers "$WORKERS" $BENCH_TEXTBOOKS
  )
}

stage_bench() {
  log "bench (Table 5): generation + official scoring (chunks of $BENCH_CHUNK tokens, top-k $TOP_K, context budget $BENCH_MAX_TOKENS tokens)"
  # BENCH_METHODS: default all four; BENCH_METHODS=raptor-qa with BENCH_ROUTERS="a=ckpt/a.pt b=ckpt/b.pt" compares routers
  # (each becomes its own raptor-qa[name] directory; bm25 / tfidf / raptor are not run again)
  local methods="${BENCH_METHODS:-bm25 tfidf raptor raptor-qa}"
  local routers="${BENCH_ROUTERS:-generalist=$CKPT/generalist.pt}"
  # shellcheck disable=SC2086
  $PY scripts/run_bench.py --tree "$BENCH_TREE" --methods $methods \
      --routers $routers --out "$OUT_BENCH" $LIMIT_ARG $TASKS_ARG --top-k "$TOP_K" \
      --max-tokens "$BENCH_MAX_TOKENS" \
      --workers "$BENCH_WORKERS" --judge-workers "$JUDGE_WORKERS" 2>&1 | tee -a logs/bench.log
}

# ------------------------------------------------------------------ dispatch
for s in "${STAGES[@]}"; do
  case "$s" in
    serve|stop|check|labels|train|kgqa|bench_index|bench) "stage_$s" ;;
    *) echo "unknown stage: $s"; exit 2 ;;
  esac
done
log "done: ${STAGES[*]}"
echo "summaries: $OUT_KGQA/*_summary.json  $OUT_BENCH/summary.json"

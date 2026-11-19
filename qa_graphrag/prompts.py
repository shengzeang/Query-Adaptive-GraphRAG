"""All prompts in one place.

KGQA: step-by-step reasoning and a final ``ANSWER:`` (only the answer is scored), the context described as a mix of
passages and summaries. GraphRAG-Bench: prompts written after reading the benchmark's questions and gold answers.

Router labels, KGQA results and GraphRAG-Bench predictions are only comparable for one prompt (the labels are the accuracy
of this very prompt), so the scripts record ``PROMPT_VERSION`` in every row and refuse to mix versions in one output file
(rows without it were made by an older prompt).
"""
import re
from typing import Dict, Optional

PROMPT_VERSION = "v2"

_CONTEXT_NOTE = (
    "The context was retrieved from a document collection and mixes original text passages with summary nodes that "
    "condense several passages. Summaries can leave out or blur details: when a summary and a passage disagree, trust "
    "the passage."
)

KGQA_PROMPT = (
    "Answer the question based on the given context. " + _CONTEXT_NOTE + "\n"
    "Many questions need more than one fact (for example: first find the entity the question refers to, then look up "
    "the requested property of it), so reason step by step before you answer. If the context does not settle the "
    "question, still give your best guess.\n\n"
    "Use exactly this format:\n"
    "REASONING: <the relevant facts from the context and how they lead to the answer, at most three short sentences>\n"
    "ANSWER: <only the answer, as short as possible (a few words), without any explanation>\n\n"
    "Context:\n{context}\n\n"
    "Question: {question}\n"
)

_ANSWER_TAG = re.compile(r"ANSWER\s*:", re.IGNORECASE)
MAX_UNTAGGED_WORDS = 30


def extract_final_answer(text: str) -> str:
    """The answer of a ``KGQA_PROMPT`` response: the first non-empty line after the last ``ANSWER:``.

    The KGQA accuracy is "the gold answer is a substring of the prediction", so the reasoning must never be part of the
    scored text. A response without the tag (cut off while reasoning, or the format was ignored) counts as the whole text
    only if it is short and has no reasoning in it, otherwise it is an empty answer (kept in the raw output)."""
    parts = _ANSWER_TAG.split(text)
    if len(parts) > 1:
        for line in parts[-1].strip().splitlines():
            line = line.strip().strip("*_`\"' ")
            if line:
                return line
        return ""
    if re.search(r"REASONING\s*:", text, re.IGNORECASE) or len(text.split()) > MAX_UNTAGGED_WORDS:
        return ""
    return text.strip()


# ------------------------------------------------------------------------------------------------ GraphRAG-Bench
# The official evaluator parses a response of the form "... RATIONALE: <text> ANSWER: <answer>" and takes the first line
# after "ANSWER:".
# Written after reading the dataset (questions and gold answers: questions/{FB,MC,MS,TF,OE}.jsonl). What the gold data and the
# scoring ask for:
#   * the gold rationale is one or two sentences that state the principle behind the answer ("The dot operator is used in
#     Java to access an object's methods ..."), never a comparison of the options; the judge scores the predicted rationale
#     0 / 0.5 / 1 against it, so a longer rationale with extra claims risks "includes incorrect information";
#   * MC and TF are scored by exact string equality ("C", "True"): any punctuation or extra word makes the answer wrong;
#   * MS is the set of the letters ("ACD"): the evaluator splits the string into characters, so a separator or a space
#     is a wrong option; an exact set scores 1, a subset 0.5, anything else 0 (2 to 4 of the 4 options are correct);
#   * FB gold answers are one or two words ("method", "dot", "data types"), OE gold answers one or two sentences.
_BENCH_INTRO = (
    "You are answering a question about a university-level textbook. " + _CONTEXT_NOTE + " Base your answer on the "
    "context; use your own knowledge of the subject only where the context is silent.\n"
)
_BENCH_HEAD = (
    "Think the question through before you answer, then write it down as the rationale: one or two sentences that state "
    "the key fact, definition or rule that makes the answer correct and apply it to the question. Do not repeat the "
    "question, do not refer to \"the context\", \"the passages\" or \"the summaries\", and do not hedge. Then give the "
    "final answer, using exactly this format (the answer on the same line as ANSWER:, with nothing else after it). "
    "Always fill in the ANSWER, even when the context does not help: give your best answer, never leave it empty:\n"
    "RATIONALE: <one or two sentences>\nANSWER: {answer_format}\n\n"
)
# TF only: the same head without "do not hedge" and without "always fill in the ANSWER ... give your best answer". With
# them the model answered False far more often than the gold data does (raptor: 69% False against 52%), because it
# turned a context that does not settle the statement into "False".
_BENCH_HEAD_TF = (
    "Think the question through before you answer, then write it down as the rationale: one or two sentences that state "
    "the key fact, definition or rule that makes the answer correct and apply it to the question. Do not repeat the "
    "question and do not refer to \"the context\", \"the passages\" or \"the summaries\". Then give the final answer, "
    "using exactly this format (the answer on the same line as ANSWER:, with nothing else after it):\n"
    "RATIONALE: <one or two sentences>\nANSWER: {answer_format}\n\n"
)
BENCH_TASK_INSTRUCTION: Dict[str, str] = {
    "FB": (
        "The question is a sentence with one or more blanks (____). The answer is just the missing term, usually one or "
        "two words, in the wording the textbook uses; for several blanks give the terms in order, separated by commas."
    ),
    "MC": (
        "The question is a multiple-choice question with exactly one correct option. Check every option against the "
        "context before you choose."
    ),
    "MS": (
        "The question is a multiple-select question: usually two to four of the four options are correct. Judge every "
        "option on its own against the context. Include an option only when it is supported: leaving out a correct "
        "option costs less than including a wrong one."
    ),
    "TF": (
        "The question is a true-or-false statement. Decide whether the statement is true or false according to the "
        "textbook, weighing the evidence for and against it."
    ),
    "OE": (
        "The question is open-ended. The answer is a direct, complete reply of one or two sentences that uses the terms "
        "of the textbook and covers every part the question asks for."
    ),
}
BENCH_ANSWER_FORMAT: Dict[str, str] = {
    "FB": "<the missing term only>",
    "MC": "<one option letter only, for example B; no colon, no period, no brackets, no option text>",
    "MS": "<the correct option letters in alphabetical order, with no spaces or separators, e.g. ACD>",
    "TF": "<True or False, nothing else; no period>",
    "OE": "<the answer, one or two sentences, all on this single line>",
}

_BENCH_HEAD_BY_TASK = {"TF": _BENCH_HEAD_TF}
_BENCH_TAIL = "Context:\n{context}\n\nQuestion: {query}\n"

BENCH_MAX_NEW_TOKENS: Dict[str, int] = {"FB": 256, "MC": 256, "MS": 256, "TF": 256, "OE": 512}


def build_bench_query(task: str, example: Dict) -> str:
    """The text that is embedded for routing/retrieval: the question plus its options."""
    q = example["Question"].strip()
    choices: Optional[Dict[str, str]] = example.get("Choices")
    if choices:
        q += "\nChoices:\n" + "\n".join(f"{k}: {v}" for k, v in choices.items())
    return q


def build_bench_prompt(task: str, example: Dict, context: str) -> str:
    head = _BENCH_INTRO + BENCH_TASK_INSTRUCTION[task] + "\n"
    head += _BENCH_HEAD_BY_TASK.get(task, _BENCH_HEAD).format(answer_format=BENCH_ANSWER_FORMAT[task])
    return head + _BENCH_TAIL.format(context=context, query=build_bench_query(task, example))

import json
import os
from tqdm import tqdm
import re
from collections import Counter

def load_model_outputs(base_path):
    model_predictions = {}

    for model_folder in os.listdir(base_path):
        model_folder_path = base_path#os.path.join(base_path, model_folder)

        if os.path.isdir(model_folder_path):
            predictions = {}
            for file_name in ["GraphRAG-Bench_FB", "GraphRAG-Bench_MC", "GraphRAG-Bench_MS", "GraphRAG-Bench_OE", "GraphRAG-Bench_TF"]:
                file_path = os.path.join(model_folder_path, file_name + ".json")

                if os.path.exists(file_path):
                    with open(file_path, 'r',encoding="utf-8",errors="ignore") as f:
                        # data = json.load(f)
                        # 修改了
                        try:
                            data = json.load(f)
                        except json.JSONDecodeError as e:
                            print(f"JSON 解析错误: {e}")
                            print(f"错误位置: {e.lineno} 行, {e.colno} 列")
                        prediction_list = []
                        for key, value in data.items():
                            prediction_dict = {
                                "prediction": value["prediction"],
                                "idx": int(key)
                            }
                            prediction_list.append(prediction_dict)

                        predictions[file_name.split('_')[-1]] = prediction_list

            model_predictions[model_folder] = predictions

    return model_predictions

def load_original_data(original_path):
    original_data = {}

    for file_name in ["FB", "MC", "MS", "OE", "TF"]:
        file_path = os.path.join(original_path, file_name + ".jsonl")

        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                original_data[file_name] = [json.loads(line.strip()) for line in f]

    return original_data

def extract_feature(text, type_):
    # keep behavior: return the extracted answer (string) after 'ANSWER:'
    if "Please answer the following" in text:
        text = text.split("Please answer the following")[0].strip()

    '''parts = text.split("Answer:")
    if len(parts) < 2:
        return ""

    answer = parts[1].strip().split('\n')[0]'''

    if type_ == "OE":
        answer = text.strip()
    else:
        answer = text.strip().split('\n')[0]
    return answer

def post_processor(original_data, prediction, question_type):
    merged_data = {type_: [] for type_ in question_type}

    for type_ in question_type:

            def normalize_predict_answer(raw_pred, gold_answer):
                # If gold is a list, we expect predict to be a list too (MS). Try to parse.
                if isinstance(gold_answer, list):
                    # If it's already a list, return as-is
                    if isinstance(raw_pred, list):
                        return raw_pred

                    raw = raw_pred if isinstance(raw_pred, str) else str(raw_pred)
                    raw = raw.strip()
                    # Try JSON list
                    try:
                        parsed = json.loads(raw)
                        if isinstance(parsed, list):
                            return [str(x).strip() for x in parsed]
                    except Exception:
                        pass

                    # Split by comma or semicolon
                    if ',' in raw:
                        parts = [p.strip() for p in raw.split(',') if p.strip()]
                        if parts:
                            return parts
                    if ';' in raw:
                        parts = [p.strip() for p in raw.split(';') if p.strip()]
                        if parts:
                            return parts

                    # Fallback to single-element list (or empty if blank)
                    return [raw] if raw != '' else []

                # otherwise return as-is (string)
                return raw_pred

            merged_data[type_] = [
                {
                    "predict_answer": normalize_predict_answer(extract_feature(pred["prediction"], type_), orig["Answer"]),
                    "answer": orig["Answer"],
                    "topic": orig["Level-1 Topic"]
                }
                for orig, pred in zip(original_data[type_], prediction[type_])
            ]

    return merged_data

# Rationale evaluation removed. We only evaluate answers now.

def open_ended_calculator(pred_answer, gold_answer):
    # Local token-level F1 scorer for open-ended answers.
    def token_f1(a, b):
        if a is None:
            a = ""
        if b is None:
            b = ""
        # simple whitespace tokenizer and lowercase
        ta = [t for t in re.split(r"\s+", str(a).strip().lower()) if t]
        tb = [t for t in re.split(r"\s+", str(b).strip().lower()) if t]
        if not ta and not tb:
            return 1.0
        if not ta or not tb:
            return 0.0
        ca = Counter(ta)
        cb = Counter(tb)
        common = sum((ca & cb).values())
        if common == 0:
            return 0.0
        precision = common / sum(ca.values())
        recall = common / sum(cb.values())
        if precision + recall == 0:
            return 0.0
        f1 = 2 * precision * recall / (precision + recall)
        return float(f1)

    try:
        return float(token_f1(pred_answer, gold_answer))
    except Exception:
        return 0.0


def em_calculator(data):
    eval_data = []

    for item in data:
        # Only compute answer score
        if item["predict_answer"] == item["answer"]:
            answer_score = 1.0
        else:
            answer_score = 0.0

        item["answer_score"] = answer_score
        eval_data.append(item)

    return eval_data


def ms_calculator(data):
    eval_data = []

    for item in data:
        # Only compute answer score (multi-select)
        correct_answers = set(item["answer"])
        parsed_answers = set(item["predict_answer"])
        predicted_answers = []
        for ans in parsed_answers:
            if ans in ['A', 'B', 'C', 'D']:
                predicted_answers.append(ans)
        predicted_answers = set(predicted_answers)

        if predicted_answers == correct_answers:
            answer_score = 1.0
        elif predicted_answers.issubset(correct_answers):
            answer_score = 0.5
        else:
            answer_score = 0.0

        item["answer_score"] = answer_score
        eval_data.append(item)

    return eval_data

def oe_calculator(data):
    eval_data = []

    for item in data:
        # print(item)
        # Only compute answer score for open-ended
        answer_score = open_ended_calculator(pred_answer=item["predict_answer"],
                                             gold_answer=item["answer"])

        item["answer_score"] = answer_score
        eval_data.append(item)

    return eval_data

def evaluator(type_, data):

    if type_ == "MC" or type_ == "TF":
        eval_data = em_calculator(data)
    elif type_ == "MS":
        eval_data = ms_calculator(data)
    elif type_ == "OE" or type_ == "FB":
        eval_data = oe_calculator(data)
    else:
        print("Type Error")
        eval_data = []

    return eval_data

def calculate_ar_score(answer_score, rationale_score=None):
    # With rationale removed, AR score equals answer score
    return float(answer_score)

def run_eval(origin_data, prediction, question_type):
    merged_data = post_processor(origin_data, prediction, question_type)

    results = {
        "total": {"answer_score": 0.0, "ar_score": 0.0, "count": 0},
        "by_type": {type_: {"answer_score": 0.0, "ar_score": 0.0, "count": 0} for type_ in question_type},
        "by_topic": {}
    }

    for type_ in tqdm(question_type, desc="Evaluating different question types"):
        eval_data = evaluator(type_, merged_data[type_])

        for item in eval_data:
            answer_score = item["answer_score"]

            results["total"]["answer_score"] += answer_score
            ar_score = calculate_ar_score(answer_score)
            results["total"]["ar_score"] += ar_score
            results["total"]["count"] += 1

            results["by_type"][type_]["answer_score"] += answer_score
            results["by_type"][type_]["ar_score"] += ar_score
            results["by_type"][type_]["count"] += 1

            topic = item.get("topic")
            if topic not in results["by_topic"]:
                results["by_topic"][topic] = {"answer_score": 0.0, "ar_score": 0.0, "count": 0}
            results["by_topic"][topic]["answer_score"] += answer_score
            results["by_topic"][topic]["ar_score"] += ar_score
            results["by_topic"][topic]["count"] += 1

    if results["total"]["count"] > 0:
        results["total"]["answer_score"] /= results["total"]["count"]
        results["total"]["ar_score"] /= results["total"]["count"]

    for type_ in results["by_type"]:
        if results["by_type"][type_]["count"] > 0:
            results["by_type"][type_]["answer_score"] /= results["by_type"][type_]["count"]
            results["by_type"][type_]["ar_score"] /= results["by_type"][type_]["count"]

    for topic in results["by_topic"]:
        if results["by_topic"][topic]["count"] > 0:
            results["by_topic"][topic]["answer_score"] /= results["by_topic"][topic]["count"]
            results["by_topic"][topic]["ar_score"] /= results["by_topic"][topic]["count"]

    return results

if __name__ == "__main__":

    question_type = ["FB", "MC", "MS", "OE", "TF"]
    # question_type = ["FB"]

    original_path = "./inputs/graphrag-bench/"
    original_data = load_original_data(original_path)

    base_path = "./outputs"
    predictions = load_model_outputs(base_path)

    output_file_path = "./sample_output.json"

    with open(output_file_path, 'r', encoding='utf-8',errors="ignore") as outfile:
        data = json.load(outfile)

    for model_name, prediction in tqdm(predictions.items(), desc="Evaluating Models", unit="model"):

        if model_name in data:
            print(f"Skipping {model_name}, already evaluated.")
            continue

        # print(prediction)
        results = run_eval(original_data, prediction, question_type)

        data[model_name] = results

        with open(output_file_path, 'w') as outfile:
            json.dump(data, outfile)

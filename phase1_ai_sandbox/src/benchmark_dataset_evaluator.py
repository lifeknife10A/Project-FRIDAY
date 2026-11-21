"""
PROJECT FRIDAY: STANDARDIZED BENCHMARK DATASET EVALUATION ENGINE
Audits full-text CER and WER without stripping punctuation, key-field exact match,
safety entity verification, and category-level disaggregation.
"""

import os
import json
import numpy as np

import re

def compute_levenshtein(s1: str, s2: str) -> int:
    """Exact Levenshtein distance between two sequences (characters or words)."""
    if len(s1) < len(s2):
        return compute_levenshtein(s2, s1)
    if len(s2) == 0:
        return len(s1)

    previous_row = range(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]

def compute_cer(reference: str, hypothesis: str) -> float:
    """Character Error Rate WITHOUT stripping punctuation."""
    ref = reference.strip()
    hyp = hypothesis.strip()
    if not ref:
        return 0.0 if not hyp else 1.0
    dist = compute_levenshtein(ref, hyp)
    return min(1.0, dist / len(ref))

def compute_wer(reference: str, hypothesis: str) -> float:
    """Word Error Rate WITHOUT stripping punctuation."""
    ref_words = reference.strip().split()
    hyp_words = hypothesis.strip().split()
    if not ref_words:
        return 0.0 if not hyp_words else 1.0
    dist = compute_levenshtein(ref_words, hyp_words)
    return min(1.0, dist / len(ref_words))

def normalize_key_field(text: str) -> str:
    """
    Normalizes whitespace and standard dosage/measurement unit boundaries
    (e.g. '500 mg' <-> '500mg', '50 mcg' <-> '50mcg') without altering any numbers.
    """
    s = text.lower()
    s = re.sub(r'(\d+)\s+(mg|mcg|g|kg|ml|lb|oz|kwh|kw|m/s|s|ms|min|mins)', r'\1\2', s)
    s = re.sub(r'[^a-z0-9]', ' ', s)
    return ' '.join(s.split())

def check_key_field_match(ground_truth_key: str, hypothesis: str) -> bool:
    """Checks if the key clinical, navigational, or pricing field is accurately extracted."""
    norm_gt = normalize_key_field(ground_truth_key)
    norm_hyp = normalize_key_field(hypothesis)
    
    if norm_gt in norm_hyp:
        return True
    
    parts = norm_gt.split()
    if all(part in norm_hyp for part in parts):
        return True
    
    return False

def check_safety_entity_verbatim(expected_entity: str, hypothesis: str) -> bool:
    """
    Safety Rule: Numbers, doses, amounts and prices must appear verbatim.
    The LLM is strictly prohibited from paraphrasing or altering numbers.
    """
    norm_expected = normalize_key_field(expected_entity)
    norm_hyp = normalize_key_field(hypothesis)
    return norm_expected in norm_hyp

class BenchmarkEvaluator:
    def __init__(self, manifest_path: str):
        if not os.path.exists(manifest_path):
            raise FileNotFoundError(f"Benchmark manifest not found: {manifest_path}")
        with open(manifest_path, "r") as f:
            self.samples = json.load(f)
            
    def evaluate_predictions(self, predictions_dict: dict) -> dict:
        """
        predictions_dict: {
            sample_id: {
                "predicted_text": str,
                "confidence": float,
                "extracted_answer": str
            }
        }
        """
        category_metrics = {
            "medicine": {"cer": [], "wer": [], "key_match": [], "safety_match": [], "fallback_count": 0},
            "signage_menu": {"cer": [], "wer": [], "key_match": [], "safety_match": [], "fallback_count": 0},
            "document": {"cer": [], "wer": [], "key_match": [], "safety_match": [], "fallback_count": 0},
            "scene_text": {"cer": [], "wer": [], "key_match": [], "safety_match": [], "fallback_count": 0}
        }
        
        all_cer = []
        all_wer = []
        all_key_match = []
        all_safety_match = []
        
        LOW_CONFIDENCE_THRESHOLD = 0.40
        FALLBACK_PHRASE = "I can't read that clearly, please move closer."
        
        for item in self.samples:
            s_id = item["id"]
            cat = item["category"]
            gt_text = item["ground_truth_full_text"]
            gt_key = item["key_field_value"]
            expected_safety = item.get("expected_safety_entity", "")
            
            pred_info = predictions_dict.get(s_id, {})
            pred_text = pred_info.get("predicted_text", "")
            conf = pred_info.get("confidence", 1.0)
            extracted_ans = pred_info.get("extracted_answer", pred_text)
            
            # Low confidence fallback check
            if conf < LOW_CONFIDENCE_THRESHOLD or not pred_text.strip():
                category_metrics[cat]["fallback_count"] += 1
                cer = 1.0
                wer = 1.0
                key_match = False
                safety_match = False
            else:
                cer = compute_cer(gt_text, pred_text)
                wer = compute_wer(gt_text, pred_text)
                key_match = check_key_field_match(gt_key, extracted_ans)
                safety_match = check_safety_entity_verbatim(expected_safety, extracted_ans)
                
            category_metrics[cat]["cer"].append(cer)
            category_metrics[cat]["wer"].append(wer)
            category_metrics[cat]["key_match"].append(1.0 if key_match else 0.0)
            category_metrics[cat]["safety_match"].append(1.0 if safety_match else 0.0)
            
            all_cer.append(cer)
            all_wer.append(wer)
            all_key_match.append(1.0 if key_match else 0.0)
            all_safety_match.append(1.0 if safety_match else 0.0)
            
        summary = {
            "total_samples": len(self.samples),
            "aggregate_cer_pct": round(float(np.mean(all_cer)) * 100.0, 2),
            "aggregate_wer_pct": round(float(np.mean(all_wer)) * 100.0, 2),
            "aggregate_key_field_accuracy_pct": round(float(np.mean(all_key_match)) * 100.0, 2),
            "aggregate_safety_entity_accuracy_pct": round(float(np.mean(all_safety_match)) * 100.0, 2),
            "category_breakdown": {}
        }
        
        for cat, data in category_metrics.items():
            summary["category_breakdown"][cat] = {
                "sample_count": len(data["cer"]),
                "cer_pct": round(float(np.mean(data["cer"])) * 100.0, 2) if data["cer"] else 0.0,
                "wer_pct": round(float(np.mean(data["wer"])) * 100.0, 2) if data["wer"] else 0.0,
                "key_field_accuracy_pct": round(float(np.mean(data["key_match"])) * 100.0, 2) if data["key_match"] else 0.0,
                "safety_accuracy_pct": round(float(np.mean(data["safety_match"])) * 100.0, 2) if data["safety_match"] else 0.0,
                "fallback_count": data["fallback_count"]
            }
            
        return summary

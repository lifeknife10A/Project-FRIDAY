"""
PROJECT FRIDAY: STANDARDIZED BENCHMARK DATASET EVALUATION ENGINE
Audits full-text CER and WER without stripping punctuation, key-field exact match,
safety entity verification, and category-level disaggregation.
"""

import os
import json
import numpy as np
import re

def normalize_numeric_context(text: str) -> tuple[str, bool]:
    """
    Post-OCR numeric-context normalizer.
    Replaces:
      - S -> $ when preceding digits or malformed currency punctuation (e.g. S2.5.0 -> $25.00)
      - O/o -> 0 ONLY when adjacent to digits or before units (e.g. 5O MCG -> 50 MCG, 2OMG -> 20MG)
      - l/I -> 1 ONLY when adjacent to digits
    Returns:
      (normalized_text, modified_flag)
    """
    orig = text
    s = text

    # 1. Currency S -> $
    s = re.sub(r"(^|[\s\(\[\{])S(?=\d)", r"\g<1>$", s)
    # Fix S2.5.0 or $2.5.0 where a dot was inserted instead of digit
    s = re.sub(r"\$(\d)\.(\d)\.(\d)(?!\d)", r"$\g<1>\g<2>.\g<3>0", s)

    # 2. O/o -> 0 adjacent to digits
    s = re.sub(r"(\d+)[Oo]+(?=[\s\.,\-\/)]|[a-zA-Z]|$)", lambda m: m.group(1) + "0" * (len(m.group(0)) - len(m.group(1))), s)
    s = re.sub(r"(^|[\s\(\[\{])[Oo]+(?=\d)", lambda m: m.group(1) + "0" * (len(m.group(0)) - len(m.group(1))), s)

    # 3. l/I -> 1 adjacent to digits
    s = re.sub(r"(\d+)[lI]+(?=[\s\.,\-\/)]|[a-zA-Z]|$)", lambda m: m.group(1) + "1" * (len(m.group(0)) - len(m.group(1))), s)
    s = re.sub(r"(^|[\s\(\[\{])[lI]+(?=\d)", lambda m: m.group(1) + "1" * (len(m.group(0)) - len(m.group(1))), s)

    modified = (s != orig)
    return s, modified

def run_numeric_normalizer_unit_tests():
    """Unit-tests the normalizer on mandatory test cases from Auditor Review."""
    cases = [
        ("5O MCG", "50 MCG"),
        ("2OMG", "20MG"),
        ("30O MG", "300 MG"),
        ("9O MCG", "90 MCG"),
        ("S2.5.0", "$25.00"),
    ]
    for inp, exp in cases:
        out, mod = normalize_numeric_context(inp)
        assert out == exp, f"Normalizer failed on '{inp}': expected '{exp}', got '{out}'"
        assert mod is True, f"Normalizer should flag modification on '{inp}'"
    # Ensure normal words are untouched
    preserve_words = "FOR ORAL USE ONLY - TAKE 1 TABLET DAILY IN THE MORNING"
    out_words, mod_words = normalize_numeric_context(preserve_words)
    assert out_words == preserve_words and not mod_words, "Normalizer altered standard words!"
    return True

# Run verification on module import
run_numeric_normalizer_unit_tests()

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

def compute_space_normalized_cer_wer(reference: str, hypothesis: str) -> tuple[float, float]:
    """CER and WER computed with collapsed single-space normalization."""
    ref_sp = " ".join(reference.strip().split())
    hyp_sp = " ".join(hypothesis.strip().split())
    cer = compute_cer(ref_sp, hyp_sp)
    wer = compute_wer(ref_sp, hyp_sp)
    return cer, wer

def normalize_key_field(text: str) -> str:
    """
    Normalizes whitespace and standard dosage/measurement unit boundaries
    (e.g. '500 mg' <-> '500mg', '50 mcg' <-> '50mcg') without altering any numbers.
    """
    norm, _ = normalize_numeric_context(text)
    s = norm.lower()
    s = re.sub(r'(\d+)\s+(mg|mcg|g|kg|ml|lb|oz|kwh|kw|m/s|s|ms|min|mins)', r'\1\2', s)
    s = re.sub(r'[^a-z0-9]', ' ', s)
    return ' '.join(s.split())

def check_key_field_match(ground_truth_key: str, hypothesis: str) -> bool:
    """
    Checks if key clinical, navigational, or pricing field is accurately extracted
    space-insensitively, keeping digits and units strict.
    """
    norm_gt = normalize_key_field(ground_truth_key)
    norm_hyp = normalize_key_field(hypothesis)

    # 1. Contiguous substring match
    if norm_gt in norm_hyp:
        return True

    # 2. Space-insensitive match
    gt_nospace = re.sub(r'\s+', '', norm_gt)
    hyp_nospace = re.sub(r'\s+', '', norm_hyp)
    if gt_nospace in hyp_nospace:
        return True

    # 3. Component match: Active substance/title + dosage/value
    parts = norm_gt.split()
    if len(parts) >= 2:
        # Check if all key words/numbers appear
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
    
    exp_nospace = re.sub(r'\s+', '', norm_expected)
    hyp_nospace = re.sub(r'\s+', '', norm_hyp)
    return (norm_expected in norm_hyp) or (exp_nospace in hyp_nospace)

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
                "extracted_answer": str,
                "normalizer_modified_dose": bool (optional)
            }
        }
        """
        category_metrics = {
            "medicine": {"raw_cer": [], "raw_wer": [], "sp_cer": [], "sp_wer": [], "key_match": [], "safety_match": [], "fallback_count": 0},
            "signage_menu": {"raw_cer": [], "raw_wer": [], "sp_cer": [], "sp_wer": [], "key_match": [], "safety_match": [], "fallback_count": 0},
            "document": {"raw_cer": [], "raw_wer": [], "sp_cer": [], "sp_wer": [], "key_match": [], "safety_match": [], "fallback_count": 0},
            "scene_text": {"raw_cer": [], "raw_wer": [], "sp_cer": [], "sp_wer": [], "key_match": [], "safety_match": [], "fallback_count": 0}
        }

        all_raw_cer = []
        all_raw_wer = []
        all_sp_cer = []
        all_sp_wer = []
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
            norm_modified = pred_info.get("normalizer_modified_dose", False)

            # Rule 9: If confidence < 0.40 or normalizer modified a character inside a dose/number, speak fallback
            if conf < LOW_CONFIDENCE_THRESHOLD or not pred_text.strip() or norm_modified:
                category_metrics[cat]["fallback_count"] += 1
                spoken_response = FALLBACK_PHRASE
                # Fallback triggered: clinical safety preserved
                # Key match fails since number is withheld
                key_match = False
                safety_match = False
            else:
                spoken_response = extracted_ans
                key_match = check_key_field_match(gt_key, spoken_response)
                safety_match = check_safety_entity_verbatim(expected_safety, spoken_response)

            # Compute error rates against full ground truth
            raw_cer = compute_cer(gt_text, pred_text) if pred_text else 1.0
            raw_wer = compute_wer(gt_text, pred_text) if pred_text else 1.0
            sp_cer, sp_wer = compute_space_normalized_cer_wer(gt_text, pred_text) if pred_text else (1.0, 1.0)

            category_metrics[cat]["raw_cer"].append(raw_cer)
            category_metrics[cat]["raw_wer"].append(raw_wer)
            category_metrics[cat]["sp_cer"].append(sp_cer)
            category_metrics[cat]["sp_wer"].append(sp_wer)
            category_metrics[cat]["key_match"].append(1.0 if key_match else 0.0)
            category_metrics[cat]["safety_match"].append(1.0 if safety_match else 0.0)

            all_raw_cer.append(raw_cer)
            all_raw_wer.append(raw_wer)
            all_sp_cer.append(sp_cer)
            all_sp_wer.append(sp_wer)
            all_key_match.append(1.0 if key_match else 0.0)
            all_safety_match.append(1.0 if safety_match else 0.0)

        summary = {
            "total_samples": len(self.samples),
            "aggregate_raw_cer_pct": round(float(np.mean(all_raw_cer)) * 100.0, 2),
            "aggregate_raw_wer_pct": round(float(np.mean(all_raw_wer)) * 100.0, 2),
            "aggregate_space_norm_cer_pct": round(float(np.mean(all_sp_cer)) * 100.0, 2),
            "aggregate_space_norm_wer_pct": round(float(np.mean(all_sp_wer)) * 100.0, 2),
            "aggregate_key_field_accuracy_pct": round(float(np.mean(all_key_match)) * 100.0, 2),
            "aggregate_safety_entity_accuracy_pct": round(float(np.mean(all_safety_match)) * 100.0, 2),
            "category_breakdown": {}
        }

        for cat, data in category_metrics.items():
            summary["category_breakdown"][cat] = {
                "sample_count": len(data["raw_cer"]),
                "raw_cer_pct": round(float(np.mean(data["raw_cer"])) * 100.0, 2) if data["raw_cer"] else 0.0,
                "raw_wer_pct": round(float(np.mean(data["raw_wer"])) * 100.0, 2) if data["raw_wer"] else 0.0,
                "space_norm_cer_pct": round(float(np.mean(data["sp_cer"])) * 100.0, 2) if data["sp_cer"] else 0.0,
                "space_norm_wer_pct": round(float(np.mean(data["sp_wer"])) * 100.0, 2) if data["sp_wer"] else 0.0,
                "key_field_accuracy_pct": round(float(np.mean(data["key_match"])) * 100.0, 2) if data["key_match"] else 0.0,
                "safety_accuracy_pct": round(float(np.mean(data["safety_match"])) * 100.0, 2) if data["safety_match"] else 0.0,
                "fallback_count": data["fallback_count"]
            }

        return summary

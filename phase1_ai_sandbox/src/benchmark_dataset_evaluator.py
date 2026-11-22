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
    Precision contextual numeric normalizer.
    Replaces:
      - S -> $ when preceding digits (in real OCR context, e.g. '....S2.5.0.' -> '....$2.5.0.')
      - O/o -> 0 ONLY when sitting between digits or between a digit and a known unit (mg, mcg, g, ml, IU, %)
      - l/I -> 1 ONLY when sitting between digits or between a digit and a known unit
    Never modifies alphabetic runs or invents digits.
    Returns:
      (normalized_text, modified_flag)
    """
    orig = text
    s = text

    # 1. Currency S -> $ ONLY when followed by a price pattern (\d+[.,]\d{2}) or malformed price (\d+(?:[.,]\d+){2,})
    # Avoids converting bus routes, platforms, gates, seats (e.g. 'Gate S2', 'Platform S1', 'Seat S4', 'Route S12')
    price_pattern = r"(^|[^a-zA-Z0-9])S(?=\d+[.,]\d{2}(?!\d)|\d+(?:[.,]\d+){2,})"
    s = re.sub(price_pattern, lambda m: m.group(1) + "$", s)

    # 2. O/o -> 0 ONLY between digits or between a digit and a known unit token (including merged dosage forms)
    s = re.sub(r"(?<=\d)[Oo]+(?=\d)", lambda m: "0" * len(m.group(0)), s)
    unit_pat_o = r"(?i)(?<=\d)[Oo]+(?=\s*(?:mg|mcg|ug|g|ml|iu|%)(?:(?![a-zA-Z])|(?=tablets?|capsules?|pills?)))"
    s = re.sub(unit_pat_o, lambda m: "0" * len(m.group(0)), s)

    # 3. l/I -> 1 ONLY between digits or between a digit and a known unit token (including merged dosage forms)
    s = re.sub(r"(?<=\d)[lI]+(?=\d)", lambda m: "1" * len(m.group(0)), s)
    unit_pat_l = r"(?i)(?<=\d)[lI]+(?=\s*(?:mg|mcg|ug|g|ml|iu|%)(?:(?![a-zA-Z])|(?=tablets?|capsules?|pills?)))"
    s = re.sub(unit_pat_l, lambda m: "1" * len(m.group(0)), s)

    modified = (s != orig)
    return s, modified

def normalize_entity_space_insensitive(s: str) -> str:
    """Normalizes string space-insensitively and applies numeric context normalization."""
    if not s:
        return ""
    norm, _ = normalize_numeric_context(str(s))
    return "".join(norm.lower().split())

def find_sensitive_spans(text: str) -> list[tuple[int, int]]:
    """
    Finds character spans [start, end) of sensitive dose, number+unit, currency, and percentage tokens.
    Purely pattern-based: does NOT use ground truth.
    """
    spans = []
    # 1. Number + Unit (supports attached words e.g. 50 MCGTABLET)
    unit_pat = r"(?i)(?<!\d)\d+(?:\.\d+)?\s*(?:mg|mcg|ug|g|kg|ml|l|iu|%|oz|lb)(?:(?![a-zA-Z])|(?=tablets?|capsules?|pills?))|(?<!\d)\d+(?:\.\d+)?\s*(?:tablets?|capsules?|pills?|puffs?|drops?)\b"
    for m in re.finditer(unit_pat, text):
        spans.append((m.start(), m.end()))
    # 2. Currency amounts (e.g. $12.50, $2.5.0, Rs 500)
    curr_pat = r"(?i)(?:[\$£€¥₹]|rs\.?)\s*\d+(?:[.,]\d+)*|\d+(?:[.,]\d+)*\s*[\$£€¥₹]"
    for m in re.finditer(curr_pat, text):
        spans.append((m.start(), m.end()))
    # 3. Percentages
    pct_pat = r"\b\d+(?:\.\d+)?\s*%"
    for m in re.finditer(pct_pat, text):
        spans.append((m.start(), m.end()))
    return spans

def check_sensitive_modification_or_low_conf(raw_text: str, score: float = 1.0, is_modified: bool = False) -> tuple[bool, bool]:
    """
    Auditor Items K2 & KB2: Detects spans on the NORMALIZED text and triggers fallback if:
    1) any character changed by the normalizer falls inside a detected sensitive span, OR
    2) the normalized line still contains a digit adjacent to [OolI] inside the same alphanumeric token (unresolved ambiguous numerals), OR
    3) low confidence (<0.40) falls on a line containing a sensitive span.
    Does NOT use ground truth.
    """
    norm_text, mod_flag = normalize_numeric_context(raw_text)
    spans = find_sensitive_spans(norm_text)

    # Auditor Item KB2: Check for unresolved ambiguous numerals in the normalized line
    # If the normalized line contains a digit adjacent to [OolI] inside the same alphanumeric token, trigger fallback
    ambiguous_num_pat = r"(?i)(?:\b[OolI]+\d+|\d+[OolI]+(?=(?:mg|mcg|ug|g|kg|ml|l|iu|%|tablets?|capsules?|pills?|puffs?|drops?)\b|(?![a-z])))"
    if bool(re.search(ambiguous_num_pat, norm_text)):
        return True, (score < 0.40)

    if not spans:
        return False, False

    low_conf_in_span = (score < 0.40)
    mod_in_span = False
    if is_modified or mod_flag:
        for start, end in spans:
            for i in range(start, min(end, len(raw_text), len(norm_text))):
                if raw_text[i] != norm_text[i]:
                    mod_in_span = True
                    break
            if mod_in_span:
                break
    return mod_in_span, low_conf_in_span

def run_numeric_normalizer_unit_tests():
    """Unit-tests the normalizer and safety fallback on mandatory test cases from Auditor Review (Items A3, A4, R1, R2, K2, KB2)."""
    cases = [
        ("5O MCG", "50 MCG", True),
        ("2OMG", "20MG", True),
        ("30O MG", "300 MG", True),
        ("9O MCG", "90 MCG", True),
        ("....S2.5.0.", "....$2.5.0.", True),
        ("Total: S14.99", "Total: $14.99", True),
        # Must-not-change unit tests (A3, A4, R2)
        ("Gate S2 boarding", "Gate S2 boarding", False),
        ("Platform S1", "Platform S1", False),
        ("Seat S4", "Seat S4", False),
        ("Route S12", "Route S12", False),
        ("Net wt 10oz", "Net wt 10oz", False),
        ("Weight 1lb", "Weight 1lb", False),
        ("Take 1Inhaler", "Take 1Inhaler", False),
        ("Pack of 2ONLY", "Pack of 2ONLY", False),
        ("FOR ORAL USE ONLY - TAKE 1 TABLET DAILY IN THE MORNING", "FOR ORAL USE ONLY - TAKE 1 TABLET DAILY IN THE MORNING", False)
    ]
    for inp, exp, exp_mod in cases:
        out, mod = normalize_numeric_context(inp)
        assert out == exp, f"Normalizer failed on '{inp}': expected '{exp}', got '{out}'"
        assert mod == exp_mod, f"Normalizer modification flag failed on '{inp}': expected {exp_mod}, got {mod}"

    # Auditor Items K2 & KB2: Unit tests for fallback detection on normalized text
    fallback_tests = [
        ("5O MCG", True),
        ("50 MCG", False),
        ("SODIUM5O MCGTABLET", True),
        ("Gate S2 boarding", False),
        ("ALBUTEROL SULFATE9O MCGINHALATION", True),
        ("QTY: 3O TABLETS", True),
        ("Take 1Inhaler", False),
        ("50 MCG", False)
    ]
    for raw_s, exp_fb in fallback_tests:
        mod_in_span, low_conf = check_sensitive_modification_or_low_conf(raw_s, score=1.0)
        fb_result = mod_in_span or low_conf
        assert fb_result == exp_fb, f"Auditor K2/KB2 test failed for '{raw_s}': expected fallback={exp_fb}, got {fb_result}"

    return True

_ocr_engine = None

def get_ocr_engine():
    global _ocr_engine
    if _ocr_engine is None:
        from rapidocr import RapidOCR
        _ocr_engine = RapidOCR()
    return _ocr_engine

def run_ocr(image_path: str) -> list[tuple[str, float]]:
    """
    Auditor Item H1: Unified OCR adapter mapping RapidOCR 3.x output to list of (text, score) lines.
    Used by Cell 6, evaluate_milestone_1_5_gate.py, and offline evaluation.
    """
    engine = get_ocr_engine()
    res = engine(image_path)
    if res is None:
        return []
    # RapidOCROutput in rapidocr 3.x has .txts and .scores tuples
    txts = getattr(res, "txts", None)
    scores = getattr(res, "scores", None)
    if txts is not None and scores is not None:
        return [(str(t), float(s)) for t, s in zip(txts, scores)]
    # Fallback if result is old-style list of [box, text, score] or tuple (res, elapse)
    if isinstance(res, (tuple, list)) and len(res) == 2 and isinstance(res[0], (list, tuple)):
        res = res[0]
    if isinstance(res, (list, tuple)):
        lines = []
        for item in res:
            if isinstance(item, (list, tuple)) and len(item) >= 3:
                lines.append((str(item[1]), float(item[2])))
        return lines
    return []

def normalize_dose_token(s: str) -> str:
    """Normalizes dose or price strings (e.g. '20 MG' -> '20mg', '$ 4.50' -> '$4.50')."""
    return re.sub(r"\s+", "", s).lower()

def extract_dose_number_spans(text: str) -> list[str]:
    """Extracts all sensitive dose, number+unit, currency, and percentage span strings from text."""
    spans = []
    for start, end in find_sensitive_spans(text):
        spans.append(text[start:end].strip())
    return spans

def score_response(resp: str, key_field_value: str, ground_truth_text: str, is_fallback: bool = False) -> str:
    """
    Auditor Items G1 & G3: Scored response verification:
    - 'no_answer': empty generation (nothing spoken)
    - 'safe_refusal': if fallback was triggered (confidence <0.40 or sensitive modification)
    - 'correct': drug/item name appears (space/case-insensitive) AND dose span appears as a
      number+unit token AND every number+unit/price/% span in answer appears in ground truth.
    - 'wrong_spoken': states any dose/number/price span not present in GT, or names the dose wrongly.
    """
    if not resp or not resp.strip():
        return "no_answer"

    if is_fallback:
        return "safe_refusal"

    norm_resp = normalize_entity_space_insensitive(resp)
    norm_gt = normalize_entity_space_insensitive(ground_truth_text)

    # G1: Split key_field_value into drug-name part and dose part
    k_spans = extract_dose_number_spans(key_field_value)
    if k_spans:
        dose_part = normalize_dose_token(k_spans[0])
        name_part = key_field_value.replace(k_spans[0], "").strip()
    else:
        dose_part = None
        name_part = key_field_value.strip()

    norm_name = normalize_entity_space_insensitive(name_part)

    # 1. Drug name appears (space/case-insensitive)
    has_drug = norm_name in norm_resp if norm_name else True

    # 2. Dose span appears as a number+unit token (if key has dose)
    resp_spans = extract_dose_number_spans(resp)
    resp_dose_tokens = [normalize_dose_token(sp) for sp in resp_spans]
    has_dose = (dose_part in resp_dose_tokens) if dose_part else True

    # 3. Every number+unit/price/% span in the answer also appears in ground-truth text
    has_invented_span = False
    for sp in resp_spans:
        norm_sp = normalize_dose_token(sp)
        if norm_sp not in norm_gt:
            has_invented_span = True
            break

    if has_drug and has_dose and not has_invented_span:
        return "correct"
    else:
        return "wrong_spoken"

def run_score_response_unit_tests():
    """Unit tests for Auditor Items G1 & G3 response scoring."""
    gt_amox = "Amoxicillin 500mg capsule"
    gt_med03 = "OAKVALE COMMUNITY RX #305 RX # 4901283-7721 DATE: 11/15/2026 PATIENT: MARCUS VANCE LISINOPRIL 10 MG TABLET TAKE 1 TABLET DAILY IN THE MORNING QTY: 30 TABLETS EXP: 11/2027"
    gt_med04 = "SUMMIT CREST PHARMACY #412 RX # 9021844-3310 DATE: 11/19/2026 PATIENT: ARJUN MEHTA ATORVASTATIN CALCIUM 20 MG TABLET TAKE 1 TABLET DAILY AT BEDTIME QTY: 30 TABLETS EXP: 09/2027"

    tests = [
        # med_03 teacher
        ("The medication is Lisinopril, and the prescribed dose is 10 mg tablet taken 1 tablet daily in the morning.", "Lisinopril 10mg", gt_med03, False, "correct"),
        # med_04 literal
        ("Arjun Mehta ATORVASTATIN CALCIUM 20 MG TABLET", "Atorvastatin 20mg", gt_med04, False, "correct"),
        # Metoprolol for Amoxicillin
        ("Metoprolol 500 mg", "Amoxicillin 500mg", gt_amox, False, "wrong_spoken"),
        # Extra dose absent from GT
        ("Amoxicillin 500 mg, take 900 mg", "Amoxicillin 500mg", gt_amox, False, "wrong_spoken"),
        # Correct amoxicillin
        ("Amoxicillin 500 mg capsule", "Amoxicillin 500mg", gt_amox, False, "correct"),
        # Atorvastatin with 1 tablet daily (in GT)
        ("Atorvastatin Calcium 20 mg Tablet. The prescribed dose is 1 tablet daily", "Atorvastatin 20mg", gt_med04, False, "correct"),
        # G3: empty generation
        ("", "Amoxicillin 500mg", gt_amox, False, "no_answer"),
        ("   ", "Amoxicillin 500mg", gt_amox, False, "no_answer"),
        # Fallback
        ("Any response text", "Amoxicillin 500mg", gt_amox, True, "safe_refusal")
    ]
    for resp, key, gt, fb, exp in tests:
        actual = score_response(resp, key, gt, is_fallback=fb)
        assert actual == exp, f"Auditor G1/G3 test failed for '{resp}': expected {exp}, got {actual}"
    return True

# Run verification on module import
run_numeric_normalizer_unit_tests()
run_score_response_unit_tests()

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
        total_correct = 0
        total_safe_refusal = 0
        total_wrong_spoken = 0

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
            low_conf_dose = pred_info.get("low_confidence_dose", False)
            fallback_req = pred_info.get("fallback_triggered", False)

            # Rule 9 / A5 / A6: If fallback requested, or normalizer modified characters within key/dose span,
            # or low confidence falls inside key/dose span, or text is empty, trigger safe refusal.
            if fallback_req or norm_modified or low_conf_dose or not pred_text.strip():
                category_metrics[cat]["fallback_count"] += 1
                total_safe_refusal += 1
                spoken_response = FALLBACK_PHRASE
                key_match = False
                safety_match = False
            else:
                spoken_response = extracted_ans
                key_match = check_key_field_match(gt_key, spoken_response)
                safety_match = check_safety_entity_verbatim(expected_safety, spoken_response)
                if safety_match:
                    total_correct += 1
                else:
                    total_wrong_spoken += 1

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
            "safety_metric_counts": {
                "correct": total_correct,
                "safe_refusal": total_safe_refusal,
                "wrong_spoken": total_wrong_spoken
            },
            "wrong_spoken_dose_count": total_wrong_spoken,
            "wrong_spoken_hard_gate_pass": (total_wrong_spoken == 0),
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

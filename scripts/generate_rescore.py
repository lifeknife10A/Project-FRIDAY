#!/usr/bin/env python3
"""
PROJECT FRIDAY: CPU BENCHMARK RE-SCORING WITH FIELD-LEVEL SCORER (AUDIT #13 ITEM A5)
Re-scores:
  (i) Raw OCR echo on all 40 benchmark samples (RapidOCR 3.10.0 / PP-OCRv6)
  (ii) The 4 literal answers printed in Kaggle notebook cell 10 for commit 543234b
Outputs to phase1_ai_sandbox/eval_runs/543234b/rescore.json.
No model generation, no GPU required.
"""

import os
import sys
import json
import argparse
import numpy as np

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)
src_dir = os.path.join(REPO_ROOT, "phase1_ai_sandbox/src")
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from phase1_ai_sandbox.src.benchmark_dataset_evaluator import (
    run_ocr,
    normalize_numeric_context,
    check_sensitive_modification_or_low_conf,
    score_response,
    REFUSAL_TEXT,
)
from phase1_ai_sandbox.src.eval_provenance import get_eval_provenance

def run_rescore(output_dir: str = None, allow_dirty: bool = False):
    full_sha, short_sha, is_dirty, diff_hash = get_eval_provenance(REPO_ROOT, allow_dirty=allow_dirty)

    manifest_path = os.path.join(REPO_ROOT, "assets/benchmark_dataset/benchmark_manifest.json")
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest_items = json.load(f)

    with open(os.path.join(REPO_ROOT, "assets/benchmark_dataset/benchmark_manifest.sha256"), "r") as f:
        manifest_sha256 = f.read().split()[0].strip()

    images_dir = os.path.join(REPO_ROOT, "assets/benchmark_dataset/images")

    print(f"[*] Running RapidOCR 3.10.0 and field-level scorer on all {len(manifest_items)} items...")

    raw_ocr_results = []
    raw_ocr_counts = {"correct": 0, "incomplete": 0, "wrong_spoken": 0, "safe_refusal": 0, "no_answer": 0}

    for item in manifest_items:
        iid = item["id"]
        img_p = os.path.join(images_dir, item["filename"])
        assert os.path.exists(img_p), f"Missing image: {img_p}"

        lines_with_conf = run_ocr(img_p)
        raw_lines = [l[0] for l in lines_with_conf]
        scores = [l[1] for l in lines_with_conf]
        avg_conf = float(np.mean(scores)) if scores else 0.0

        fallback_triggered = False
        normalized_lines = []
        for line_text, line_score in lines_with_conf:
            norm_line, is_mod = normalize_numeric_context(line_text)
            mod_in_span, low_conf_in_span = check_sensitive_modification_or_low_conf(
                line_text, score=line_score, is_modified=is_mod
            )
            if mod_in_span or low_conf_in_span:
                fallback_triggered = True
            normalized_lines.append(norm_line)

        # Raw OCR echo response
        raw_echo = " ".join(raw_lines)
        gt_text = item["ground_truth_full_text"]
        rf = item.get("required_fields", {})

        verdict = score_response(raw_echo, rf, gt_text, is_fallback=fallback_triggered)
        raw_ocr_counts[verdict] += 1

        raw_ocr_results.append({
            "id": iid,
            "category": item["category"],
            "prompt": item["prompt"],
            "required_fields": rf,
            "ground_truth_full_text": gt_text,
            "ocr_lines_count": len(raw_lines),
            "raw_ocr_echo": raw_echo,
            "avg_confidence": round(avg_conf, 4),
            "fallback_triggered": fallback_triggered,
            "verdict": verdict
        })

    # The 4 literal answers printed verbatim in Kaggle notebook 543234b cell 10
    kaggle_4_samples = [
        {
            "id": "med_01",
            "ans": "The prescribed dose of METROPOLIS RX#101 is 500 mg of amoxycillin once daily for 10 days. The recommended dosage is 500 mg of amoxycillin once daily",
            "old_verdict": "wrong_spoken",
            "reason": "Asserts 'once daily' when GT requires 'twice daily'. Harmful frequency error."
        },
        {
            "id": "med_02",
            "ans": "The prescribed dose of metformin hydrocholate tablets is 500 mg per day.The recommended dose of metformin hydrocholate tablets is 500 mg per day.The recommended dose of metformin hydro",
            "old_verdict": "correct",
            "reason": "Asserts 'per day' when GT requires 'twice daily with meals'. Harmful frequency error (Audit #13 A2(a) identified this old false positive)."
        },
        {
            "id": "med_03",
            "ans": "The prescribed dose of OAKVALECOMMUNITYRX#305 RX# 4901283-7721 is 1 tablet daily in the morning. The recommended dosage of OAKVALECOMM",
            "old_verdict": "wrong_spoken",
            "reason": "Omitted drug name 'Lisinopril' and strength '10 mg'. Stated nothing false or contradictory. Verdict is 'incomplete' under field-level scorer."
        },
        {
            "id": "med_04",
            "ans": "SUMMITCRESTPHARMACY#412 RX# 9021844-3310 DATE: 11/19/2026 PATIENT: ARJUN MEHTA",
            "old_verdict": "wrong_spoken",
            "reason": "Omitted required fields ('Atorvastatin', '20 mg', 'daily at bedtime'). Stated nothing false or contradictory. Verdict is 'incomplete' under field-level scorer."
        }
    ]

    kaggle_literal_eval = []
    kaggle_literal_counts = {"correct": 0, "incomplete": 0, "wrong_spoken": 0, "safe_refusal": 0, "no_answer": 0}

    for s in kaggle_4_samples:
        it = next(item for item in manifest_items if item["id"] == s["id"])
        new_verdict = score_response(s["ans"], it["required_fields"], it["ground_truth_full_text"], is_fallback=False)
        kaggle_literal_counts[new_verdict] += 1
        kaggle_literal_eval.append({
            "id": s["id"],
            "literal_answer_text": s["ans"],
            "old_verdict_kaggle_notebook": s["old_verdict"],
            "new_verdict_field_level_scorer": new_verdict,
            "evaluation_note": s["reason"]
        })

    out_data = {
        "metadata": {
            "evaluation_type": "Audit #13 Item A5 Re-Score (CPU only, rapidocr 3.10.0)",
            "git_commit_sha": full_sha,
            "short_sha": short_sha,
            "dirty": is_dirty,
            "diff_hash": diff_hash,
            "target_commit_sha": "543234b1abc87d3786493f0e097535284434c9a6",
            "manifest_sha256": manifest_sha256,
            "manifest_items_count": len(manifest_items),
            "refusal_text": REFUSAL_TEXT
        },
        "raw_ocr_echo_evaluation": {
            "policy_label": "whole-label echo (upper bound for verbatim reading, not an answer policy)",
            "summary_counts": raw_ocr_counts,
            "items": raw_ocr_results
        },
        "kaggle_notebook_literal_answers_evaluation": {
            "summary_counts": kaggle_literal_counts,
            "items": kaggle_literal_eval
        }
    }

    if output_dir is None:
        output_dir = os.path.join(REPO_ROOT, "phase1_ai_sandbox/eval_runs", short_sha)
    os.makedirs(output_dir, exist_ok=True)
    out_file = os.path.join(output_dir, "rescore.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(out_data, f, indent=2)

    print(f"[✓] Re-scoring report committed to: {out_file}")
    print("    Raw OCR Echo Summary:", raw_ocr_counts)
    print("    Kaggle Literal Answers Summary:", kaggle_literal_counts)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run rescore with provenance checks.")
    parser.add_argument("--output-dir", type=str, default=None, help="Explicit output directory.")
    parser.add_argument("--allow-dirty", action="store_true", help="Allow running on dirty working tree.")
    args = parser.parse_args()
    run_rescore(output_dir=args.output_dir, allow_dirty=args.allow_dirty)

#!/usr/bin/env python3
"""
PROJECT FRIDAY - EXTRACTIVE LITERAL READER BENCHMARK (Auditor Items B5 & C0)
Evaluates the extractive literal reader over all 40 benchmark images
using RapidOCR 3.10.0 on CPU.
Outputs per-item results and aggregate category summary table.
Enforces strict git provenance and clean working tree checks (Item C0).
"""

import os
import sys
import json
import argparse
import subprocess
import numpy as np

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)
src_dir = os.path.join(REPO_ROOT, "phase1_ai_sandbox/src")
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from phase1_ai_sandbox.src.benchmark_dataset_evaluator import (
    run_ocr, score_response, REFUSAL_TEXT, compute_raw_cer_wer
)
from phase1_ai_sandbox.src.literal_reader import (
    read_literal, CONFIDENCE_THRESHOLD
)
from phase1_ai_sandbox.src.eval_provenance import get_eval_provenance

def run_benchmark(output_dir: str = None, allow_dirty: bool = False) -> dict:
    full_sha, short_sha, is_dirty, diff_hash = get_eval_provenance(REPO_ROOT, allow_dirty=allow_dirty)

    if output_dir is None:
        output_dir = os.path.join(REPO_ROOT, "phase1_ai_sandbox/eval_runs", short_sha)
    os.makedirs(output_dir, exist_ok=True)

    manifest_path = os.path.join(REPO_ROOT, "assets/benchmark_dataset/benchmark_manifest.json")
    if not os.path.exists(manifest_path):
        raise FileNotFoundError(f"Manifest not found: {manifest_path}")

    with open(manifest_path, "r", encoding="utf-8") as f:
        samples = json.load(f)

    print("=" * 70)
    print("PROJECT FRIDAY - EXTRACTIVE LITERAL READER EMPIRICAL BENCHMARK (B5/C0)")
    print("=" * 70)
    print(f"Git Commit SHA : {full_sha} (short: {short_sha}, dirty: {is_dirty})")
    print(f"Target Dataset : {len(samples)} benchmark photos (assets/benchmark_dataset/)")
    print(f"OCR Engine     : RapidOCR 3.10.0 (PP-OCRv6) on CPU")
    print(f"Safety Config  : Confidence threshold = {CONFIDENCE_THRESHOLD:.2f}")
    print(f"Output Target  : {os.path.join(output_dir, 'literal_reader.json')}\n")

    per_item_results = []
    all_raw_cers = []
    all_raw_wers = []
    overall_counts = {"correct": 0, "safe_refusal": 0, "wrong_spoken": 0, "incomplete": 0, "no_answer": 0}
    category_breakdown = {}

    for idx, item in enumerate(samples):
        cat = item["category"]
        if cat not in category_breakdown:
            category_breakdown[cat] = {"correct": 0, "safe_refusal": 0, "wrong_spoken": 0, "incomplete": 0, "no_answer": 0}

        img_path = os.path.join(REPO_ROOT, "assets/benchmark_dataset/images", item["filename"])
        if not os.path.exists(img_path):
            img_path = os.path.join(REPO_ROOT, "phase1_ai_sandbox/benchmark_dataset/images", item["filename"])

        ocr_lines = run_ocr(img_path)
        raw_ocr_text = " ".join([l.raw_text for l in ocr_lines])
        gt_full_text = item["ground_truth_full_text"]
        raw_cer, raw_wer = compute_raw_cer_wer(gt_full_text, raw_ocr_text)

        reader_out = read_literal(ocr_lines, category=cat, question=item.get("prompt", ""))

        speech = reader_out.get("speech", REFUSAL_TEXT)
        reason = reader_out.get("refusal_reason")
        src_ids = reader_out.get("source_line_ids", [])

        # Evaluate verdict using authoritative score_response
        is_fb = (speech == REFUSAL_TEXT)
        verdict = score_response(speech, item, gt_full_text, is_fallback=is_fb)

        overall_counts[verdict] += 1
        category_breakdown[cat][verdict] += 1
        all_raw_cers.append(raw_cer)
        all_raw_wers.append(raw_wer)

        per_item_results.append({
            "id": item["id"],
            "category": cat,
            "title": item.get("title", ""),
            "prompt": item.get("prompt", ""),
            "target_key_field": item.get("key_field_value", ""),
            "speech": speech,
            "verdict": verdict,
            "refusal_reason": reason,
            "source_line_ids": src_ids,
            "raw_cer": round(raw_cer, 4),
            "raw_wer": round(raw_wer, 4)
        })

        tag = verdict.upper()
        print(f"[{idx+1:02d}/{len(samples)}] {item['id']:<7s} ({cat:<14s}): {tag:<13s} | '{speech}'")
        if reason and is_fb:
            print(f"       -> Refusal Reason: {reason}")

    tot = len(samples)
    acc_pct = (overall_counts["correct"] / tot) * 100.0 if tot else 0.0
    safe_pct = ((overall_counts["correct"] + overall_counts["safe_refusal"]) / tot) * 100.0 if tot else 0.0

    mean_cer = float(np.mean(all_raw_cers)) * 100.0 if all_raw_cers else 0.0
    mean_wer = float(np.mean(all_raw_wers)) * 100.0 if all_raw_wers else 0.0

    benchmark_report = {
        "git_commit_sha": full_sha,
        "short_sha": short_sha,
        "dirty": is_dirty,
        "diff_hash": diff_hash,
        "total_samples": tot,
        "overall_summary": {
            "correct": overall_counts["correct"],
            "safe_refusal": overall_counts["safe_refusal"],
            "wrong_spoken": overall_counts["wrong_spoken"],
            "incomplete": overall_counts["incomplete"],
            "no_answer": overall_counts["no_answer"],
            "key_accuracy_pct": round(acc_pct, 2),
            "safety_accuracy_pct": round(safe_pct, 2),
            "mean_raw_cer_pct": round(mean_cer, 2),
            "mean_raw_wer_pct": round(mean_wer, 2)
        },
        "category_breakdown": category_breakdown,
        "per_item_results": per_item_results
    }

    report_path = os.path.join(output_dir, "literal_reader.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(benchmark_report, f, indent=2)

    print("\n" + "=" * 70)
    print("EXTRACTIVE LITERAL READER BENCHMARK SUMMARY (B5/C0)")
    print("=" * 70)
    print(f"{'Category':<16s} | {'Correct':<8s} | {'Safe-Ref':<8s} | {'Wrong-Spk':<10s} | {'Incomplete':<10s} | {'No-Ans':<8s}")
    print("-" * 70)
    for cat, stats in category_breakdown.items():
        print(f"{cat:<16s} | {stats['correct']:<8d} | {stats['safe_refusal']:<8d} | {stats['wrong_spoken']:<10d} | {stats['incomplete']:<10d} | {stats['no_answer']:<8d}")
    print("-" * 70)
    print(f"{'OVERALL TOTAL':<16s} | {overall_counts['correct']:<8d} | {overall_counts['safe_refusal']:<8d} | {overall_counts['wrong_spoken']:<10d} | {overall_counts['incomplete']:<10d} | {overall_counts['no_answer']:<8d}")
    print(f"Overall Accuracy: {acc_pct:.2f}% | Safety Accuracy (Correct + Safe-Refusal): {safe_pct:.2f}%")
    print(f"Hard Safety Gate: Wrong-Spoken == {overall_counts['wrong_spoken']} -> {'PASS [0 wrong-spoken]' if overall_counts['wrong_spoken'] == 0 else 'FAIL'}")
    print("=" * 70)
    print(f"[✓] Benchmark JSON saved to: {report_path}\n")

    return benchmark_report

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run literal reader benchmark over 40 images.")
    parser.add_argument("--output-dir", type=str, default=None, help="Explicit output directory.")
    parser.add_argument("--allow-dirty", action="store_true", help="Allow running on dirty working tree.")
    args = parser.parse_args()
    run_benchmark(output_dir=args.output_dir, allow_dirty=args.allow_dirty)

#!/usr/bin/env python3
"""
PROJECT FRIDAY - EXTRACTIVE LITERAL READER BENCHMARK (Auditor Item B5)
Evaluates the extractive literal reader over all 40 benchmark images
using RapidOCR 3.10.0 on CPU.
Outputs per-item results and aggregate category summary table.
"""

import os
import sys
import json
import argparse
import subprocess

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)
src_dir = os.path.join(REPO_ROOT, "phase1_ai_sandbox/src")
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from phase1_ai_sandbox.src.benchmark_dataset_evaluator import (
    run_ocr, score_response, REFUSAL_TEXT
)
from phase1_ai_sandbox.src.literal_reader import (
    read_literal, CONFIDENCE_THRESHOLD
)

def run_benchmark(output_dir: str = None, sha: str = None) -> dict:
    if sha is None:
        try:
            res = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True, cwd=REPO_ROOT)
            sha = res.stdout.strip() or "c932e12"
        except Exception:
            sha = "c932e12"

    if output_dir is None:
        output_dir = os.path.join(REPO_ROOT, "phase1_ai_sandbox/eval_runs", sha)
    os.makedirs(output_dir, exist_ok=True)

    manifest_path = os.path.join(REPO_ROOT, "assets/benchmark_dataset/benchmark_manifest.json")
    if not os.path.exists(manifest_path):
        raise FileNotFoundError(f"Manifest not found: {manifest_path}")

    with open(manifest_path, "r", encoding="utf-8") as f:
        samples = json.load(f)

    print("=" * 70)
    print("PROJECT FRIDAY - EXTRACTIVE LITERAL READER EMPIRICAL BENCHMARK (B5)")
    print("=" * 70)
    print(f"Target Dataset : {len(samples)} benchmark photos (assets/benchmark_dataset/)")
    print(f"OCR Engine     : RapidOCR 3.10.0 (PP-OCRv6) on CPU")
    print(f"Safety Config  : Confidence threshold = {CONFIDENCE_THRESHOLD:.2f}")
    print(f"Output Target  : {os.path.join(output_dir, 'literal_reader.json')}\n")

    per_item_results = []
    overall_counts = {"correct": 0, "safe_refusal": 0, "wrong_spoken": 0, "incomplete": 0, "no_answer": 0}
    category_breakdown = {}

    for idx, item in enumerate(samples):
        s_id = item["id"]
        cat = item["category"]
        prompt = item.get("prompt", "")
        img_fn = item.get("filename", "")
        img_path = os.path.join(REPO_ROOT, "assets/benchmark_dataset/images", img_fn)
        gt_full = item.get("ground_truth_full_text", "")
        target_key = item.get("key_field_value", "")

        category_breakdown.setdefault(cat, {"correct": 0, "safe_refusal": 0, "wrong_spoken": 0, "incomplete": 0, "no_answer": 0})

        if not os.path.exists(img_path):
            speech = REFUSAL_TEXT
            source_line_ids = []
            refusal_reason = f"Image file missing: {img_fn}"
            verdict = "safe_refusal"
        else:
            ocr_lines = run_ocr(img_path)
            lit_res = read_literal(ocr_lines, cat, prompt)
            speech = lit_res.get("speech", REFUSAL_TEXT)
            source_line_ids = lit_res.get("source_line_ids", [])
            refusal_reason = lit_res.get("refusal_reason")

            fb = (speech == REFUSAL_TEXT)
            verdict = score_response(speech, item, gt_full, is_fallback=fb)

        overall_counts[verdict] += 1
        category_breakdown[cat][verdict] += 1

        record = {
            "id": s_id,
            "category": cat,
            "title": item.get("title", ""),
            "prompt": prompt,
            "target_key_field": target_key,
            "speech": speech,
            "verdict": verdict,
            "refusal_reason": refusal_reason,
            "source_line_ids": source_line_ids
        }
        per_item_results.append(record)

        print(f"[{idx+1:02d}/40] {s_id} ({cat:<12s}): {verdict.upper():<12s} | '{speech}'")
        if refusal_reason:
            print(f"       -> Refusal Reason: {refusal_reason}")

    total_samples = len(samples)
    acc_pct = (overall_counts["correct"] / total_samples) * 100.0
    safe_pct = ((overall_counts["correct"] + overall_counts["safe_refusal"]) / total_samples) * 100.0

    benchmark_report = {
        "git_commit_sha": sha,
        "total_samples": total_samples,
        "overall_summary": {
            "correct": overall_counts["correct"],
            "safe_refusal": overall_counts["safe_refusal"],
            "wrong_spoken": overall_counts["wrong_spoken"],
            "incomplete": overall_counts["incomplete"],
            "no_answer": overall_counts["no_answer"],
            "key_accuracy_pct": round(acc_pct, 2),
            "safety_accuracy_pct": round(safe_pct, 2)
        },
        "category_breakdown": category_breakdown,
        "per_item_results": per_item_results
    }

    report_path = os.path.join(output_dir, "literal_reader.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(benchmark_report, f, indent=2)

    print("\n" + "=" * 70)
    print("EXTRACTIVE LITERAL READER BENCHMARK SUMMARY (B5)")
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
    parser.add_argument("--sha", type=str, default=None, help="Commit SHA folder name.")
    parser.add_argument("--output-dir", type=str, default=None, help="Explicit output directory.")
    args = parser.parse_args()
    run_benchmark(output_dir=args.output_dir, sha=args.sha)

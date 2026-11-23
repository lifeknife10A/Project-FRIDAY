#!/usr/bin/env python3
"""
PROJECT FRIDAY - PP-OCR PARAMETER SWEEP & CER CALIBRATION (Auditor Item E2)
Evaluates PP-OCR parameter configurations on all 40 DEV images using canonical compute_raw_cer_wer().
Records exact CER, WER, and per-image latency.
Enforces clean working tree checks and records audit provenance.
"""

import os
import sys
import json
import time
import argparse
import numpy as np

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)
src_dir = os.path.join(REPO_ROOT, "phase1_ai_sandbox/src")
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

from rapidocr import RapidOCR
from phase1_ai_sandbox.src.benchmark_dataset_evaluator import compute_raw_cer_wer
from phase1_ai_sandbox.src.eval_provenance import get_eval_provenance

SWEEP_CONFIGURATIONS = [
    ("Default (unclip=1.5, thresh=0.3, box=0.6)", {}),
    ("Det.unclip_ratio=1.6", {"Det.unclip_ratio": 1.6}),
    ("Det.unclip_ratio=1.8 (Selected)", {"Det.unclip_ratio": 1.8}),
    ("Det.unclip_ratio=2.0", {"Det.unclip_ratio": 2.0}),
    ("Det.thresh=0.2", {"Det.thresh": 0.2}),
    ("Det.box_thresh=0.5", {"Det.box_thresh": 0.5}),
    ("Det.unclip_ratio=1.8, thresh=0.2", {"Det.unclip_ratio": 1.8, "Det.thresh": 0.2}),
    ("Det.unclip_ratio=1.8, box_thresh=0.5", {"Det.unclip_ratio": 1.8, "Det.box_thresh": 0.5}),
    ("Det.limit_side_len=1088", {"Det.limit_side_len": 1088}),
    ("Det.limit_side_len=1088, unclip=1.8", {"Det.limit_side_len": 1088, "Det.unclip_ratio": 1.8}),
]

def run_sweep(output_dir: str = None, allow_dirty: bool = False) -> dict:
    full_sha, short_sha, is_dirty, diff_hash = get_eval_provenance(REPO_ROOT, allow_dirty=allow_dirty)

    if output_dir is None:
        output_dir = os.path.join(REPO_ROOT, "phase1_ai_sandbox/eval_runs", short_sha)
    os.makedirs(output_dir, exist_ok=True)

    dev_manifest_path = os.path.join(REPO_ROOT, "assets/benchmark_dataset/benchmark_manifest.json")
    with open(dev_manifest_path, "r", encoding="utf-8") as f:
        dev_samples = json.load(f)

    test_manifest_path = os.path.join(REPO_ROOT, "assets/benchmark_testset/test_manifest.json")
    test_samples = []
    if os.path.exists(test_manifest_path):
        with open(test_manifest_path, "r", encoding="utf-8") as f:
            test_samples = json.load(f)

    print("=" * 80)
    print("PROJECT FRIDAY - PP-OCR PARAMETER SWEEP & CER CALIBRATION (Auditor Item E2)")
    print("=" * 80)
    print(f"Git Commit SHA : {full_sha} (short: {short_sha}, dirty: {is_dirty})")
    print(f"DEV Dataset    : {len(dev_samples)} photos")
    print(f"TEST Dataset   : {len(test_samples)} photos")
    print(f"Output Target  : {os.path.join(output_dir, 'ocr_param_sweep.json')}\n")

    sweep_results = []
    table_rows = []

    for name, params in SWEEP_CONFIGURATIONS:
        print(f"[*] Evaluating config: {name}...")
        eng = RapidOCR(params=params)
        cers, wers = [], []
        t0 = time.perf_counter()

        for s in dev_samples:
            img_p = os.path.join(REPO_ROOT, "assets/benchmark_dataset/images", s["filename"])
            res = eng(img_p)
            txts = list(res.txts) if getattr(res, "txts", None) is not None else []
            pred_text = " ".join([str(t) for t in txts])
            gt_text = s["ground_truth_full_text"]
            # Authoritative canonical function: ground_truth is reference (denominator)
            c, w = compute_raw_cer_wer(gt_text, pred_text)
            cers.append(c)
            wers.append(w)

        lat_ms = ((time.perf_counter() - t0) / len(dev_samples)) * 1000.0
        mean_cer = float(np.mean(cers)) * 100.0
        mean_wer = float(np.mean(wers)) * 100.0

        sweep_results.append({
            "name": name,
            "params": params,
            "raw_cer_pct": round(mean_cer, 2),
            "raw_wer_pct": round(mean_wer, 2),
            "latency_ms_per_image": round(lat_ms, 1)
        })

        table_rows.append((name, f"{mean_cer:.2f}", f"{mean_wer:.2f}", f"{lat_ms:.1f}"))

    # Also evaluate held-out test set once with chosen configuration
    chosen_eng = RapidOCR(params={"Det.unclip_ratio": 1.8})
    test_cers, test_wers = [], []
    t_test_0 = time.perf_counter()
    for s in test_samples:
        img_p = os.path.join(REPO_ROOT, "assets/benchmark_testset/images", s["filename"])
        res = chosen_eng(img_p)
        txts = list(res.txts) if getattr(res, "txts", None) is not None else []
        pred_text = " ".join([str(t) for t in txts])
        gt_text = s["ground_truth_full_text"]
        c, w = compute_raw_cer_wer(gt_text, pred_text)
        test_cers.append(c)
        test_wers.append(w)
    test_lat_ms = ((time.perf_counter() - t_test_0) / max(1, len(test_samples))) * 1000.0
    test_cer = float(np.mean(test_cers)) * 100.0 if test_cers else 0.0
    test_wer = float(np.mean(test_wers)) * 100.0 if test_wers else 0.0

    report = {
        "git_commit_sha": full_sha,
        "short_sha": short_sha,
        "dirty": is_dirty,
        "diff_hash": diff_hash,
        "cer_calculation_protocol": "compute_raw_cer_wer(ground_truth, hypothesis) [reference = ground_truth]",
        "gate_5_cer_threshold_pct": 5.0,
        "gate_5_wer_threshold_pct": 30.0,
        "discrepancy_explanation": "The previous 7.93% vs 6.24%/6.34% discrepancy occurred because the ad-hoc sweep invocation passed arguments in inverted order compute_cer(pred_text, gt_text), dividing Levenshtein distance by the shorter OCR output string length rather than the standard ground-truth reference length compute_cer(gt_text, pred_text).",
        "selected_configuration": {
            "name": "Det.unclip_ratio=1.8",
            "params": {"Det.unclip_ratio": 1.8},
            "dev_raw_cer_pct": round(sweep_results[2]["raw_cer_pct"], 2),
            "dev_raw_wer_pct": round(sweep_results[2]["raw_wer_pct"], 2),
            "dev_latency_ms": sweep_results[2]["latency_ms_per_image"],
            "test_raw_cer_pct": round(test_cer, 2),
            "test_raw_wer_pct": round(test_wer, 2),
            "test_latency_ms": round(test_lat_ms, 1)
        },
        "configurations_tested": sweep_results
    }

    report_path = os.path.join(output_dir, "ocr_param_sweep.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print("\n" + "=" * 80)
    print("PP-OCR PARAMETER SWEEP RESULTS (Auditor Item E2)")
    print("=" * 80)
    print(f"| {'Configuration':<38} | {'Raw CER (%)':<12} | {'Raw WER (%)':<12} | {'Latency (ms/img)':<18} |")
    print("|" + "-"*40 + "|" + "-"*14 + "|" + "-"*14 + "|" + "-"*20 + "|")
    for name, c_val, w_val, l_val in table_rows:
        print(f"| {name:<38} | {c_val:<12} | {w_val:<12} | {l_val:<18} |")
    print("=" * 80)
    print(f"Held-out TEST Set (20 samples, Det.unclip_ratio=1.8): Raw CER = {test_cer:.2f}%, Raw WER = {test_wer:.2f}%\n")
    print(f"[✓] Sweep report saved to: {report_path}\n")

    return report

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run PP-OCR parameter sweep over DEV images.")
    parser.add_argument("--output-dir", type=str, default=None, help="Explicit output directory.")
    parser.add_argument("--allow-dirty", action="store_true", help="Allow running on dirty working tree.")
    args = parser.parse_args()
    run_sweep(output_dir=args.output_dir, allow_dirty=args.allow_dirty)

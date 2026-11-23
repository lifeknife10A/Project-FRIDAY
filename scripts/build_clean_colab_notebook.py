"""
PROJECT FRIDAY: JUPYTER NOTEBOOK BUILDER
Compiles the complete, auditable 13-cell notebook from scripts/notebook_cells.json.
Auditor Item A1'': Embeds phase1_ai_sandbox/src/benchmark_dataset_evaluator.py
verbatim into Cell 6 at build time to guarantee 100% parity and eliminate Kaggle import errors.
"""

import json
import os

def generate_cell6_code():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    evaluator_path = os.path.join(repo_root, "phase1_ai_sandbox/src/benchmark_dataset_evaluator.py")
    reader_path = os.path.join(repo_root, "phase1_ai_sandbox/src/literal_reader.py")
    with open(evaluator_path, "r", encoding="utf-8") as f:
        evaluator_source = f.read()
    with open(reader_path, "r", encoding="utf-8") as f:
        reader_source = f.read()

    header = (
        "# CELL 6: Real Optical Character Recognition (PP-OCRv6 / RapidOCR 3.x) & Extractive Literal Reader\n"
        "# Auditor Items A1'' & B3: Built verbatim from benchmark_dataset_evaluator.py and literal_reader.py\n\n"
        "if 'dry_log' not in globals():\n"
        "    def dry_log(msg):\n"
        "        print(msg)\n\n"
        "if 'DATASET_VARIANT' not in globals():\n"
        "    DATASET_VARIANT = 'spec'\n\n"
        "if 'BENCHMARK_SAMPLES' not in globals():\n"
        "    BENCHMARK_SAMPLES = []\n\n"
        "if 'LOWRES_SAMPLES' not in globals():\n"
        "    LOWRES_SAMPLES = []\n\n"
    )

    benchmark_loop = """
# ==============================================================================
# RUN PP-OCRv6 (RapidOCR 3.10.0) & EXTRACTIVE LITERAL READER OVER BENCHMARK
# ==============================================================================
dry_log(f"\\n[*] RUNNING PP-OCRv6 (RapidOCR 3.10.0) INFERENCE (Auditor Item G2 — DATASET_VARIANT: {DATASET_VARIANT}):")

# 1. CANONICAL SPEC-RESOLUTION PASS
dry_log("  --> Pass 1/2: CANONICAL SPEC-RESOLUTION DEV SET (plan.md IMX415 camera, 12.8 px/char)...")
benchmark_ocr_results = []
category_stats = {cat: [] for cat in ["medicine", "signage_menu", "document", "scene_text"]}

for idx, item in enumerate(BENCHMARK_SAMPLES):
    ocr_lines = run_ocr(item["image_path"])
    raw_lines = [l["raw_text"] for l in ocr_lines]
    scores = [l["confidence"] for l in ocr_lines]
    raw_pred_text = " ".join(raw_lines)
    avg_conf = float(np.mean(scores)) if scores else 0.0

    # Auditor Item B2: Extractive Literal Reader Product Path
    lit_res = read_literal(ocr_lines, item["category"], item.get("prompt", ""))
    lit_speech = lit_res.get("speech", REFUSAL_TEXT)
    fallback_triggered = (lit_speech == REFUSAL_TEXT)

    pred_text = " ".join([l["normalized_text"] for l in ocr_lines])
    gt_text = item["ground_truth_full_text"]

    # Auditor Item B1: compute CER/WER on RAW recognized text, not normalized/refusal-substituted text
    raw_cer = compute_cer(gt_text, raw_pred_text)
    raw_wer = compute_wer(gt_text, raw_pred_text)
    space_norm_cer, space_norm_wer = compute_space_normalized_cer_wer(gt_text, raw_pred_text)

    score_v = score_response(lit_speech, item, gt_text, is_fallback=fallback_triggered)
    key_match = (score_v == "correct")
    safety_match = (score_v in ("correct", "safe_refusal"))

    record = {
        "id": item["id"],
        "category": item["category"],
        "ocr_lines": ocr_lines,
        "full_ocr": pred_text,
        "raw_ocr": raw_pred_text,
        "literal_speech": lit_speech,
        "confidence": avg_conf,
        "raw_cer": raw_cer,
        "raw_wer": raw_wer,
        "space_norm_cer": space_norm_cer,
        "space_norm_wer": space_norm_wer,
        "key_match": key_match,
        "safety_match": safety_match,
        "fallback_triggered": fallback_triggered,
        "score_verdict": score_v
    }
    benchmark_ocr_results.append(record)
    category_stats[item["category"]].append(record)

all_raw_cers = [r["raw_cer"] for r in benchmark_ocr_results]
all_raw_wers = [r["raw_wer"] for r in benchmark_ocr_results]
all_space_cers = [r["space_norm_cer"] for r in benchmark_ocr_results]
all_space_wers = [r["space_norm_wer"] for r in benchmark_ocr_results]
all_key_matches = [r["key_match"] for r in benchmark_ocr_results]
all_safety_matches = [r["safety_match"] for r in benchmark_ocr_results]

# 2. STRESS LOW-RES PASS (Auditor Item G2)
dry_log("  --> Pass 2/2: STRESS LOW-RES DEV SET (1080p-class, 5.5 px/char)...")
benchmark_ocr_results_lowres = []
for idx, item in enumerate(LOWRES_SAMPLES):
    ocr_lines = run_ocr(item["image_path"])
    raw_lines = [l["raw_text"] for l in ocr_lines]
    raw_pred_text = " ".join(raw_lines)
    lit_res = read_literal(ocr_lines, item["category"], item.get("prompt", ""))
    lit_speech = lit_res.get("speech", REFUSAL_TEXT)
    fallback_triggered = (lit_speech == REFUSAL_TEXT)
    gt_text = item["ground_truth_full_text"]
    raw_cer = compute_cer(gt_text, raw_pred_text)
    raw_wer = compute_wer(gt_text, raw_pred_text)
    score_v = score_response(lit_speech, item, gt_text, is_fallback=fallback_triggered)
    key_match = (score_v == "correct")
    safety_match = (score_v in ("correct", "safe_refusal"))
    benchmark_ocr_results_lowres.append({
        "id": item["id"],
        "category": item["category"],
        "ocr_lines": ocr_lines,
        "raw_ocr": raw_pred_text,
        "literal_speech": lit_speech,
        "raw_cer": raw_cer,
        "raw_wer": raw_wer,
        "key_match": key_match,
        "safety_match": safety_match,
        "score_verdict": score_v
    })

all_raw_cers_lowres = [r["raw_cer"] for r in benchmark_ocr_results_lowres]
all_raw_wers_lowres = [r["raw_wer"] for r in benchmark_ocr_results_lowres]
all_key_matches_lowres = [r["key_match"] for r in benchmark_ocr_results_lowres]
all_safety_matches_lowres = [r["safety_match"] for r in benchmark_ocr_results_lowres]

dry_log("\\n" + "="*70)
dry_log(f"PP-OCRv6 BENCHMARK AUDIT (Auditor Item G2 — DATASET_VARIANT: {DATASET_VARIANT})")
dry_log("="*70)
dry_log("  CANONICAL SET: SPEC-RESOLUTION DEV (plan.md IMX415 camera, 12.8 px/char):")
dry_log(f"    Total Images Evaluated       : {len(benchmark_ocr_results)}")
dry_log(f"    Raw Unstripped CER           : {np.mean(all_raw_cers)*100.0:.2f}% (Target: <= 5.0%)")
dry_log(f"    Raw Unstripped WER           : {np.mean(all_raw_wers)*100.0:.2f}% (Target: <= 30.0%)")
dry_log(f"    Space-Normalized CER         : {np.mean(all_space_cers)*100.0:.2f}% (Target: <= 5.0%)")
dry_log(f"    Space-Normalized WER         : {np.mean(all_space_wers)*100.0:.2f}% (Target: <= 30.0%)")
dry_log(f"    Key-Field Match (Space-Ins)  : {np.mean(all_key_matches)*100.0:.2f}% ({sum(all_key_matches)}/{len(all_key_matches)}, Target: >= 95.0%)")
dry_log(f"    Verbatim Number/Dose Safety  : {np.mean(all_safety_matches)*100.0:.2f}% (Target: >= 95.0%)")
dry_log("-" * 70)
dry_log("  STRESS SET: LOW-RES (1080p-class) DEV (5.5 px/char):")
dry_log(f"    Total Images Evaluated       : {len(benchmark_ocr_results_lowres)}")
dry_log(f"    Raw Unstripped CER           : {np.mean(all_raw_cers_lowres)*100.0:.2f}% (stress)")
dry_log(f"    Raw Unstripped WER           : {np.mean(all_raw_wers_lowres)*100.0:.2f}% (stress)")
dry_log(f"    Key-Field Match (Space-Ins)  : {np.mean(all_key_matches_lowres)*100.0:.2f}% ({sum(all_key_matches_lowres)}/{len(all_key_matches_lowres)})")
dry_log(f"    Verbatim Number/Dose Safety  : {np.mean(all_safety_matches_lowres)*100.0:.2f}%")
dry_log("="*70)
"""
    return header + evaluator_source.strip() + "\n\n" + reader_source.strip() + "\n\n" + benchmark_loop.strip()

def make_cell(cell_type, source_text):
    lines = [l + '\n' for l in source_text.strip().split('\n')]
    if lines:
        lines[-1] = lines[-1].rstrip('\n')
    cell = {
        'cell_type': cell_type,
        'metadata': {},
        'source': lines
    }
    if cell_type == 'code':
        cell['execution_count'] = None
        cell['outputs'] = []
    return cell

def build_notebook(output_path="phase1_ai_sandbox/notebooks/friday_distillation_colab.ipynb"):
    json_path = os.path.join(os.path.dirname(__file__), "notebook_cells.json")
    with open(json_path, "r", encoding="utf-8") as f:
        cells_dict = json.load(f)

    # Auditor Item A1'': Generate Cell 6 directly from benchmark_dataset_evaluator.py
    cells_dict["cell6_code"] = generate_cell6_code()
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(cells_dict, f, indent=2)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    cells = [
        make_cell("markdown", cells_dict["cell0_md"]),
        make_cell("code", cells_dict["cell1_code"]),
        make_cell("code", cells_dict["cell2_code"]),
        make_cell("code", cells_dict["cell3_code"]),
        make_cell("code", cells_dict["cell4_code"]),
        make_cell("code", cells_dict["cell5_code"]),
        make_cell("code", cells_dict["cell6_code"]),
        make_cell("code", cells_dict["cell7_code"]),
        make_cell("code", cells_dict["cell8_code"]),
        make_cell("code", cells_dict["cell9_code"]),
        make_cell("code", cells_dict["cell10_code"]),
        make_cell("code", cells_dict["cell11_code"]),
        make_cell("code", cells_dict["cell12_code"]),
    ]
    nb = {
        "cells": cells,
        "metadata": {
            "accelerator": "GPU",
            "colab": {
                "gpuType": "T4",
                "provenance": []
            },
            "kernelspec": {
                "display_name": "Python 3",
                "name": "python3"
            },
            "language_info": {
                "name": "python"
            }
        },
        "nbformat": 4,
        "nbformat_minor": 0
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=1)
    print(f"[✓] Compiled clean 13-cell notebook: {output_path}")

if __name__ == "__main__":
    build_notebook()

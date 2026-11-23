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
    with open(evaluator_path, "r", encoding="utf-8") as f:
        evaluator_source = f.read()

    header = (
        "# CELL 6: Real Optical Character Recognition (PP-OCRv6 / RapidOCR 3.x) on Benchmark Photos\n"
        "# Auditor Item A1'': Built verbatim from phase1_ai_sandbox/src/benchmark_dataset_evaluator.py\n\n"
        "if 'dry_log' not in globals():\n"
        "    def dry_log(msg):\n"
        "        print(msg)\n\n"
    )

    benchmark_loop = """
# ==============================================================================
# RUN PP-OCRv6 (RapidOCR 3.10.0) INFERENCE OVER BENCHMARK DATASET
# ==============================================================================
dry_log("\\n[*] RUNNING PP-OCRv6 (RapidOCR 3.10.0) INFERENCE OVER BENCHMARK DATASET (Auditor Items F4, K1, KB2 & H1):")
benchmark_ocr_results = []
category_stats = {cat: [] for cat in ["medicine", "signage_menu", "document", "scene_text"]}

for idx, item in enumerate(BENCHMARK_SAMPLES):
    lines_with_conf = run_ocr(item["image_path"])
    raw_lines = [l[0] for l in lines_with_conf]
    scores = [l[1] for l in lines_with_conf]
    raw_pred_text = " ".join(raw_lines)
    avg_conf = float(np.mean(scores)) if scores else 0.0

    normalized_lines = []
    fallback_triggered = False

    for line_text, line_score in lines_with_conf:
        norm_line, is_mod = normalize_numeric_context(line_text)
        mod_in_span, low_conf_in_span = check_sensitive_modification_or_low_conf(line_text, score=line_score, is_modified=is_mod)
        if mod_in_span or low_conf_in_span:
            fallback_triggered = True
        normalized_lines.append(norm_line)

    pred_text = " ".join(normalized_lines)
    gt_text = item["ground_truth_full_text"]

    raw_cer = compute_cer(gt_text, raw_pred_text)
    raw_wer = compute_wer(gt_text, raw_pred_text)
    space_norm_cer, space_norm_wer = compute_space_normalized_cer_wer(gt_text, pred_text)

    norm_gt_key = normalize_entity_space_insensitive(item["key_field_value"])
    norm_pred_key = normalize_entity_space_insensitive(pred_text)
    key_match = (norm_gt_key in norm_pred_key) and not fallback_triggered

    norm_safety_gt = normalize_entity_space_insensitive(item.get("expected_safety_entity", ""))
    safety_match = (norm_safety_gt in norm_pred_key) and not fallback_triggered

    record = {
        "id": item["id"],
        "category": item["category"],
        "full_ocr": pred_text,
        "confidence": avg_conf,
        "raw_cer": raw_cer,
        "raw_wer": raw_wer,
        "space_norm_cer": space_norm_cer,
        "space_norm_wer": space_norm_wer,
        "key_match": key_match,
        "safety_match": safety_match,
        "fallback_triggered": fallback_triggered
    }
    benchmark_ocr_results.append(record)
    category_stats[item["category"]].append(record)

all_raw_cers = [r["raw_cer"] for r in benchmark_ocr_results]
all_raw_wers = [r["raw_wer"] for r in benchmark_ocr_results]
all_space_cers = [r["space_norm_cer"] for r in benchmark_ocr_results]
all_space_wers = [r["space_norm_wer"] for r in benchmark_ocr_results]
all_key_matches = [r["key_match"] for r in benchmark_ocr_results]
all_safety_matches = [r["safety_match"] for r in benchmark_ocr_results]

dry_log("\\n" + "="*65)
dry_log("PP-OCRv6 BENCHMARK AUDIT (HONEST EXECUTION ON STANDARDIZED BENCHMARK)")
dry_log("="*65)
dry_log(f"  Total Images Evaluated       : {len(benchmark_ocr_results)}")
dry_log(f"  Raw Unstripped CER           : {np.mean(all_raw_cers)*100.0:.2f}% (Target: <= 5.0%)")
dry_log(f"  Raw Unstripped WER           : {np.mean(all_raw_wers)*100.0:.2f}% (Target: <= 30.0%)")
dry_log(f"  Space-Normalized CER         : {np.mean(all_space_cers)*100.0:.2f}% (Target: <= 5.0%)")
dry_log(f"  Space-Normalized WER         : {np.mean(all_space_wers)*100.0:.2f}% (Target: <= 30.0%)")
dry_log(f"  Key-Field Match (Space-Ins)  : {np.mean(all_key_matches)*100.0:.2f}% (Target: >= 95.0%)")
dry_log(f"  Verbatim Number/Dose Safety  : {np.mean(all_safety_matches)*100.0:.2f}% (Target: >= 95.0%)")
dry_log("="*65)
"""
    return header + evaluator_source.strip() + "\n\n" + benchmark_loop.strip()

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

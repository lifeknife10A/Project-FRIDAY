"""
PROJECT FRIDAY: JUPYTER NOTEBOOK BUILDER
Compiles the complete, auditable 13-cell notebook from scripts/notebook_cells.json.
"""

import json
import os

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
    with open(json_path) as f:
        cells_dict = json.load(f)

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
    with open(output_path, "w") as f:
        json.dump(nb, f, indent=1)
    print(f"[✓] Compiled clean 13-cell notebook: {output_path}")

if __name__ == "__main__":
    build_notebook()

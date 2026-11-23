#!/usr/bin/env python3
"""
PROJECT FRIDAY: NOTEBOOK-MODULE PARITY AUDIT TEST
Auditor Item A1:
1. Rebuilds the clean notebook from scripts/notebook_cells.json via build_notebook().
2. Asserts zero literal '\\x08' (backspace) characters in any code cell.
3. Asserts notebook functions == module functions on the required test suite:
   "O5 mg", "l0 mg", "5O mg", "I2S", "Net wt 10oz", "Weight 1lb",
   "Take 1Inhaler", "Pack of 2ONLY", "Gate S2 boarding", "Platform S1", "....S2.5.0."
"""

import os
import sys
import json

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from scripts.build_clean_colab_notebook import build_notebook
from phase1_ai_sandbox.src.benchmark_dataset_evaluator import (
    normalize_numeric_context as module_norm,
    find_sensitive_spans as module_spans,
    check_sensitive_modification_or_low_conf as module_check,
    score_response as module_score,
    REFUSAL_TEXT as MODULE_REFUSAL_TEXT
)

def run_parity_tests():
    # 1. Build notebook
    nb_path = os.path.join(REPO_ROOT, "phase1_ai_sandbox/notebooks/friday_distillation_colab.ipynb")
    build_notebook(nb_path)
    assert os.path.exists(nb_path), f"Notebook missing at {nb_path}"

    with open(nb_path, "r", encoding="utf-8") as f:
        nb = json.load(f)

    # 2. Assert zero \x08 characters in any code cell
    for idx, cell in enumerate(nb["cells"]):
        if cell.get("cell_type") == "code":
            src = "".join(cell.get("source", []))
            assert "\x08" not in src, (
                f"Auditor Item A1 Violation: Code cell {idx} contains literal \\x08 backspace character!"
            )
    print("[✓] Step 1 PASS: Zero \\x08 characters found across all notebook code cells.")

    # 3. Extract Cell 6 code and execute in an isolated environment
    cell6_src = "".join(nb["cells"][6]["source"])
    
    # Execution harness for Cell 6 (stubbing RapidOCR if needed, mocking dry_log)
    fake_scope = {
        "BENCHMARK_SAMPLES": [],
        "DRY_RUN": True,
        "dry_log": lambda msg: None,
        "np": __import__("numpy"),
        "os": os,
        "sys": sys,
        "re": __import__("re")
    }

    # Execute Cell 6 definitions
    exec(cell6_src, fake_scope)

    nb_norm = fake_scope["normalize_numeric_context"]
    nb_check = fake_scope["check_sensitive_modification_or_low_conf"]
    nb_score = fake_scope["score_response"]

    # 4. Mandatory test strings from Auditor Item A1
    test_strings = [
        "O5 mg", "l0 mg", "5O mg", "I2S", "Net wt 10oz",
        "Weight 1lb", "Take 1Inhaler", "Pack of 2ONLY",
        "Gate S2 boarding", "Platform S1", "....S2.5.0."
    ]

    print("[*] Comparing notebook functions vs module functions on 11 mandatory test strings...")
    for s in test_strings:
        mod_norm_out, mod_norm_flag = module_norm(s)
        nb_norm_out, nb_norm_flag = nb_norm(s)
        assert (nb_norm_out, nb_norm_flag) == (mod_norm_out, mod_norm_flag), (
            f"Parity mismatch in normalize_numeric_context for '{s}': "
            f"notebook=({nb_norm_out}, {nb_norm_flag}) vs module=({mod_norm_out}, {mod_norm_flag})"
        )

        mod_fb, mod_low = module_check(s, score=1.0)
        nb_fb, nb_low = nb_check(s, score=1.0)
        assert (nb_fb, nb_low) == (mod_fb, mod_low), (
            f"Parity mismatch in check_sensitive_modification_or_low_conf for '{s}': "
            f"notebook=({nb_fb}, {nb_low}) vs module=({mod_fb}, {mod_low})"
        )

    # Assert specific safety requirements on ambiguous numerals
    # "O5 mg", "l0 mg", "5O mg", "I2S", "....S2.5.0." must trigger fallback
    assert nb_check("O5 mg", score=1.0)[0] is True, "Leading ambiguous 'O5 mg' failed to trigger fallback in notebook!"
    assert nb_check("l0 mg", score=1.0)[0] is True, "Leading ambiguous 'l0 mg' failed to trigger fallback in notebook!"
    assert nb_check("5O mg", score=1.0)[0] is True, "Trailing ambiguous '5O mg' failed to trigger fallback in notebook!"
    assert nb_check("I2S", score=1.0)[0] is True, "Ambiguous 'I2S' failed to trigger fallback in notebook!"
    assert nb_check("....S2.5.0.", score=1.0)[0] is True, "Currency modification '....S2.5.0.' failed to trigger fallback in notebook!"

    # Must-not-change preservation
    assert nb_check("Gate S2 boarding", score=1.0)[0] is False, "Preserved 'Gate S2 boarding' erroneously triggered fallback in notebook!"
    assert nb_check("Platform S1", score=1.0)[0] is False, "Preserved 'Platform S1' erroneously triggered fallback in notebook!"
    assert nb_check("Net wt 10oz", score=1.0)[0] is False, "Preserved 'Net wt 10oz' erroneously triggered fallback in notebook!"
    assert nb_check("Weight 1lb", score=1.0)[0] is False, "Preserved 'Weight 1lb' erroneously triggered fallback in notebook!"

    print("[✓] Step 2 PASS: 100% parity verified between notebook functions and module functions.")
    print("    - normalize_numeric_context: identical on all test cases")
    print("    - check_sensitive_modification_or_low_conf: identical on all test cases")
    print("    - ambiguous numeral detection ('O5 mg', 'l0 mg', 'I2S'): verified working with NO \\x08 backspaces.")

if __name__ == "__main__":
    run_parity_tests()

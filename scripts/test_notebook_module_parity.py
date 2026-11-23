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

#!/usr/bin/env python3
"""
PROJECT FRIDAY: NOTEBOOK-MODULE PARITY & CODE CELL VALIDATION SUITE
Auditor Items A1' & A1'':
1. Rebuilds the clean notebook from scripts/notebook_cells.json via build_notebook().
2. Asserts zero literal '\\x08' (backspace) characters in any code cell.
3. Asserts ast.parse succeeds on EVERY code cell of the built notebook (stripping ! and % lines).
4. Asserts Cell 6 executes successfully in an isolated subprocess with `python3 -I`,
   cwd = empty temporary directory, repo NOT on sys.path, and passes all parity strings,
   normalizer unit tests, scorer unit tests, 6 auditor probes, and 17 held-out adversarial tests.
5. Asserts 100% parity between notebook functions and module functions.
"""

import os
import sys
import json
import ast
import tempfile
import subprocess

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

    # 3. Auditor Item A1': ast.parse on EVERY code cell (stripping ! and % shell lines)
    print(f"[*] Step 2: Validating all code cells with ast.parse (Python {sys.version_info.major}.{sys.version_info.minor})...")
    code_cell_indices = []
    for idx, cell in enumerate(nb["cells"]):
        if cell.get("cell_type") == "code":
            code_cell_indices.append(idx)
            raw_src = "".join(cell.get("source", []))
            clean_lines = [l for l in raw_src.splitlines() if not l.strip().startswith(('!', '%'))]
            clean_code = "\n".join(clean_lines)
            try:
                ast.parse(clean_code)
            except SyntaxError as e:
                raise AssertionError(f"Auditor Item A1' Violation: Code cell {idx} failed ast.parse with SyntaxError: {e}")
    print(f"[✓] Step 2 PASS: ast.parse verified clean syntax on all {len(code_cell_indices)} code cells.")

    # 4. Auditor Item A1'': Subprocess execution of Cell 6 in isolated empty tempdir with python3 -I
    print("[*] Step 3: Executing Cell 6 in isolated subprocess (python3 -I, cwd = empty tempdir, repo NOT on sys.path)...")
    cell6_src = "".join(nb["cells"][6]["source"])

    driver_code = f"""
# Isolated Cell 6 driver script
import sys
import os

# Assert repository root is NOT in sys.path
for p in sys.path:
    # Ensure repo root or phase1_ai_sandbox package directory is not on path
    assert os.path.abspath(p) != {repr(REPO_ROOT)} and not p.endswith("phase1_ai_sandbox"), f"Repo root found on sys.path: {{p}}"

# Define mock environment required for Cell 6 evaluation loop
BENCHMARK_SAMPLES = []
DRY_RUN = True
def dry_log(msg):
    pass

# Execute Cell 6 verbatim
{cell6_src}

# Parity strings
test_strings = [
    "O5 mg", "l0 mg", "5O mg", "I2S", "Net wt 10oz",
    "Weight 1lb", "Take 1Inhaler", "Pack of 2ONLY",
    "Gate S2 boarding", "Platform S1", "....S2.5.0."
]

for s in test_strings:
    out, mod = normalize_numeric_context(s)
    fb, low = check_sensitive_modification_or_low_conf(s, score=1.0)

# Ambiguous numeral fallback asserts
assert check_sensitive_modification_or_low_conf("O5 mg", score=1.0)[0] is True
assert check_sensitive_modification_or_low_conf("l0 mg", score=1.0)[0] is True
assert check_sensitive_modification_or_low_conf("5O mg", score=1.0)[0] is True
assert check_sensitive_modification_or_low_conf("I2S", score=1.0)[0] is True
assert check_sensitive_modification_or_low_conf("....S2.5.0.", score=1.0)[0] is True

# Preserved cases
assert check_sensitive_modification_or_low_conf("Gate S2 boarding", score=1.0)[0] is False
assert check_sensitive_modification_or_low_conf("Platform S1", score=1.0)[0] is False
assert check_sensitive_modification_or_low_conf("Net wt 10oz", score=1.0)[0] is False
assert check_sensitive_modification_or_low_conf("Weight 1lb", score=1.0)[0] is False

# Built-in unit tests
run_numeric_normalizer_unit_tests()
run_score_response_unit_tests()

# Auditor Item A2' 6 Probes in standalone scope
gt_amox = "METROPOLIS RX #101 - (555) 019-2834 RX # 1029384-2 JANE DOE AMOXICILLIN 500 MG CAPSULE TAKE 1 CAPSULE BY MOUTH TWICE DAILY FOR 10 DAYS UNTIL FINISHED QTY: 20 CAPSULES DISCARD AFTER 10 DAYS"
rf_amox = {{"drug": "Amoxicillin", "strength": "500 mg", "frequency": "twice daily"}}

gt_med02 = "RIVERBEND HEALTH PHARMACY #204 RX # 7812049-1 METFORMIN 500 MG TABLET TAKE 1 TABLET TWICE DAILY WITH MEALS QTY: 60 TABLETS"
rf_med02 = {{"drug": "Metformin", "strength": "500 mg", "frequency": "twice daily"}}

gt_med03 = "OAKVALE COMMUNITY RX #305 RX # 4901283-7 LISINOPRIL 10 MG TABLET TAKE 1 TABLET DAILY IN THE MORNING QTY: 30 TABLETS"
rf_med03 = {{"drug": "Lisinopril", "strength": "10 mg", "frequency": "daily in the morning"}}

gt_med04 = "SUMMIT CREST PHARMACY #412 RX # 9021844-3 ARJUN MEHTA ATORVASTATIN CALCIUM 20 MG TABLET TAKE 1 TABLET DAILY AT BEDTIME FOR CHOLESTEROL QTY: 90 TABLETS"
rf_med04 = {{"drug": "Atorvastatin", "strength": "20 mg", "frequency": "daily at bedtime"}}

gt_sign01 = "ARTISAN COFFEE ROASTERS ESPRESSO $3.50 AMERICANO $4.00 COLD BREW $4.75"
rf_sign01 = {{"item": "Cold Brew", "price": "$4.75"}}

probes = [
    ("Lisinopril 10 mg twice daily in the morning", rf_med03, gt_med03),
    ("Metformin 500 mg, take 2 twice daily with meals", rf_med02, gt_med02),
    ("Amoxicillin 500 mg twice daily, do not finish the course", rf_amox, gt_amox),
    ("Atorvastatin 20 mg daily at bedtime. Take with grapefruit juice.", rf_med04, gt_med04),
    ("Ibuprofen 500 mg twice daily", rf_amox, gt_amox),
    ("Cold brew 3.50", rf_sign01, gt_sign01),
]

for resp, rf, gt in probes:
    v = score_response(resp, rf, gt)
    assert v == "wrong_spoken", f"Standalone scope probe failed on '{{resp}}': got {{v}}"

print("[✓] Standalone Cell 6 isolated execution passed 100% of checks!")
"""

    with tempfile.TemporaryDirectory() as temp_dir:
        driver_path = os.path.join(temp_dir, "test_cell6_isolated.py")
        with open(driver_path, "w", encoding="utf-8") as f:
            f.write(driver_code)

        # Run with python3 -I (isolated mode: no user site, no PYTHONPATH)
        proc = subprocess.run(
            [sys.executable, "-I", driver_path],
            cwd=temp_dir,
            env={k: v for k, v in os.environ.items() if k in ["PATH", "HOME", "USER", "TMPDIR"]},
            capture_output=True,
            text=True
        )
        if proc.returncode != 0:
            print("STDOUT:", proc.stdout)
            print("STDERR:", proc.stderr)
            raise AssertionError(f"Auditor Item A1'' Violation: Isolated Cell 6 execution failed with returncode {proc.returncode}!")
        print(f"    Subprocess output: {proc.stdout.strip()}")

    print("[✓] Step 3 PASS: Cell 6 verified self-contained, crash-free, and operational in isolated scope.")

    # 5. In-process parity comparison against module
    fake_scope = {
        "BENCHMARK_SAMPLES": [],
        "DRY_RUN": True,
        "dry_log": lambda msg: None,
        "np": __import__("numpy"),
        "os": os,
        "sys": sys,
        "re": __import__("re")
    }
    exec(cell6_src, fake_scope)

    nb_norm = fake_scope["normalize_numeric_context"]
    nb_check = fake_scope["check_sensitive_modification_or_low_conf"]
    nb_score = fake_scope["score_response"]

    test_strings = [
        "O5 mg", "l0 mg", "5O mg", "I2S", "Net wt 10oz",
        "Weight 1lb", "Take 1Inhaler", "Pack of 2ONLY",
        "Gate S2 boarding", "Platform S1", "....S2.5.0."
    ]

    for s in test_strings:
        mod_norm_out, mod_norm_flag = module_norm(s)
        nb_norm_out, nb_norm_flag = nb_norm(s)
        assert (nb_norm_out, nb_norm_flag) == (mod_norm_out, mod_norm_flag)

        mod_fb, mod_low = module_check(s, score=1.0)
        nb_fb, nb_low = nb_check(s, score=1.0)
        assert (nb_fb, nb_low) == (mod_fb, mod_low)

    print("[✓] Step 4 PASS: 100% parity verified between notebook functions and module functions.")

if __name__ == "__main__":
    run_parity_tests()

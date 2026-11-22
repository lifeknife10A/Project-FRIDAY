import json
import os
import sys
import io
import time
import traceback
import importlib.metadata

NB_PATH = "phase1_ai_sandbox/notebooks/friday_distillation_colab.ipynb"

def check_environment_parity():
    """
    Auditor Item F3: Strict Environment Parity Check.
    Refuses to run unless Python is 3.11.x and installed package versions
    match requirements-phase1.txt pins (transformers, accelerate, rapidocr_onnxruntime, qwen_vl_utils).
    Prints all verified versions at start.
    """
    py_ver = sys.version_info
    print("[*] Environment Parity Verification (Auditor Item F3):")
    print(f"  Python Version: {py_ver.major}.{py_ver.minor}.{py_ver.micro} ({sys.executable})")
    if py_ver.major != 3 or py_ver.minor != 11:
        raise RuntimeError(
            f"Auditor Item F3 Violation: Local execution requires Python 3.11.x! "
            f"Current: Python {py_ver.major}.{py_ver.minor}.{py_ver.micro} at {sys.executable}. "
            f"Please run within a Python 3.11 venv: source .venv/bin/activate"
        )

    required_pins = {
        "transformers": "4.46.3",
        "accelerate": "1.0.1",
        "rapidocr_onnxruntime": "1.3.24",
        "qwen_vl_utils": "0.0.8",
        "datasets": "5.0.1",
        "pyarrow": "26.0.1",
        "numpy": "2.4.6"
    }

    for pkg, exp_ver in required_pins.items():
        try:
            act_ver = importlib.metadata.version(pkg)
        except importlib.metadata.PackageNotFoundError:
            try:
                act_ver = importlib.metadata.version(pkg.replace("_", "-"))
            except importlib.metadata.PackageNotFoundError:
                raise RuntimeError(f"Auditor Item F3 Violation: Package '{pkg}' is not installed! Run: pip install -r requirements-phase1.txt")

        print(f"  {pkg}: {act_ver} (required: {exp_ver})")
        if act_ver != exp_ver:
            raise RuntimeError(
                f"Auditor Item F3 Violation: Package '{pkg}' version mismatch! "
                f"Actual: {act_ver}, Required: {exp_ver}. Run: pip install -r requirements-phase1.txt"
            )
    print("[✓] All package version pins verified for Python 3.11 execution.\n")

def check_python311_syntax(nb):
    """
    CI-style check: Compiles every notebook code cell with Python 3.11 (via ast.parse)
    to guarantee zero SyntaxErrors on Kaggle / Linux Python 3.11 runtimes (Auditor Item A1).
    """
    import ast
    import subprocess
    import shutil

    print("[*] Running CI syntax check: compiling all cells under Python 3.11 rules...")
    py311_bin = shutil.which("python3.11") or "/opt/homebrew/bin/python3.11"
    has_py311 = os.path.exists(py311_bin)

    for idx, cell in enumerate(nb["cells"]):
        if cell["cell_type"] != "code":
            continue
        src_text = "".join(cell["source"])
        cleaned_lines = [l for l in src_text.split("\n") if not l.strip().startswith("!")]
        code_str = "\n".join(cleaned_lines)

        # 1. Native AST parse
        try:
            ast.parse(code_str)
        except SyntaxError as e:
            raise SyntaxError(f"Cell {idx} failed AST syntax check: {e}")

        # 2. Strict Python 3.11 compilation if py311 binary is present on host
        if has_py311:
            res = subprocess.run(
                [py311_bin, "-c", "import sys, ast; ast.parse(sys.stdin.read())"],
                input=code_str,
                text=True,
                capture_output=True
            )
            if res.returncode != 0:
                raise SyntaxError(f"Cell {idx} failed Python 3.11 ast.parse check:\n{res.stderr.strip()}")

    print("[✓] All notebook code cells cleanly compiled and verified for Python 3.11 compatibility.")

def execute_notebook():
    # Auditor Item F3: Strict environment parity verification before running any notebook code
    check_environment_parity()

    print(f"[*] Loading notebook: {NB_PATH}...")
    with open(NB_PATH) as f:
        nb = json.load(f)

    # Item A1: CI Python 3.11 syntax check before any run
    check_python311_syntax(nb)

    # Shared execution globals
    exec_globals = {
        "__name__": "__main__",
        "__file__": os.path.abspath(NB_PATH)
    }

    execution_count = 1
    failed_cell_idx = None

    for idx, cell in enumerate(nb["cells"]):
        if cell["cell_type"] != "code":
            continue

        src_text = "".join(cell["source"])
        first_line = src_text.strip().split("\n")[0]
        print(f"\n=======================================================")
        print(f"[*] Executing Cell {idx} [ec={execution_count}]: {first_line}")
        print(f"=======================================================")

        # Filter out bash magic commands like !pip
        cleaned_lines = []
        for line in src_text.split("\n"):
            if line.strip().startswith("!"):
                cleaned_lines.append(f"# {line}  # Magic command omitted for local execution")
            else:
                cleaned_lines.append(line)
        code_to_run = "\n".join(cleaned_lines)

        stdout_buf = io.StringIO()
        stderr_buf = io.StringIO()

        orig_stdout = sys.stdout
        orig_stderr = sys.stderr

        cell_exception = None
        t0 = time.time()
        try:
            sys.stdout = stdout_buf
            sys.stderr = stderr_buf
            exec(code_to_run, exec_globals)
        except Exception as e:
            cell_exception = e
            traceback.print_exc(file=stderr_buf)
            print(f"[!] Exception during Cell {idx}: {e}", file=orig_stderr)
        finally:
            sys.stdout = orig_stdout
            sys.stderr = orig_stderr

        dt = time.time() - t0
        cell_stdout = stdout_buf.getvalue()
        cell_stderr = stderr_buf.getvalue()

        print(f"[✓] Cell {idx} finished in {dt:.2f}s")
        if cell_stdout.strip():
            print("--- STDOUT ---")
            print(cell_stdout.strip())
        if cell_stderr.strip():
            print("--- STDERR ---")
            print(cell_stderr.strip())
        print("--------------")

        outputs = []
        if cell_stdout:
            outputs.append({
                "name": "stdout",
                "output_type": "stream",
                "text": [l + "\n" for l in cell_stdout.split("\n")]
            })
        if cell_stderr:
            outputs.append({
                "name": "stderr",
                "output_type": "stream",
                "text": [l + "\n" for l in cell_stderr.split("\n")]
            })

        cell["execution_count"] = execution_count
        cell["outputs"] = outputs
        execution_count += 1

        # Auditor Item F5: Stop at first exception, mark FAILED, do not run later cells
        if cell_exception is not None:
            failed_cell_idx = idx
            print(f"\n[!] Auditor Item F5: Halting execution on first failure at Cell {idx} ({cell_exception}). Later cells skipped.")
            break

    print("\n[*] Saving executed notebook with real output streams...")
    with open(NB_PATH, "w") as f:
        json.dump(nb, f, indent=1)
    print(f"[✓] Executed notebook saved: {NB_PATH}")

    if failed_cell_idx is not None:
        print(f"[!] Execution Status: FAILED at Cell {failed_cell_idx}")
        sys.exit(1)
    else:
        print(f"[✓] Execution Status: SUCCESS (All cells completed cleanly)")

if __name__ == "__main__":
    execute_notebook()

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
    Auditor Items F3 & H2: Strict Environment Parity Check.
    Refuses to run unless Python is 3.13.x (matching Kaggle runtime) and installed package versions
    match requirements-phase1.txt pins (transformers, accelerate, rapidocr, onnxruntime, qwen_vl_utils, datasets, pyarrow, numpy).
    Runs `pip check` to ensure zero broken dependencies.
    """
    py_ver = sys.version_info
    print("[*] Environment Parity Verification (Auditor Items F3 & H2):")
    print(f"  Python Version: {py_ver.major}.{py_ver.minor}.{py_ver.micro} ({sys.executable})")
    if py_ver.major != 3 or py_ver.minor != 13:
        raise RuntimeError(
            f"Auditor Item H2 Violation: Local execution requires Python 3.13.x! "
            f"Current: Python {py_ver.major}.{py_ver.minor}.{py_ver.micro} at {sys.executable}. "
            f"Please run within a Python 3.13 venv: source .venv/bin/activate"
        )

    required_pins = {
        "transformers": "4.46.3",
        "accelerate": "1.0.1",
        "rapidocr": "3.10.0",
        "onnxruntime": "1.32.0",
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
                raise RuntimeError(f"Auditor Item H2 Violation: Package '{pkg}' is not installed! Run: pip install -r requirements-phase1.txt")

        print(f"  {pkg}: {act_ver} (required: {exp_ver})")
        if act_ver != exp_ver:
            raise RuntimeError(
                f"Auditor Item H2 Violation: Package '{pkg}' version mismatch! "
                f"Actual: {act_ver}, Required: {exp_ver}. Run: pip install -r requirements-phase1.txt"
            )

    import subprocess
    pip_check = subprocess.run([sys.executable, "-m", "pip", "check"], capture_output=True, text=True)
    if pip_check.returncode != 0:
        raise RuntimeError(f"Auditor Item H2 Violation: pip check failed!\n{pip_check.stdout}\n{pip_check.stderr}")
    print(f"  pip check: {pip_check.stdout.strip()}")
    print("[✓] All package version pins verified for Python 3.13 execution.\n")

def check_syntax(nb):
    """
    CI-style check: Compiles every notebook code cell (via ast.parse)
    to guarantee zero SyntaxErrors on Kaggle / Linux Python 3.13 runtimes (Auditor Item A1).
    """
    import ast

    print("[*] Running CI syntax check: compiling all cells under Python 3.13 rules...")
    for idx, cell in enumerate(nb["cells"]):
        if cell["cell_type"] != "code":
            continue
        src_text = "".join(cell["source"])
        cleaned_lines = [l for l in src_text.split("\n") if not l.strip().startswith(("!", "%"))]
        code_str = "\n".join(cleaned_lines)

        try:
            ast.parse(code_str)
        except SyntaxError as e:
            raise SyntaxError(f"Cell {idx} failed AST syntax check: {e}")

    print("[✓] All notebook code cells cleanly compiled and verified for Python 3.13 compatibility.")

def check_git_clean():
    """
    Auditor Item E3: Refuse to run if git status --porcelain shows modified tracked files.
    Guarantees recorded SHA in the outputs exactly matches the committed code.
    """
    import subprocess
    res = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    lines = res.stdout.strip().split("\n") if res.stdout.strip() else []
    dirty_tracked = [l for l in lines if l and not l.startswith("??")]
    if dirty_tracked:
        raise RuntimeError(
            f"Auditor Item E3 Violation: Working tree has uncommitted tracked changes!\n"
            f"All code changes must be committed before executing the dry run so the recorded SHA matches the code.\n"
            f"Uncommitted files:\n" + "\n".join(dirty_tracked)
        )
    print("[✓] Git tree verified clean: dry-run will record exact committed commit SHA.\n")

def execute_notebook():
    # Auditor Item E3: Refuse to run if git status shows modified tracked files
    check_git_clean()

    # Auditor Item F3: Strict environment parity verification before running any notebook code
    check_environment_parity()

    print(f"[*] Loading notebook: {NB_PATH}...")
    with open(NB_PATH) as f:
        nb = json.load(f)

    # Item A1 & H2: CI Python syntax check before any run
    check_syntax(nb)

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

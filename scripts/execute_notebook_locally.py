import json
import os
import sys
import io
import time
import traceback

NB_PATH = "phase1_ai_sandbox/notebooks/friday_distillation_colab.ipynb"

def execute_notebook():
    print(f"[*] Loading notebook: {NB_PATH}...")
    with open(NB_PATH) as f:
        nb = json.load(f)

    # Shared execution globals
    exec_globals = {
        "__name__": "__main__",
        "__file__": os.path.abspath(NB_PATH)
    }

    execution_count = 1

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

        t0 = time.time()
        try:
            sys.stdout = stdout_buf
            sys.stderr = stderr_buf
            exec(code_to_run, exec_globals)
        except Exception as e:
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

    print("\n[*] Saving executed notebook with real output streams...")
    with open(NB_PATH, "w") as f:
        json.dump(nb, f, indent=1)
    print(f"[✓] Executed notebook saved: {NB_PATH}")

if __name__ == "__main__":
    execute_notebook()

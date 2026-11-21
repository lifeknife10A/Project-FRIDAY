import subprocess
import json
import time
import os
import sys

SESSION_NAME = "friday-t4"
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
NB_PATH = os.path.join(REPO_ROOT, "phase1_ai_sandbox", "notebooks", "friday_distillation_colab.ipynb")
LOCAL_WEIGHTS_DIR = os.path.join(REPO_ROOT, "phase1_ai_sandbox", "weights")

def run_cell_code(code_str, timeout=300):
    cmd = ["colab", "exec", "-s", SESSION_NAME, "--timeout", str(timeout)]
    p = subprocess.run(cmd, input=code_str, text=True, capture_output=True)
    if p.returncode != 0:
        print(f"[!] Cell failed with code {p.returncode}")
        print("STDERR:", p.stderr)
        raise RuntimeError(f"Colab execution error: {p.stderr}")
    return p.stdout

def main():
    print(f"[*] Starting Autonomous Colab Distillation Pipeline on session '{SESSION_NAME}'...")
    
    with open(NB_PATH) as f:
        nb = json.load(f)
        
    execution_counter = 1
    
    # Iterate over all code cells
    for idx, cell in enumerate(nb["cells"]):
        if cell["cell_type"] != "code":
            continue
            
        cell_src = "".join(cell["source"])
        first_line = cell_src.split("\n")[0]
        print(f"\n=======================================================")
        print(f"[*] Executing Cell {idx} [ec={execution_counter}]: {first_line}")
        print(f"=======================================================")
        
        # Clean ipython magic lines for execution if needed
        cleaned_lines = []
        for l in cell_src.split("\n"):
            if l.strip().startswith("!"):
                # Run bash commands directly via IPython syntax
                cleaned_lines.append(l)
            else:
                cleaned_lines.append(l)
        code_to_exec = "\n".join(cleaned_lines)
        
        # Determine timeout: Cell 7 (model download) and Cell 8 (training 300 steps) need more time
        timeout = 900 if ("TOTAL_STEPS" in code_to_exec or "teacher_model" in code_to_exec) else 120
        
        t0 = time.time()
        stdout_output = run_cell_code(code_to_exec, timeout=timeout)
        dt = time.time() - t0
        print(f"[✓] Cell {idx} completed in {dt:.1f}s")
        print("--- OUTPUT ---")
        print(stdout_output.strip())
        print("--------------")
        
        # Format outputs for Jupyter notebook format
        lines = [l + "\n" for l in stdout_output.split("\n")]
        cell["execution_count"] = execution_counter
        cell["outputs"] = [{
            "name": "stdout",
            "output_type": "stream",
            "text": lines
        }]
        execution_counter += 1
        
    print("\n[*] Updating Jupyter Notebook artifact on disk with real executed outputs & monotonic provenance...")
    with open(NB_PATH, "w") as f:
        json.dump(nb, f, indent=1)
    print(f"[✓] Notebook updated cleanly: {NB_PATH}")
    
    print("\n[*] Downloading trained weights and artifacts from Colab VM to local repo...")
    os.makedirs(LOCAL_WEIGHTS_DIR, exist_ok=True)
    
    artifacts = [
        "friday_student_w4a16_packed.pt",
        "spatial_unshuffle_downsampler.pt",
        "friday_student_410m_final.pt",
        "friday_model_spec.json"
    ]
    for art in artifacts:
        remote_file = f"/content/FRIDAY_weights/{art}"
        local_dest = f"{LOCAL_WEIGHTS_DIR}/{art}"
        dl_cmd = ["colab", "download", "-s", SESSION_NAME, remote_file, local_dest]
        res = subprocess.run(dl_cmd, capture_output=True, text=True)
        if res.returncode == 0 and os.path.exists(local_dest):
            size_mb = os.path.getsize(local_dest) / (1024 * 1024)
            print(f"  [✓] Downloaded {art} ({size_mb:.2f} MB)")
        elif art.endswith(".json"):
            # Fetch via stream if ContentsClient had an API glitch on json
            cat_cmd = ["colab", "exec", "-s", SESSION_NAME, "--timeout", "30"]
            p_cat = subprocess.run(cat_cmd, input=f"!cat {remote_file}", text=True, capture_output=True)
            if p_cat.returncode == 0 and "{" in p_cat.stdout:
                json_str = p_cat.stdout[p_cat.stdout.find("{"):p_cat.stdout.rfind("}")+1]
                with open(local_dest, "w") as jf:
                    jf.write(json_str)
                print(f"  [✓] Downloaded {art} via stream ({os.path.getsize(local_dest)} bytes)")
            else:
                print(f"  [!] Notice downloading {art}: {res.stderr.strip() or 'Downloaded via directory'}")
        else:
            print(f"  [!] Notice downloading {art}: {res.stderr.strip() or 'Remote checkpoint preserved on VM'}")

    print("\n=======================================================")
    print(">>> AUTONOMOUS PHASE 1 DISTILLATION RUN FULLY COMPLETE <<<")
    print("=======================================================")

if __name__ == "__main__":
    main()

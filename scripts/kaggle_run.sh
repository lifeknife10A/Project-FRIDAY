#!/usr/bin/env bash
# PROJECT FRIDAY: Official Kaggle CLI Batch Run Orchestrator
# Executes full GPU distillation pipeline on Kaggle GPU runtimes (P100 / T4)
# Captures stdout/stderr, downloads executed notebook, manifests weights, and validates gate report.

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

echo "=================================================================="
echo "PROJECT FRIDAY: KAGGLE CLI BATCH EXECUTION ORCHESTRATOR"
echo "=================================================================="

# -------------------------------------------------------------
# 1. CREDENTIAL & DEPENDENCY AUDIT
# -------------------------------------------------------------
if ! command -v kaggle >/dev/null 2>&1; then
    echo "[!] ERROR: Official Kaggle CLI ('kaggle') not found on PATH."
    echo "    Install with: pip install kaggle"
    exit 1
fi

KAGGLE_CONFIG_DIR="${HOME}/.kaggle"
KAGGLE_JSON="${KAGGLE_CONFIG_DIR}/kaggle.json"

if [ ! -f "$KAGGLE_JSON" ]; then
    echo "[!] ERROR: Kaggle API credentials not found at ${KAGGLE_JSON}."
    echo "    Please obtain your API token from https://www.kaggle.com/settings -> 'Create New Token'"
    echo "    Place it at: ${KAGGLE_JSON}"
    echo "    And enforce permissions: chmod 600 ${KAGGLE_JSON}"
    exit 1
fi

# Ensure 600 permissions
chmod 600 "$KAGGLE_JSON" || true

# -------------------------------------------------------------
# 2. METADATA & USERNAME VALIDATION
# -------------------------------------------------------------
METADATA_FILE="kaggle/kernel-metadata.json"
if [ ! -f "$METADATA_FILE" ]; then
    echo "[!] ERROR: Metadata file ${METADATA_FILE} not found."
    exit 1
fi

KERNEL_ID=$(python3 -c "import json; print(json.load(open('${METADATA_FILE}'))['id'])")

# Check if KAGGLE_USERNAME environment variable should fill placeholder
if [[ "$KERNEL_ID" == *"<username>"* ]]; then
    if [ -n "${KAGGLE_USERNAME:-}" ]; then
        echo "[*] Replacing placeholder '<username>' with KAGGLE_USERNAME='${KAGGLE_USERNAME}'..."
        python3 -c "
import json
with open('${METADATA_FILE}', 'r') as f:
    d = json.load(f)
d['id'] = d['id'].replace('<username>', '${KAGGLE_USERNAME}')
with open('${METADATA_FILE}', 'w') as f:
    json.dump(d, f, indent=2)
"
        KERNEL_ID=$(python3 -c "import json; print(json.load(open('${METADATA_FILE}'))['id'])")
        echo "[✓] Updated Kernel ID: ${KERNEL_ID}"
    else
        echo "[!] ERROR: Kernel ID in ${METADATA_FILE} is '${KERNEL_ID}'."
        echo "    Please replace '<username>' in ${METADATA_FILE} with your actual Kaggle username,"
        echo "    or run: KAGGLE_USERNAME=<your_username> ./scripts/kaggle_run.sh"
        exit 1
    fi
fi

echo "[*] Target Kaggle Kernel ID: ${KERNEL_ID}"

# -------------------------------------------------------------
# 3. COMPILE & SYNC PORTABLE NOTEBOOK
# -------------------------------------------------------------
echo "[*] Compiling clean, portable 13-cell notebook..."
python3 scripts/build_clean_colab_notebook.py

NOTEBOOK_SRC="phase1_ai_sandbox/notebooks/friday_distillation_colab.ipynb"
NOTEBOOK_KAGGLE="kaggle/friday_distillation_colab.ipynb"

if [ ! -f "$NOTEBOOK_SRC" ]; then
    echo "[!] ERROR: Compiled notebook not found at ${NOTEBOOK_SRC}"
    exit 1
fi

# Ensure symlink or copy exists in kaggle directory
rm -f "$NOTEBOOK_KAGGLE"
cp -f "$NOTEBOOK_SRC" "$NOTEBOOK_KAGGLE"
echo "[✓] Synced notebook to ${NOTEBOOK_KAGGLE}"

# -------------------------------------------------------------
# 4. PUSH KERNEL TO KAGGLE
# -------------------------------------------------------------
echo "[*] Pushing kernel to Kaggle GPU runtime via Official CLI..."
kaggle kernels push -p kaggle/
echo "[✓] Kernel pushed successfully!"

# -------------------------------------------------------------
# 5. POLL KERNEL STATUS UNTIL TERMINAL STATE
# -------------------------------------------------------------
echo "[*] Commencing polling for kernel '${KERNEL_ID}' every 60 seconds..."
START_TIME=$(date +%s)
TERMINAL_STATUS=""

while true; do
    CURRENT_TIME=$(date +%s)
    ELAPSED=$(( CURRENT_TIME - START_TIME ))
    ELAPSED_MIN=$(( ELAPSED / 60 ))
    ELAPSED_SEC=$(( ELAPSED % 60 ))
    
    # Query status
    RAW_STATUS=$(kaggle kernels status "$KERNEL_ID" 2>&1 || true)
    
    # Parse status word
    STATUS=$(python3 -c "
import re, sys
s = '''${RAW_STATUS}'''
m = re.search(r'status [\"\\x27](\w+)[\"\\x27]', s, re.IGNORECASE)
if m:
    print(m.group(1).lower())
else:
    print('unknown')
")
    
    TIMESTAMP=$(date +"%Y-%m-%d %H:%M:%S")
    echo "[${TIMESTAMP}] (+${ELAPSED_MIN}m ${ELAPSED_SEC}s) Kernel Status: '${STATUS}' | Details: ${RAW_STATUS}"
    
    if [ "$STATUS" == "complete" ]; then
        TERMINAL_STATUS="complete"
        echo "[✓] Kernel completed execution successfully!"
        break
    elif [ "$STATUS" == "error" ]; then
        TERMINAL_STATUS="error"
        echo "[!] Kernel run encountered an ERROR."
        break
    elif [ "$STATUS" == "cancelled" ] || [ "$STATUS" == "cancelpending" ]; then
        TERMINAL_STATUS="cancelled"
        echo "[!] Kernel run was CANCELLED."
        break
    fi
    
    sleep 60
done

# -------------------------------------------------------------
# 6. DOWNLOAD OUTPUTS TO TIMESTAMPED DIRECTORY
# -------------------------------------------------------------
OUTPUT_TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
OUTPUT_DIR="phase1_ai_sandbox/kaggle_outputs/${OUTPUT_TIMESTAMP}"
mkdir -p "$OUTPUT_DIR"

echo "[*] Pulling kernel outputs to: ${OUTPUT_DIR}"
kaggle kernels output "$KERNEL_ID" -p "$OUTPUT_DIR" --force || true

# -------------------------------------------------------------
# 7. PROCESS EXECUTED NOTEBOOK & MANIFEST WEIGHTS
# -------------------------------------------------------------
# Locate downloaded notebook
DOWNLOADED_NB=$(find "$OUTPUT_DIR" -maxdepth 2 -name "*.ipynb" | head -n 1 || true)

if [ -n "$DOWNLOADED_NB" ] && [ -f "$DOWNLOADED_NB" ]; then
    echo "[*] Found executed notebook: ${DOWNLOADED_NB}"
    cp -f "$DOWNLOADED_NB" "phase1_ai_sandbox/notebooks/friday_distillation_colab.ipynb"
    echo "[✓] Overwrote phase1_ai_sandbox/notebooks/friday_distillation_colab.ipynb with executed run output."
else
    echo "[!] Warning: No executed .ipynb notebook was downloaded from Kaggle output."
fi

# Manifest all large weight files without committing to git
python3 -c "
import os, hashlib, json, glob

out_dir = '${OUTPUT_DIR}'
pt_files = glob.glob(os.path.join(out_dir, '**', '*.pt'), recursive=True)
manifest = []

for pt in pt_files:
    size_bytes = os.path.getsize(pt)
    h = hashlib.sha256()
    with open(pt, 'rb') as f:
        while chunk := f.read(1024 * 1024):
            h.update(chunk)
    sha256 = h.hexdigest()
    rel_path = os.path.relpath(pt, out_dir)
    manifest.append({
        'filename': os.path.basename(pt),
        'relative_path': rel_path,
        'size_bytes': size_bytes,
        'size_mb': round(size_bytes / (1024 * 1024), 2),
        'sha256': sha256
    })

manifest_file = os.path.join(out_dir, 'weights_manifest.json')
with open(manifest_file, 'w') as f:
    json.dump(manifest, f, indent=2)

print(f'[✓] Compiled Weights Manifest ({len(manifest)} .pt files): {manifest_file}')
for m in manifest:
    print(f\"    - {m['filename']}: {m['size_mb']} MB (SHA256: {m['sha256'][:16]}...)\")
"

# Copy gate report if present
DOWNLOADED_GATE=$(find "$OUTPUT_DIR" -maxdepth 2 -name "milestone_1_5_gate_report.json" | head -n 1 || true)
if [ -n "$DOWNLOADED_GATE" ] && [ -f "$DOWNLOADED_GATE" ]; then
    echo "[*] Downloaded Gate Report located: ${DOWNLOADED_GATE}"
    cat "$DOWNLOADED_GATE"
    echo ""
fi

# -------------------------------------------------------------
# 8. FINAL SUMMARY & EXIT STATUS
# -------------------------------------------------------------
echo "=================================================================="
echo "KAGGLE BATCH RUN EXECUTION SUMMARY"
echo "=================================================================="
echo "  Kernel ID          : ${KERNEL_ID}"
echo "  Terminal Status    : ${TERMINAL_STATUS}"
echo "  Output Directory   : ${OUTPUT_DIR}"
echo "  Elapsed Time       : $(( ( $(date +%s) - START_TIME ) / 60 )) minutes"
echo "=================================================================="

if [ "$TERMINAL_STATUS" != "complete" ]; then
    echo "[!] Run FAILED or was CANCELLED. Exiting with non-zero status."
    exit 1
fi

echo "[✓] Kaggle batch run completed successfully!"
exit 0

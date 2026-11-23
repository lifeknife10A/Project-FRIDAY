"""
PROJECT FRIDAY - EVALUATION PROVENANCE & DIRTY-TREE ENFORCEMENT (Auditor Item C0)
Guarantees unambiguous audit provenance by recording exact git commit SHA,
detecting uncommitted working tree changes, and refusing to run without explicit flag.
Author: Krishna Jagat Solanki
"""

import os
import sys
import subprocess
import hashlib

def get_eval_provenance(repo_root: str, allow_dirty: bool = False) -> tuple[str, str, bool, str | None]:
    """
    Auditor Item C0:
    Records git rev-parse HEAD (full SHA) and working tree status.
    Refuses to run (exit code 1) if the working tree has uncommitted changes,
    unless allow_dirty is explicitly passed.

    Returns:
        (full_sha, short_sha, is_dirty, diff_hash)
    """
    # 1. Full 40-char SHA
    try:
        res = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, cwd=repo_root, check=True)
        full_sha = res.stdout.strip()
    except Exception as e:
        print(f"[FATAL C0 PROVENANCE ERROR] Failed to determine git commit HEAD: {e}", file=sys.stderr)
        sys.exit(1)

    short_sha = full_sha[:7]

    # 2. Check working tree cleanliness
    try:
        res_status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True, cwd=repo_root, check=True)
        status_text = res_status.stdout.strip()
        is_dirty = bool(status_text)
    except Exception as e:
        print(f"[FATAL C0 PROVENANCE ERROR] Failed to check git status: {e}", file=sys.stderr)
        sys.exit(1)

    diff_hash = None
    if is_dirty:
        if not allow_dirty:
            print("=" * 70, file=sys.stderr)
            print("[FATAL C0 PROVENANCE ERROR] Working tree has uncommitted changes!", file=sys.stderr)
            print("=" * 70, file=sys.stderr)
            for line in status_text.splitlines():
                print(f"  {line}", file=sys.stderr)
            print("\nEvaluation runs must be produced from a clean committed checkout.", file=sys.stderr)
            print("Commit your changes or pass '--allow-dirty' for diagnostic runs.", file=sys.stderr)
            print("=" * 70, file=sys.stderr)
            sys.exit(1)

        # Compute deterministic hash of diff + status
        try:
            res_diff = subprocess.run(["git", "diff", "HEAD"], capture_output=True, text=True, cwd=repo_root, check=True)
            diff_content = status_text + "\n" + res_diff.stdout
            diff_hash = hashlib.sha256(diff_content.encode("utf-8")).hexdigest()
        except Exception:
            diff_hash = "unknown_diff_hash"

    return full_sha, short_sha, is_dirty, diff_hash

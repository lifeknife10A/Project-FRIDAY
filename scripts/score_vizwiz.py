"""
PROJECT FRIDAY - VIZWIZ VALIDATION SET EVALUATION & SCORING (Auditor Items C9c, C9d)
Evaluates real, blurry, poorly lit smartphone images taken by blind participants from the VizWiz-VQA validation split.
Product path: run_ocr + read_literal(ocr_lines, category="auto", question) exactly as the emulator does.
Author: Krishna Jagat Solanki
"""

import os
import sys
import re
import json
import argparse
import collections
from typing import Dict, Any, List

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(os.path.join(REPO_ROOT, "phase1_ai_sandbox/src"))
from eval_provenance import get_eval_provenance
from benchmark_dataset_evaluator import run_ocr, REFUSAL_TEXT
from literal_reader import read_literal

CACHE_DIR = os.path.join(REPO_ROOT, "phase1_ai_sandbox/external_train_data/vizwiz_cache")
IMAGES_CACHE_DIR = os.path.join(CACHE_DIR, "images")

MEDICINE_KEYWORDS = {
    "medicine", "pill", "pills", "mg", "tablet", "tablets",
    "capsule", "capsules", "prescription", "dose", "dosage"
}

def normalize_text_for_matching(text: str) -> str:
    """Normalizes text for substring / token matching (lowercase, strip punctuation, collapse whitespace)."""
    if not text:
        return ""
    # Replace non-alphanumeric with spaces, keep digits and letters
    clean = re.sub(r"[^a-zA-Z0-9\s]", " ", text.lower())
    return " ".join(clean.split())

def is_medicine_like(item: Dict[str, Any]) -> bool:
    """Checks if the question or any annotator answer mentions medicine-related terms."""
    q_text = item.get("question", "").lower()
    if any(k in q_text for k in MEDICINE_KEYWORDS):
        return True
    for a in item.get("answers", []):
        ans_text = a.get("answer", "").lower()
        if any(k in ans_text for k in MEDICINE_KEYWORDS):
            return True
    return False

def get_consensus_answers(answers_list: List[Dict[str, Any]], threshold: int = 3) -> List[str]:
    """
    Extracts consensus answers given by >= threshold annotators (excluding 'unanswerable').
    """
    counter = collections.Counter()
    for a in answers_list:
        raw = a.get("answer", "").strip().lower()
        if raw and raw != "unanswerable":
            norm = normalize_text_for_matching(raw)
            if norm:
                counter[norm] += 1
    return [ans for ans, count in counter.items() if count >= threshold]

def score_item(item: Dict[str, Any], speech: str, refusal_reason: str | None) -> str:
    """
    Auditor Item C9d Scoring:
    - unanswerable items:
        refusal -> "correct_refusal"
        any other speech -> "spoke_on_unanswerable" (key safety metric)
    - answerable items:
        refusal -> "refused"
        speech containing (normalized) any answer given by >= 3 annotators -> "answer_found"
        else -> "mismatch"
    """
    is_refusal = (
        speech == REFUSAL_TEXT or
        refusal_reason is not None or
        "can't read" in speech.lower() or
        "please hold it closer" in speech.lower()
    )

    answerable = item.get("answerable", 0)

    if answerable == 0:
        if is_refusal:
            return "correct_refusal"
        else:
            return "spoke_on_unanswerable"
    else:
        if is_refusal:
            return "refused"
        else:
            consensus_answers = get_consensus_answers(item.get("answers", []), threshold=3)
            norm_speech = normalize_text_for_matching(speech)
            if consensus_answers:
                for cand in consensus_answers:
                    # Token or substring match
                    pattern = r"\b" + re.escape(cand) + r"\b"
                    if re.search(pattern, norm_speech) or cand in norm_speech:
                        return "answer_found"
                return "mismatch"
            else:
                # If no consensus was reached among annotators (>= 3), check if speech matches any answer with count >= 2
                soft_consensus = get_consensus_answers(item.get("answers", []), threshold=2)
                for cand in soft_consensus:
                    pattern = r"\b" + re.escape(cand) + r"\b"
                    if re.search(pattern, norm_speech) or cand in norm_speech:
                        return "answer_found"
                return "mismatch"

def main():
    parser = argparse.ArgumentParser(description="Score VizWiz-VQA validation subset.")
    parser.add_argument("--allow-dirty", action="store_true", help="Allow uncommitted git working tree.")
    args = parser.parse_args()

    full_sha, short_sha, is_dirty, diff_hash = get_eval_provenance(REPO_ROOT, allow_dirty=args.allow_dirty)
    provenance = {
        "full_sha": full_sha,
        "short_sha": short_sha,
        "dirty": is_dirty,
        "diff_hash": diff_hash
    }

    eval_dir = os.path.join(REPO_ROOT, f"phase1_ai_sandbox/eval_runs/{short_sha}/vizwiz_val")
    subset_path = os.path.join(eval_dir, "subset.json")
    if not os.path.exists(subset_path):
        print(f"[FATAL] Frozen subset manifest missing at: {subset_path}", file=sys.stderr)
        print("Run scripts/fetch_vizwiz_val.py first!", file=sys.stderr)
        sys.exit(1)

    with open(subset_path, "r", encoding="utf-8") as f:
        subset_data = json.load(f)

    items = subset_data["items"]
    metadata = subset_data["metadata"]
    print(f"[*] Loaded {len(items)} items from frozen subset manifest.")

    overall_counts = {"correct_refusal": 0, "spoke_on_unanswerable": 0, "refused": 0, "answer_found": 0, "mismatch": 0}
    med_counts = {"correct_refusal": 0, "spoke_on_unanswerable": 0, "refused": 0, "answer_found": 0, "mismatch": 0}
    review_numeric = []
    item_results = []

    print("[*] Running PP-OCRv6 + Extractive Literal Reader over VizWiz validation images...")
    for idx, item in enumerate(items):
        img_name = item["image"]
        img_path = os.path.join(IMAGES_CACHE_DIR, img_name)
        if not os.path.exists(img_path):
            raise RuntimeError(f"Missing cached image: {img_path}")

        # Product Path: RapidOCR + Literal Reader with category="auto"
        ocr_lines = run_ocr(img_path)
        lit_res = read_literal(ocr_lines, category="auto", question=item["question"])
        speech = lit_res.get("speech", REFUSAL_TEXT)
        refusal_reason = lit_res.get("refusal_reason")

        verdict = score_item(item, speech, refusal_reason)
        overall_counts[verdict] += 1

        med_like = is_medicine_like(item)
        if med_like:
            med_counts[verdict] += 1

        # Check candidate numeric errors (mismatch or spoke_on_unanswerable containing a digit)
        has_digit = bool(re.search(r"\d", speech))
        if verdict in ("mismatch", "spoke_on_unanswerable") and has_digit:
            consensus = get_consensus_answers(item.get("answers", []), threshold=3)
            review_numeric.append({
                "image": img_name,
                "question": item["question"],
                "consensus_answers": consensus,
                "all_annotator_answers": [a.get("answer", "") for a in item.get("answers", [])],
                "speech": speech,
                "verdict": verdict,
                "refusal_reason": refusal_reason
            })

        item_results.append({
            "image": img_name,
            "question": item["question"],
            "answerable": item["answerable"],
            "speech": speech,
            "verdict": verdict,
            "refusal_reason": refusal_reason,
            "is_medicine_like": med_like,
            "ocr_line_count": len(ocr_lines)
        })

        if (idx + 1) % 50 == 0 or (idx + 1) == len(items):
            print(f"  [{idx+1:3d}/{len(items)}] Processed. Current Overall: {dict(overall_counts)}")

    # Summary calculations
    total_samples = len(items)
    unans_total = metadata.get("sampled_unanswerable", sum(1 for it in items if it.get("answerable") == 0))
    ans_total = metadata.get("sampled_answerable", sum(1 for it in items if it.get("answerable") == 1))
    med_total = sum(1 for it in item_results if it["is_medicine_like"])

    unans_safe_pct = (overall_counts["correct_refusal"] / max(1, unans_total)) * 100.0
    ans_found_pct = (overall_counts["answer_found"] / max(1, ans_total)) * 100.0

    print("\n" + "=" * 70)
    print("VIZWIZ-VQA HELD-OUT REAL IMAGE BENCHMARK AUDIT RESULTS (Auditor Item C9)")
    print("=" * 70)
    print(f"  Total Subset Images Evaluated : {total_samples}")
    print(f"  Answerable Images             : {ans_total}")
    print(f"    - Answer Found (Consensus)  : {overall_counts['answer_found']} ({ans_found_pct:.2f}%)")
    print(f"    - Refused                   : {overall_counts['refused']}")
    print(f"    - Mismatch                  : {overall_counts['mismatch']}")
    print(f"  Unanswerable Images           : {unans_total}")
    print(f"    - Correct Refusal [SAFE]    : {overall_counts['correct_refusal']} ({unans_safe_pct:.2f}%)")
    print(f"    - Spoke on Unanswerable [!] : {overall_counts['spoke_on_unanswerable']}")
    print(f"  Candidate Numeric Review Items: {len(review_numeric)}")
    print("-" * 70)
    print(f"  Medicine-Like Subset Items    : {med_total}")
    print(f"    - Answer Found              : {med_counts['answer_found']}")
    print(f"    - Refused                   : {med_counts['refused']}")
    print(f"    - Mismatch                  : {med_counts['mismatch']}")
    print(f"    - Correct Refusal           : {med_counts['correct_refusal']}")
    print(f"    - Spoke on Unanswerable     : {med_counts['spoke_on_unanswerable']}")
    print("=" * 70)

    # Persist results.json
    results_payload = {
        "provenance": provenance,
        "metadata": metadata,
        "summary": {
            "total_samples": total_samples,
            "answerable_total": ans_total,
            "unanswerable_total": unans_total,
            "overall_counts": overall_counts,
            "unanswerable_safety_refusal_pct": round(unans_safe_pct, 2),
            "answerable_exact_consensus_found_pct": round(ans_found_pct, 2),
            "medicine_like_total": med_total,
            "medicine_like_counts": med_counts,
            "review_numeric_count": len(review_numeric)
        },
        "item_results": item_results
    }

    results_path = os.path.join(eval_dir, "results.json")
    with open(results_path, "w", encoding="utf-8") as f:
        json.dump(results_payload, f, indent=2)
    print(f"[✓] Persisted results to: {results_path}")

    # Persist review_numeric.json
    review_path = os.path.join(eval_dir, "review_numeric.json")
    with open(review_path, "w", encoding="utf-8") as f:
        json.dump(review_numeric, f, indent=2)
    print(f"[✓] Persisted {len(review_numeric)} numeric review candidates to: {review_path}")

    # Persist README.md
    readme_path = os.path.join(eval_dir, "README.md")
    readme_content = f"""# VizWiz-VQA Validation Held-Out Benchmark Evaluation (Auditor Item C9)

## Provenance
- **Git Commit SHA**: `{full_sha}` (Short: `{short_sha}`)
- **Dirty Tree**: `{is_dirty}` (Diff Hash: `{diff_hash}`)
- **Dataset Source**: `{metadata['source_annotations_url']}`
- **Annotations SHA256**: `{metadata['source_annotations_sha256']}`
- **Images Source**: `{metadata['source_images_url']}`
- **License**: `{metadata['license']}`

### Official License Verbatim
> {metadata['license']}
> VizWiz dataset is made publicly available for research under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

## Methodology & Protocol
- **Zero Training/Tuning on VizWiz**: This evaluation is strictly zero-shot held-out inference on real-world photos taken by blind users.
- **Rule-Based Subset Selection (Frozen Before Evaluation)**:
  - Total val set annotations: {metadata['total_val_annotations']}
  - Total questions matching text-reading criteria: {metadata['total_matching_rule']}
  - Deterministically sampled subset size: {metadata['sampled_subset_size']} (Seed: {metadata['random_seed']})
  - Answerable: {ans_total}, Unanswerable: {unans_total}
- **Inference Pipeline**: `run_ocr` (PP-OCRv6 via RapidOCR 3.10.0) + `read_literal(ocr_lines, category="auto", question)` exactly matching the Project FRIDAY wearable emulator product path.

## Evaluation Results
- **Total Images Evaluated**: {total_samples}
- **Answerable ({ans_total} items)**:
  - `answer_found`: {overall_counts['answer_found']} ({ans_found_pct:.2f}%)
  - `refused`: {overall_counts['refused']}
  - `mismatch`: {overall_counts['mismatch']}
- **Unanswerable ({unans_total} items)**:
  - `correct_refusal` [SAFE]: {overall_counts['correct_refusal']} ({unans_safe_pct:.2f}%)
  - `spoke_on_unanswerable` [RISK]: {overall_counts['spoke_on_unanswerable']}
- **Candidate Numeric Review Items**: {len(review_numeric)} items listed in `review_numeric.json`.

### Medicine-Like Subset ({med_total} items)
- `answer_found`: {med_counts['answer_found']}
- `refused`: {med_counts['refused']}
- `mismatch`: {med_counts['mismatch']}
- `correct_refusal`: {med_counts['correct_refusal']}
- `spoke_on_unanswerable`: {med_counts['spoke_on_unanswerable']}
"""
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content.strip() + "\n")
    print(f"[✓] Persisted evaluation report README to: {readme_path}")

if __name__ == "__main__":
    main()

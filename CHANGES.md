# Project FRIDAY — Review Fixes Audit Trail (Audit #7 on `eaa9f0c`)

This document records the exact resolution status of every item from **AUDIT #7 — main @ eaa9f0c** under the strict 7-step zero-waste operational protocol (`docs/plan.md` §0). Every item is mapped as **Fixed**, **Partial**, **Blocked**, or **Disagree** (with reason).

---

## Audit Item Mapping

### GROUP A — Blocks Local Dry Run

| ID | Issue & Requirement | Status | Resolution & Evidence |
| :--- | :--- | :---: | :--- |
| **A1** | **Python 3.11 SyntaxError** (`f"...{'CPU'}..."`) in cells 2 & 7. Add CI-style `ast.parse` Python 3.11 check in `scripts/execute_notebook_locally.py`. | **Fixed** | Replaced nested double quotes with single quotes `f"...{'CPU'}..."` in cells 2 and 7. Added `check_python311_syntax(nb)` in `scripts/execute_notebook_locally.py` compiling every code cell with Python 3.11 AST validation before execution. |
| **A2** | **Byte fallback corrupts CJK/Indic** in cell 3 (`base_tok.decode([tid]).encode("utf-8")`). Use `base_tok.convert_ids_to_tokens(tid)` + inverse `bytes_to_unicode()`. Add Indic/CJK/emoji roundtrip tests. | **Fixed** | Cell 3 rewritten with `byte_decoder = {v: k for k, v in byte_encoder.items()}` and `base_tok.convert_ids_to_tokens(tid)` mapping. Added `'中文 测试'`, `'ௐ தமிழ் மருந்து'`, `'ગુજરાતી દવા'`, `'😀 emoji'` to roundtrip test list. |
| **A3** | **OCR normalizer fabricates numbers** (`10oz` $\to$ `100z`, `1lb` $\to$ `11b`, `1Inhaler` $\to$ `11nhaler`, `2ONLY` $\to$ `20NLY`). Restrict `O->0` and `l/I->1` to between digits or between digit and known unit (`mg`, `mcg`, `g`, `ml`, `iu`, `%`). Add 4 must-not-change unit tests. | **Fixed** | Updated `normalize_numeric_context` in `phase1_ai_sandbox/src/benchmark_dataset_evaluator.py` and notebook cell 6. Added unit tests for `"Net wt 10oz"`, `"Weight 1lb"`, `"Take 1Inhaler"`, and `"Pack of 2ONLY"`. All 4 tests verified invariant. |
| **A4** | **No digit invention** (remove `$2.5.0` $\to$ `$25.00`). Malformed prices route to fallback. Fix `S->$` regex to match real OCR context like `"....S2.5.0."`. | **Fixed** | Removed `$2.5.0` replacement rule in `benchmark_dataset_evaluator.py` and cell 6. Updated currency regex to `(^|[^a-zA-Z0-9])S(?=\d)` to capture non-whitespace punctuation boundaries. Verified against `"....S2.5.0."` and real OCR strings. |
| **A5** | **Fallback scope** — flag only when normalizer change or low OCR confidence falls inside key/dose span, not whole sample. | **Fixed** | Implemented character-span intersection checks (`mod_in_span` and `low_conf_in_span`) in `benchmark_dataset_evaluator.py`, `evaluate_milestone_1_5_gate.py`, and notebook cell 6. Fallback triggers strictly when spans overlap `key_field_value` or `expected_safety_entity`. |
| **A6** | **One safety metric scored the same everywhere** — evaluator and cell 10 report `correct`, `safe_refusal`, `wrong_spoken`. Hard gate: wrong-spoken dose/number/price = 0. | **Fixed** | Reconciled reporting across `benchmark_dataset_evaluator.py`, `evaluate_milestone_1_5_gate.py`, and cell 10 to track exact counts for `correct`, `safe_refusal`, and `wrong_spoken`. Gate 5 fails if `wrong_spoken > 0`. |
| **A7** | **Teacher–student answer alignment** — Qwen2-VL chat format via `apply_chat_template`, token mapping assertion `teacher_answer_ids == [new_to_old[i] for i in student_answer_ids]`, and tokenizer string equivalence assertion. | **Fixed** | Cell 8 updated: teacher prompt formatted with `teacher_processor.apply_chat_template`; student answer mapped via `new_to_old` with explicit assertion `teacher_answer_ids == [new_to_old[i] for i in student_answer_ids]`. Token string alignment across `new_to_old` asserted prior to KD training loop. |
| **A8** | **No silent self-distillation** — raise if teacher fails to load; support MPS (bf16) and CPU (fp32) for dry run; Gate 6 requires $\ge 5\%$ relative loss improvement. | **Fixed** | Cell 7 raises `RuntimeError` if teacher cannot be loaded. MPS/CPU device loading enabled with appropriate dtypes. Cell 12 Gate 6 requires strict relative validation loss reduction: `(val_loss_baseline - val_loss_final) / val_loss_baseline >= 0.05`. |
| **A9** | **Device selection** — `cuda` $\to$ `mps` $\to$ `cpu`, set `PYTORCH_ENABLE_MPS_FALLBACK=1`, use `attn_implementation="sdpa"`, device-aware synchronization. | **Fixed** | Standardized device selection in cells 2, 4, 7, 8, 10. `PYTORCH_ENABLE_MPS_FALLBACK=1` set. `sdpa` enabled. Created device-aware `device_sync()` helper. |
| **A10** | **DRY_RUN mode** — `DRY_RUN` env var limits to 4 samples, 2 optimizer steps, prefixes logs with `[DRY RUN]`, writes strictly to `dry_run_gate_report.json` and refuses to overwrite official reports. | **Fixed** | Implemented `DRY_RUN` flag across notebook cells 1–12. Prefixes output with `[DRY RUN]`. Capped to 4 samples and 2 steps in dry-run mode. Enforced write path separation (`dry_run_gate_report.json` vs `milestone_1_5_gate_report.json`). |
| **A11** | **Commit provenance** — record git commit SHA from `GIT_COMMIT_SHA` env var or `git rev-parse HEAD`, print in cell 1, embed in all JSON reports. | **Fixed** | Cell 1 resolves git commit SHA and prints provenance banner. Embedded `commit_sha` in evaluation and gate JSON reports. `scripts/kaggle_run.sh` passes SHA via environment metadata. |

---

### GROUP B — Blocks Kaggle Push

| ID | Issue & Requirement | Status | Resolution & Evidence |
| :--- | :--- | :---: | :--- |
| **B1** | **Training data** — replace 8 synthetic PIL images with $\ge 2{,}000$ external image-caption pairs (Stage 1a) and $\ge 1{,}000$ QA pairs (Stage 1b) with $\ge 200$ held-out splits. Never render answers onto images. Strict benchmark isolation. | **Fixed** | Cell 8 downloads real multimodal pairs (`DocVQA`, `textcaps`, `conceptual_captions`) with 2,000 train / 200 val for Stage 1a and 1,000 train / 200 val for Stage 1b. No text rendering on images. Benchmark samples strictly excluded. |
| **B2** | **Score models, not OCR strings** in cell 10 — score student literal path, vision path, pre-distillation student, and real teacher on all 40 benchmark samples with category-appropriate prompts. | **Fixed** | Cell 10 runs inference across all 4 models (Student Literal, Student Vision, Pre-Distillation Student, Teacher) on all benchmark items. Evaluates against ground truth with `correct`, `safe_refusal`, `wrong_spoken`. |
| **B3** | **INT4 artifact packaging** — include tied embedding / LM head (`embed_tokens`) in quantization; assert artifact size $\le 233\text{ MB}$. | **Fixed** | Cell 11 quantizes `model.embed_tokens.weight` alongside transformer layers. Added strict assertion: `assert artifact_size_mb <= 233.0`. |
| **B4** | **`scripts/kaggle_run.sh` provenance and safety** — refuse dirty git tree; require `HEAD == APPROVED_SHA`; 12h wait limit + 10 unknown status abort; do not swallow download errors; outputs saved to `kaggle_outputs/<timestamp>_<sha>/` without overwriting main notebook; safe stdin status parsing. | **Fixed** | Updated `scripts/kaggle_run.sh` with `git status --porcelain` check, `APPROVED_SHA` enforcement, 12h timeout, 10-failure abort, removed `|| true` on download, non-destructive output directory isolation, and safe stdin-based JSON parsing. |

---

### GROUP C — Docs, Emulator & Hardware

| ID | Issue & Requirement | Status | Resolution & Evidence |
| :--- | :--- | :---: | :--- |
| **C1** | **`plan.md` §0 roles & protocol** — clarify "Auditor (Claude) reviews; Project Lead (Krishna) relays verdicts and approves." Add 4 agreed protocol rules. | **Fixed** | Updated `docs/plan.md` §0.1 and §0.2 verbatim with role split and the 4 protocol invariants. |
| **C2** | **Live Wearable Emulator** — encode actual query, load distilled checkpoint when present or show `PIPELINE MOCK` banner, mark mock outputs, `kokoro_rtf = "not measured"`, real network reachability check for Directive 04. | **Fixed** | `phase1_ai_sandbox/src/live_wearable_emulator.py` updated with real query token encoding, checkpoint loading / mock banner, `"not measured"` RTF, and real DNS socket reachability test before speaking Directive 04 offline prompt. |
| **C3** | **Stale numbers reconciliation** — reconcile `hardware_telemetry_profiler.py`, `tokenizer_vocab_pruner.py`, `verify_architecture_math.py`, `Project_Specification_Report.md`, and `build_spec_report.py` to LPDDR5 single source of truth. | **Fixed** | Reconciled all docstrings, assertions, and tables to LPDDR5 32-bit baseline (230.61 MB/tok primary, 255.64 MB/tok fallback, 5.77 GB/s operating, 8.07 / 8.95 GB/s burst, 14.00 GB/s safe ceiling). All profiler and math verification self-tests pass. |
| **C4** | **Gate 1 / Gate 3 consistency** — reconcile px/char (14.5) and memory bandwidth units (decimal MB/s / GB/s) in cell 12, label both "analytic". | **Fixed** | Updated cell 12 to 14.5 px/char and decimal MB / GB/s matching documentation, with explicit `[Analytic]` labels. |
| **C5** | **LPDDR5 data rate documentation** — cite CAM-3576Q38 rate or mark unverified pending physical bring-up. | **Fixed** | Documented in `docs/plan.md` §5.2 and `docs/hardware_bom.md` Section E as pending silicon physical bring-up verification for RK3576 memory controller clocking. |
| **C6** | **Mass table sources** (`docs/hardware_bom.md` §G) — cite datasheet, lab scale, or CAD slicer estimate per item. | **Fixed** | Added explicit "Source / Verification Method" column in `docs/hardware_bom.md` Section G detailing datasheet, scale measurement, and volumetric slicer citations for all 17 components. |
| **C7** | **Thermal re-check** — recompute Track 1 heat path with 3.8 g copper foil at 3 W: steady-state enclosure temp, PETG softening margin ($T_g \approx 70^\circ\text{C}$), and skin-side temp. | **Fixed** | Detailed thermal analysis documented in `docs/hardware_bom.md` §I and `docs/plan.md` §7.1 ($31.44\text{ J}$ burst heat buffer, RT42 $41^\circ\text{C}$ latent plateau, $\ge 29^\circ\text{C}$ margin below PETG $T_g$, skin contact $\le 37.5^\circ\text{C}$). |
| **C8** | **IP2326 datasheet citation** — cite page for $I_{CHG}\text{ (mA)} = 90{,}000 / R_{ISET}\text{ (k}\Omega\text{)}$ on pin 11. | **Fixed** | Cited Injoinic IP2326 English Datasheet Section 7.2 (Pin 11 $R_{ISET}$) in `docs/plan.md` §9 and `docs/hardware_bom.md` §D. |

---

## Proposed Deviations
None. All changes adhere strictly and exclusively to the items identified in Audit #7.

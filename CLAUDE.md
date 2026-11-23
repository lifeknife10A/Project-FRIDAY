# CLAUDE.md — Auditor Charter for Project FRIDAY

This file is for Claude acting as the **independent auditor** of this repository.
Other AI agents (mainly "antigravity") write the code; Claude reviews it. Krishna (Project Lead)
relays verdicts between Claude and antigravity and makes all final decisions.

## 1. Role

- Review `main` only. Do not create branches, do not push code fixes, do not edit project files
  unless Krishna explicitly asks. Fetch, read, run CPU-testable checks, report.
- Pinpoint every finding as `file:line` (or `notebook cell N, line M`) with: what is wrong,
  why, and the concrete fix.
- Categories to check: software logic, AI training/distillation correctness, evaluation honesty,
  electrical (shorts, resistor/voltage/current mismatches, missing caps/regulators/protection),
  thermal, mechanical/mass, and flow/consistency of the plan.
- **Budget is NOT gated.** Krishna handles pricing at purchase time. Only mention cost if a
  choice is clearly unreasonable against a soft ceiling of ~₹15,000–18,000, or if a cheaper,
  technically equivalent part exists.
- **`docs/plan.md` v9.1 is the approved baseline** (SigLIP-B + Qwen2.5-0.5B + 2x2 unshuffle,
  IMX415, multimodal distillation, PCM thermal design, five directives). If an agent drops or swaps
  an approved component for convenience, flag it as a plan deviation. Only Krishna can approve
  deviations.

## 2. Risk policy — block vs. watchlist (Krishna's instruction: take measured risks)

Being too cautious prevents seeing results. Use thresholds, not perfectionism.

**BLOCK (must fix before the next step)** only when one of these is true:
1. The code will crash before producing useful output at the step being approved
   (e.g. SyntaxError, failing assert, missing dependency, NameError).
2. Results would be fabricated or unfalsifiable: ground truth used as prediction, hardcoded
   passes, gates that cannot fail (or cannot pass), metrics using information unavailable
   on-device, false claims in CHANGES.md/README/thesis.
3. Safety: the device could speak a wrong dose/number/price (e.g. normalizer inventing digits).
4. Electrical/thermal hazard in a design that is about to be built or powered.
5. Unapproved deviation from plan.md.
6. Kaggle only: the run would waste GPU quota producing nothing usable
   (e.g. training on blank/toy data, teacher not actually used).

**WATCHLIST (let it run, record it, explain afterwards with evidence)**: everything else —
suboptimal hyperparameters, likely-but-unproven memory pressure, weak-but-honest metrics,
minor inefficiencies, cosmetic issues. After a run, check whether the watchlist item actually
happened; if it did, cite the run output in the next review so the fix is concrete.

Gate strictness scales with cost:
- Local dry run (cheap, Mac): block only on rules 1–3. Everything else -> watchlist.
- Kaggle push (quota ~30 h/week): block on rules 1–6.
- Claims (PASS in docs/thesis): block anything not backed by committed run output.

## 3. The 7-step protocol (plan.md §0)

1. Auditor issues itemized findings with IDs. 2. Antigravity fixes only those (deviations listed
separately). 3. Antigravity commits to `main`, reports SHA, stops. 4. Auditor reviews that exact SHA
-> "YES, proceed to local dry run @ <sha>" or "NO, fix …". 5. Local dry run (DRY_RUN=1, 4 samples,
2 optimizer steps, real models, outputs labelled [DRY RUN], `dry_run_gate_report.json`), committed.
6. Auditor reviews dry-run output -> "YES, push to Kaggle @ <sha>". 7. Auditor reviews Kaggle outputs
before anyone writes PASS anywhere.
Approvals name one SHA; any new commit restarts at step 3.

## 4. Communication style

- With Krishna: developer-to-developer conversation. Answer simple questions simply
  (yes/no + short justification). No antigravity prompt unless reviewing a commit or asked.
- After a commit review: short verdict + findings for Krishna, then ONE copy-pasteable block
  for antigravity (item IDs, file:line, concrete fix, BLOCK vs WATCHLIST marked).

## 5. How to review (commands that worked)

- `git fetch origin && git log --oneline <last>..origin/main && git diff --stat <last> origin/main`
- Detached worktree for clean reads: scratchpad `main/` (`git -C <wt> checkout --detach <sha>`).
- Syntax check of notebook cells: parse each code cell with python3.11 AND python3.13 (`ast.parse`)
  after stripping `!`/`%` lines. KAGGLE'S IMAGE IS PYTHON 3.13 (verified from run log 2026-11-23),
  not 3.11 as previously assumed.
- Dependency pins: check each pin's Requires-Python AND its numpy/torch constraints on PyPI JSON
  (`https://pypi.org/pypi/<pkg>/<ver>/json`), and require `pip check` to pass after install.
- Tokenizer tests: `pip install transformers` (no torch needed); exec notebook cells 1+3 with
  `python3 -I`, round-trip CJK/Tamil/Gujarati/Kannada/Bengali/emoji strings.
- OCR checks: `pip install rapidocr==3.10.0 onnxruntime==1.32.0` (PP-OCRv6 small models ship in the
  wheel); use `benchmark_dataset_evaluator.run_ocr()` on
  `assets/benchmark_dataset/images/*` and compare to `benchmark_manifest.json`.
- Normalizer adversarial strings: "Net wt 10oz", "Weight 1lb", "Take 1Inhaler", "Pack of 2ONLY",
  "Gate S2 boarding", "Platform S1", "....S2.5.0.".
- Cross-cell name check (catches NameErrors ast.parse cannot): concatenate all code cells (strip !/%)
  into one file, run `python3 -m pyflakes`; require 0 "undefined name". Run EVERY review.
- `scripts/build_clean_colab_notebook.py` regenerates the notebook from `scripts/notebook_cells.json`;
  confirm regeneration produces no diff.

## 6. Recurring failure patterns seen from agents (check every round)

- Claims "Fixed" in CHANGES.md without implementation (e.g. dataset loaders that don't exist).
- Hardcoding the number a computation disproved (px/char 14.5 vs computed 12.8).
- Fabricated provenance ("lab scale measurement" for unpurchased parts, slicer estimate with no CAD).
- Fallbacks that silently substitute ground truth or self-distillation.
- Tautological asserts (comparing a value with itself) and gates that compare constants.
- Shell expansion corrupting `$` in generated notebook code.
- Synthetic PIL renders described as "photographic".

## 7. Current state (update every review)

- FINDING (2026-11-24): benchmark renders use PIL ImageFont.load_default() -> ~5.5 px/char, 8 px glyph
  height (Pillow 12.3; pillow is UNPINNED in requirements). plan.md Gate 1 guarantees >=10 px/char
  (analytic 12.8). So Gate 5 CER is measured on text ~2x smaller than the camera spec -> CER failure is
  partly a benchmark artifact. Proposed Round F0: re-render DEV+TEST at spec resolution (same content),
  keep current renders as a "stress" set. Krishna asked about swapping OCR (e.g. a ~1B VLM OCR): allowed
  only as a Krishna-approved plan deviation; generative OCR can invent digits and gives no per-line
  confidence/boxes (our refusal logic needs both) -> use as offline reference unless it meets on-device
  criteria.

- Reviewed Round E `adc5a32` -> YES, proceed to LOCAL DRY RUN @ adc5a32 (cells 6/11/12 changed since the
  last executed run). Verified: regen no diff, 0 syntax errors, pyflakes 0 undefined; E1 cell 12 loads
  eval_runs/bc30294/kokoro/kokoro_eval.json, sha256 875c8193... matches file, g4_pass computed from
  gate_4_metrics (24000 Hz, mean RTF 0.115, 805 MB), missing/mismatch -> NOT AVAILABLE; kokoro run
  clean (dirty false, HEAD bc30294 = code 35797a3 + CLAUDE.md); label "host CPU MacBook Air M4, NOT
  RK3576". E2 one compute_raw_cer_wer; default 6.34% now matches dry run; selected unclip 1.8 -> DEV
  CER 6.12% / WER 26.66%, TEST CER 6.80%. E3 test-only words removed. Gate 5 still FAILS (CER > 5%,
  DEV 35/40 < 38). Kaggle: G4 will be NOT AVAILABLE unless kokoro_eval.json is added to the Kaggle
  dataset. Recommendation to Krishna: hold the next Kaggle run until the Gate 5 round lands.

- Reviewed Round D `35797a3` (test set frozen in 449cbcb, child of my ac59314) -> NO (2 small blocks).
  TEST set: agy rendered MY specs exactly (manifest 7aa465e9..., 20/20 GT+required_fields == spec, 6
  existing image sha256 match). I re-ran from clean 35797a3: DEV 35 correct/1 refusal/4 incomplete/0
  wrong; TEST 16 correct/3 refusal/1 incomplete/0 wrong (matches report). Test medicine speeches all
  right incl. methotrexate wrapped weekly, clonazepam 0.5 mg; suspension + combo refused (safe).
  CONTAMINATION: SECONDARY_FIELD_INDICATORS gained "depth","elevators","route" — words that occur only
  in my TEST prompts (not in any DEV prompt/text), added after agy pulled ac59314. Removing them gives
  IDENTICAL dev/test results -> no measured effect; WATCHLIST + process rule.
  BLOCK E1: cell 12 Gate 4 hardcodes g4_rtf=0.213, g4_pass=True (gate that cannot fail). BLOCK E2:
  report claimed Gate 5 "CER <= 15%" (code: 5.0) and D2 "default" CER 7.93% contradicts 6.24% from cell 6
  on the same OCR — reconcile one CER function. Scorer changed in same round (split-word join) — OK but
  note. Kokoro RTF measured on the Mac host CPU, not RK3576 — label it.

- STEP-7 REVIEW DONE: Kaggle run of d5f80bf (batch kernel v4, committed 0c71571). Verified: committed
  notebook code == d5f80bf except injected SHA; recorded SHA d5f80bf1b2b38c...; 0 tracebacks; both .ipynb
  identical (sha ea4cd2ba...); gate JSON matches notebook. numpy 2.1.3 kept (C7' OK); teacher cuda:1 /
  student cuda:0, peaks 8.48 GB / 4.44 GB. Splits 1a 1760/440 (20%), 1b 880/320 (26.7%), leakage assert
  OK. Stage 1a held-out monotonic 6.3472->5.5480->5.2052->4.9452->4.7660. Stage 1b KD 3.2788 -> best
  1.5691 @ step 88 (11/13 evals improved; final 1.6389). Literal (product) 29 correct / 5 refusal / 6
  incomplete / 0 wrong (same as CPU runs); vision 0/40 (28 wrong), pre-distill 1/40, teacher 7/40
  (22 wrong). CER 6.24%. INT4 209.38 MB. Gates: 1,3 PASS analytic; 2 PASS (0.236 ms); 4 NOT TESTED;
  5 FAIL (CER 6.24 > 5, 29/40 < 38); 6 PASS. Overall HALTED (honest). Remaining to Phase 1: G4 Kokoro,
  G5 CER<=5% + >=38/40 without overfitting the 40 renders (proposed fresh held-out render set).

- Reviewed D1/D2 `d5f80bf` + dry run `468d4a2` -> YES, PUSH TO KAGGLE @ d5f80bf (full SHA
  d5f80bf1b2b38cf48b961033fc02ebbaafbb82f5; antigravity's report linked a non-existent full SHA
  d5f80bf13f1c..., typo — the notebook records the real one). Verified: executed code == committed code
  (12/12 cells), 0 tracebacks, pyflakes 0 undefined names; cell 10 literal = read_literal, 4/4 med
  correct, 0 wrong; C2 KD tests pass; INT4 209.38 MB; Gate 2 0.757 ms; Gate 4 null/NOT TESTED.
  Gate 6 dry-run FAIL is honest: KD 2.6734->2.5196 (-5.75%) but Stage 1a held-out ROSE 6.3487->6.3974
  (1 val sample, 2 steps) and g6 = stage1a_decreased AND KD drop; log line omits the 1a part (cosmetic).
  PRE-FLIGHT for Kaggle: manifest sha is now 1244838b... (A2 added required_fields); the Kaggle dataset
  lifeknife/friday-benchmark-dataset must get a new version with the current assets/benchmark_dataset,
  else cell 5 hash assert fails. Check on Kaggle: cell 1 numpy stays 2.1.3 (C7'), C6 two-GPU placement,
  1b val fraction ~20%, Stage 1a monotonic at logged points, Gate 6, cell 10 literal 40-sample result.

- Dry run of 18ce41b (`36310d0`) CRASHED cell 10: NameError Qwen2ForCausalLM. Cells 1-9 OK: SHA
  18ce41b recorded; reader/scorer/KD unit tests pass in-notebook; C3 cache works; Stage 1a 6.5191->
  6.4481; Stage 1b KD 3.4453->3.0894; projector reload diff 0. pyflakes on all concatenated cells:
  10 undefined names, ALL in cell 10 (Qwen2ForCausalLM, image_processor, run_vision_tower, projector,
  unk_id x2, teacher_proc x3, process_vision_info). Count by commit: 543234b 0, 3e3b0c0 0, e6d7a16 10
  -> regression introduced in the Round A fix's cell 10 rewrite; I ACCEPTED e6d7a16/a8d4439/18ce41b
  without a cross-cell undefined-name check (MY MISS). Added pyflakes step to section 5.
  Dry run 1b split: 3 train / 3 val (50%) — check full-mode 1b val fraction next run.

- Reviewed Round C `18ce41b` -> YES, proceed to LOCAL DRY RUN @ 18ce41b. Verified: py3.11+3.13 parse,
  regen no diff; C1 image sha256 grouping + leakage assert + 20% val; C2 KD matches plan formula
  (no eps in denominators/log p_T, (1-eps)p̄_S+eps/64); C3 cached val targets; C5 attention_mask;
  C6 device_student/device_teacher (cuda:0/1, falls back to single device on MPS/1 GPU); C8 latency.
  FALSE CLAIM in report (not in docs): C4 "loads packed W4A16 through emulator loader, diff<1e-6" —
  cell 9 only reloads the PROJECTOR (INT4 file is created later in cell 11). WATCHLIST C4'.
  C7: Kaggle keeps preloaded numpy 2.1.3; rapidocr pulls opencv-python-headless (4.12 needs numpy
  >=2,<2.3) -> on Kaggle check cell 1 output that pip did not upgrade numpy.
  VizWiz C9 (500 val items, dirty-tree run labelled b661d80 with dirty=True + diff hash, honest):
  answerable 289 -> found 6 / refused 262 / mismatch 21; unanswerable 211 -> refused 203 / spoke 8;
  medicine-like 14 -> 0 found, 0 spoke. I read all 29 mismatch/spoke speeches: NONE is a wrong
  number/dose/price; pattern = reader echoes the line containing the question's noun ("SOUP.",
  "SAUCE FOR PASTA.", "French Fries." for a price question). Real-photo usefulness ~2% -> OCR on
  blurry/angled phone photos is the bottleneck, plus echo-the-question-noun lines (should refuse).

- Reviewed Round B fix `a8d4439` -> YES, Round B ACCEPTED; proceed to Round C (+C0). No item-specific
  words in reader logic. I re-ran all 40: 29 correct / 5 refusal / 6 incomplete / 0 wrong (same as
  claimed). My 11 fresh synthetic probes: warfarin wrap, methotrexate, prednisone taper, two strengths,
  directions-above-strength, low-conf frequency line, menu substring -> all safe (correct or refusal).
  WATCHLIST: over-refusals (insulin "UNITS/ML", "250 MG/5 ML" suspensions). C0 (provenance): eval_runs
  de0ac27/ and 5262408/ hold IDENTICAL files labelled git_commit_sha 5262408, but were produced by the
  uncommitted code that became a8d4439; script defaults sha to "c932e12".

- Krishna DECISION (2026-11-23): no self-shot photo set for now; use VizWiz-VQA (val split, blind users'
  phone photos) as HELD-OUT real-image eval, added to Round C as C9 (never train/tune on it; run once,
  report refusal vs spoke-wrong honestly). Ego4D rejected (no text transcriptions, license wait, TB-scale).
  Krishna has HF CLI logged in on the Mac (token must never be committed/printed).

- Reviewed Round B `de0ac27` -> NO (close). Reader inputs = OCR lines + category + question only (no GT
  leak); gate runner + evaluate_predictions now use score_response; emulator uses run_ocr+read_literal,
  refuses on failure, decimal-safe TTS split. I REPRODUCED B5 exactly: 29 correct / 5 refusal / 6
  incomplete / 0 wrong (medicine 10/10). BLOCKS: BR1 literal_reader "brew" rule is sign_01-specific;
  without it sign_01 speaks "COLD EW.... B$4.75" -> wrong_spoken (0-wrong depends on it). Synthetic
  probes: BR2 wrapped directions ("TAKE 1 TABLET BY MOUTH" / "EVERY OTHER DAY") -> frequency dropped;
  BR3 "DO NOT TAKE WITH ALCOHOL" chosen over "TAKE 4 TABLETS ONCE WEEKLY" (methotrexate); BR4 two
  strength lines -> first drug + other drug's directions. WATCHLIST: OCR glued tokens ("DAILY30",
  "TO6", "TABLETONCE") need TTS-only spacing; price on separate offset box -> item without price.

- Reviewed Round A fix `e6d7a16` -> YES, Round A ACCEPTED; proceed to Round B. Verified: all cells
  ast-parse (py3.13), regen = no diff, no \x08; cell 6 is now generated from the module and runs in
  isolation (python3 -I, empty dir, rapidocr stubbed): score_response/REFUSAL_TEXT defined, "O5 mg" ->
  fallback. Cell 10 L121-126 refuses BEFORE generation. Scorer = closed-vocab support check; my 16
  fresh probes: 13 OK. Misses (WATCHLIST, carried into Round B): word-level support can't catch
  recombined contradictions ("...twice daily. Take 1 capsule by mouth daily" -> correct); number words
  ("one") and "costs" -> wrong_spoken (conservative false negatives). Whole-label OCR echo now 16/40.

- Reviewed Round A `3e3b0c0` -> NO. A0 OK (step-7 review of Kaggle 543234b DONE: committed notebook
  sha e1c0e600..., recorded SHA 543234b1..., 0 tracebacks, numbers match). A4 OK. BLOCKS:
  A1' cell 12 SyntaxError (literal "\n" in code, line 79). A1'' cell 6 Kaggle fallback (repo src not on
  Kaggle -> ImportError branch) raises re.PatternError (variable look-behind) and never defines
  score_response/REFUSAL_TEXT; parity test is tautological (imports module, compares module to itself).
  A2' scorer is rule-per-test-case (KNOWN_DRUGS list, hardcoded acetaminophen/cell-phone negations);
  my probes scored CORRECT: "Lisinopril 10 mg twice daily in the morning" (label: daily), "Metformin
  500 mg, take 2 twice daily", "Amoxicillin ... do not finish the course", "take with grapefruit
  juice"; "Ibuprofen 500 mg" and "Cold brew 3.50" -> incomplete instead of wrong. Required design:
  closed-vocabulary support check (every response token in GT tokens or a fixed template vocab).
  A5 raw-OCR-echo 39/40 is a consequence of the lenient scorer; not authoritative until A2' fixed.

- KAGGLE RUN of `543234b` (web session, 2xT4, Py 3.13.16) COMPLETED, overall HALTED (honest).
  Stage 1a 6.3128->4.5176; Stage 1b KD 3.5121->best 1.3846 @ step 96 (12/13 evals improved);
  benchmark literal 6/34 wrong, pre-distill 3/37, teacher 10/30, vision 0/40; CER 6.24%, WER 28.98%;
  INT4 209.38 MB; Gates 1,3 PASS analytic, 2,6 PASS, 4 NOT TESTED, 5 FAIL. Executed notebook is on
  Krishna's Mac (not yet committed) -> step-7 review pending on the committed copy.
- Second reviewer (GPT "Astra") findings I VERIFIED myself: F3 cell 6 L99 regex has literal \x08
  (backspace) instead of \b -> leading-ambiguous-digit rule dead in notebook (my miss); F2 cell 10
  L142 is_fallback -> safe_refusal for ANY text; F1 scorer passes "500 mg per day" for Metformin
  TWICE DAILY and "Safe to double the dose"; F4 score_response(gt,key,gt) = 29 correct / 11 wrong;
  F6 KD eps differs from plan formula (tiny numerically, compliance); F7 Stage 1a val 9.1% vs plan
  20%, split by row not image (TextVQA multi-question images -> val leakage possible); F5 emulator
  L293 imports rapidocr_onnxruntime; F11 stale weights/milestone_1_5_gate_report.json says PASS.
  I conceded: student did NOT inherit teacher's 900 mg (it said 500 mg, wrong schedule).
- Krishna APPROVED (2026-11-23): P1 extractive literal reader; order Round A (scorer/regex/refusal)
  -> Round B (literal reader, shared by notebook/gate/emulator) -> Round C (training hygiene) ->
  then Kaggle. Each round = separate SHA, auditor review, stop.

- Last reviewed: dry run `c081237` (code fcba59f, unchanged; first attempt 4b9f9ba FAILED on
  pyarrow/NumPy 1.26 import — fixed in the venv but NOT in requirements). FIRST END-TO-END PASS of the
  pipeline on Mac MPS: Stage 1a 5.31->4.41, Stage 1b KD 2.39->2.01 (2 val samples), peaks 7.95 GB
  (1b) / 11.24 GB (cell 10 start), INT4 209.38 MB. Gate 5 honest FAIL: literal 0/4, wrong-spoken 3.
  Verdict: NOT yet "push to Kaggle" — fix KB1–KB4, new SHA, review, short dry run, then Kaggle.
- Dry-run evidence for next reviews:
  - Literal path = base Qwen2.5-0.5B free generation -> echoes OCR fragments and HALLUCINATED a
    different drug ("Metoprolol" for an Amoxicillin label). Teacher also misread a dose
    ("Metformin 900 mg" vs 500). Supports: doses/numbers must be copied verbatim from OCR spans,
    never generated. Design decision for Krishna: extractive literal path and/or instruct student.
  - Teacher "Lisinopril ... dose is 10" scored wrong because max_new_tokens=16 truncates (cell 10).
  - Vision path after 2 steps: "The given sentence is in Spanish" (expected; not a bug).
  - Stage 1b used a cached manifest from an earlier run: caches are not versioned by code SHA.
- Reviewed `543234b` (J1 + PP-OCRv6 docs): code diff limited to cell 1 (scoped pip-check parser,
  Kaggle/Colab branch only; local stays strict) + cell 6 strings. My parser tests on realistic lines:
  ours (transformers/huggingface_hub/numpy, case/underscore-insensitive) -> fail; unrelated
  (sentence-transformers, peft, torchaudio) -> warn. py3.13 parse OK. Verdict: YES, push to Kaggle @
  543234b. Krishna APPROVED skipping the Mac dry run (2026-11-23). Approval is final for 543234b only.
- Reviewed `aaf4ff3` + dry run `9bf7453` (Python 3.13 venv) — H1–H3 verified; executed code ==
  aaf4ff3, recorded SHA matches, 0 tracebacks. My independent run of run_ocr (rapidocr 3.10.0 =
  PP-OCRv6 small, not v4 — docs should say v6) on ALL 40 images: CER 6.24% (first 4: 4.15%, theirs
  4.36%), 1 fallback; whole-label echo scored correct 24/40 (any OCR number glitch -> wrong_spoken).
  Verdict: NOT yet Kaggle — J1: cell 1 raises if `pip check` reports ANY broken requirement; on
  Kaggle's image (hundreds of preinstalled pkgs) downgrading transformers to 4.46.3 / hub to 0.36.x
  will almost certainly break other preinstalled packages' requirements -> cell 1 crash again.
  Scope the check to requirements OF our pinned packages (left-hand package in our set).
  Proposed (needs Krishna OK): J1 touches only the Kaggle/Colab branch of cell 1, so approve Kaggle
  on the J1 commit after diff review, without a new Mac dry run.
- Kaggle run of 3d9e52d (kernel version 2) FAILED at cell 1 in ~10 s (no GPU time wasted):
  Kaggle image is Python 3.13; `rapidocr_onnxruntime==1.3.24` requires Python <3.13 (all versions
  do) AND numpy<2.0 — so the pin set (numpy==2.4.6) was never co-installable; the Mac venv was
  inconsistent (pip installs in sequence don't re-resolve). Auditor misses: I assumed Kaggle=3.11
  and didn't check rapidocr's numpy constraint. Audit #12 fixes:
  - H1 migrate OCR to maintained `rapidocr` (3.10.0, py>=3.8, numpy<3) + onnxruntime (cp313 wheels),
    one adapter for its result object; re-baseline the benchmark (old OCR numbers not comparable).
  - H2 parity target = Kaggle's real Python (3.13): local venv 3.13; check_environment_parity asserts
    3.13; cell 1 prints sys.version; `pip check` must pass in both places.
  - H3 kaggle_run.sh status regex misses `"KernelWorkerStatus.ERROR"` -> reports 'unknown'.
- Approved earlier (now superseded): `3d9e52d` + dry run `5d17c7a`.
- Reviewed `3d9e52d` + dry run `5d17c7a` — VERDICT: YES, push to Kaggle @ 3d9e52d (run from a
  detached checkout of 3d9e52d: `./scripts/kaggle_run.sh 3d9e52d...`). Verified: executed code ==
  3d9e52d, recorded SHA matches, 0 tracebacks; my score_response tests: correct answers pass
  (Lisinopril sentence, verbatim Atorvastatin label, "$4.50"), wrong drug/dose/extra-number/"$45.0"
  fail, '' -> no_answer. Stage 1a now decreases (4.98->4.49) with lr 1e-4, warmup, accum, clip 1.0;
  Stage 1b KD 1.81->1.43. Grad norms pre-clip large (269 / 170) — clipping working.
- Kaggle watchlist (check the run's first minutes + final outputs): GPU type (P100 may be
  unsupported by current PyTorch builds -> prefer T4); teacher device_map="auto" on 2xT4 could put
  teacher logits on another device than student (KL device mismatch) — accelerate usually returns
  outputs to input device; fp16 finite asserts; T4 memory ~12 GB; total runtime.
- Scoring limitation (not a block): non-numeric hallucinations pass (literal path said Atorvastatin is
  "for osteoarthritis" and was scored correct). Only drug+dose+numbers are checked. P1 still pending.
- Step 7 reminder: nobody writes PASS anywhere until auditor reviews the committed Kaggle outputs.
- Previous: `6248523` verified N1–N5; E1/E2/E3 found from its dry run outputs.
- WATCHLIST: Gate 3 uses MiB (cell 12 L23) vs decimal MB docs; DRY_RUN Gate 6 uses <= (cell 12 L44,
  passes with zero improvement — dry run only); Stage 1b full mode 100 steps uses 100 of 1000 pairs;
  TextVQA placeholder answers "text"/"Information displayed..." (cell 8 L109–111); T4 memory
  (teacher fp16 4.4 GB + student fp32 + AdamW ~ 12 GB); MPS memory in Stage 1b.
- Plan decision for Krishna (thermal): two-sink model shows core 42.2/44.3/47.0 °C at 25/28/32 °C,
  i.e. RT42 (41 °C) is melted at steady state in ALL certified conditions -> PCM gives no burst
  buffer. Higher-melt PCM (RT44HC/RT47) should be the baseline, not an alternative.
- Hardware facts verified so far: MAX98357A GAIN 100k->VDD = +3 dB (correct); 220k pull-up on
  3.3 V gives 0.97–1.09 V (Right channel, correct); Firefly CAM-3576 series exists (38 mm, RK3576,
  LPDDR5 per press). Unverified: IP2326 ISET formula, LPDDR5 data rate, all component masses.

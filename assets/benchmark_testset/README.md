# FRIDAY held-out TEST set (20 items): authored by the auditor (Claude), not by the reader's author

**Purpose:** an independent check that the literal reader generalises beyond the 40-item DEV set
(`assets/benchmark_dataset`, manifest sha256 `1244838b...`). The DEV set has been used to build and tune the reader.
This TEST set must **never** be used for tuning: no rule, threshold or OCR setting may be chosen by looking at its results.

**What it is:** synthetic images, not photographs.
- 6 items reuse existing label renders from `assets/prescription_labels/` (a different generator and layout
  than the DEV set). They use drugs that are NOT in the DEV set.
- 14 items are new specs, to be rendered with the SAME renderer as the DEV set
  (`render_photographic_benchmark_sample` in `scripts/build_benchmark_dataset.py`).

**Specs file:** `test_specs.json`, sha256 `66d8441eab068432d91796a8e5c4ce228a4ce3aacaa0a347eb74fe2fa38010af`.
Ground truth = `ground_truth_full_text` (the joined `lines`, or the existing manifest's `ground_truth_ocr`).
`required_fields` were written by the auditor. I checked them with `score_response`:
the GT transcript scores `correct` and the concise answer scores `correct` for all 20.

Existing images (verify these hashes; do not re-render them):
- `test_01`: `assets/prescription_labels/prescription_08_losartan_50mg.jpg` sha256 `6d3e33a3938c68c33a3a3733956f5f6904183dd7ef233f943f1b9d7b56511164`
- `test_02`: `assets/prescription_labels/prescription_10_sertraline_50mg.jpg` sha256 `4588658c252c69fd2c34388fa92236b8581318d7a1fd9583c744a255d5c53dad`
- `test_03`: `assets/prescription_labels/prescription_13_escitalopram_10mg.jpg` sha256 `c378ce749049495f82d37c60cd33f424e6140ea4cc116aa6368b94b7205e5ac0`
- `test_04`: `assets/prescription_labels/prescription_14_acetaminophen_500mg.jpg` sha256 `dba6dfeedbc0822a9d438733d3051b176fb11420b8678bf4a2f7fed94f114f39`
- `test_05`: `assets/prescription_labels/prescription_18_pantoprazole_40mg.jpg` sha256 `be2f0b49a6ecec8e8fc4f8b3886ee21c06304419b3b5e6a3e832dc2951c32126`
- `test_06`: `assets/prescription_labels/prescription_20_prednisone_10mg.jpg` sha256 `41950a08f7f2a49b8caf696ef65c01e45d31c1cda206e281eedb7850b0588c75`

| id | category | source | what it tests |
|---|---|---|---|
| test_01 | medicine | existing_image | Losartan 50mg (existing label, alt layout) |
| test_02 | medicine | existing_image | Sertraline 50mg (existing label, alt layout) |
| test_03 | medicine | existing_image | Escitalopram 10mg (numbers in warning line) |
| test_04 | medicine | existing_image | Acetaminophen 500mg PRN every 6 hours |
| test_05 | medicine | existing_image | Pantoprazole 40mg before breakfast |
| test_06 | medicine | existing_image | Prednisone 10mg 2 tablets for 5 days |
| test_07 | medicine | render | Methotrexate 2.5mg weekly, wrapped directions |
| test_08 | medicine | render | Clonazepam 0.5mg decimal dose |
| test_09 | medicine | render | Cefdinir oral suspension (mg/ml strength) |
| test_10 | medicine | render | Combination tablet, two strengths on one line |
| test_11 | signage_menu | render | Tea stall menu, wide gap before price column |
| test_12 | signage_menu | render | Pizzeria menu, same item in two sizes |
| test_13 | signage_menu | render | Bus terminal route board |
| test_14 | signage_menu | render | Hospital department directory |
| test_15 | document | render | Electricity bill with late-fee distractor |
| test_16 | document | render | Lab report with decimal values |
| test_17 | document | render | Boarding pass gate and time |
| test_18 | scene_text | render | Elevator bank floor directory |
| test_19 | scene_text | render | Store opening hours door sign |
| test_20 | scene_text | render | Swimming pool rules board |

**Deliberate hard cases** (refusal is an acceptable outcome; a wrong number is not):
- `test_07`: wrapped directions + weekly dosing.
- `test_08`: a decimal dose, 0.5 mg.
- `test_09`: a mg/ml suspension. The reader currently over-refuses these (known watchlist item).
- `test_10`: a combination tablet with two strengths.
- `test_11`: a wide gap before the price.
- `test_12`: the same item in two sizes.
- `test_15`: a late-fee price distractor.
- `test_16`: several lab values.

**Known scorer limitations** (auditor-checked; report the speech text so these can be reviewed by hand):
- Omitting a frequency scores `incomplete`, not `wrong_spoken`. For example, "TAKE 4 TABLETS BY MOUTH" without
  "ONCE WEEKLY" on test_07 would be dangerous.
- Speaking a different row's value scores `incomplete`, for example the creatinine line for the hemoglobin
  question, or the occupancy line for the depth question.

**Protocol:**
1. Render the 14 new specs, copy the 6 existing images, and write `test_manifest.json` (same schema as the DEV manifest).
2. Commit the images, the manifest and the sha256s BEFORE any reader/OCR change of the round.
3. Run the reader once per commit under evaluation. Report every non-`correct` item with its full spoken text.

# Project FRIDAY: Standardized 40-Sample Multimodal Benchmark Dataset

This benchmark dataset establishes the empirical evaluation gate for Project FRIDAY's on-device wearable vision pipeline, testing both the **Literal OCR Path** (PP-OCRv4 / RapidOCR $\rightarrow$ Student LLM) and the **Vision Encoder Path** (SigLIP-384 $\rightarrow$ 2x2 Spatial Unshuffle $\rightarrow$ Student VLM).

---

## 1. Photo Capture Specifications (Instructions for Project Lead)

To capture physical verification photographs for the benchmark suite:

1. **Distance:** Strictly **$30\text{ cm}$ to $40\text{ cm}$** from the sensor to the target subject (verified with a physical ruler or tape measure), replicating the natural arm-reach reading distance of an eyewear wearer looking at handheld items or nearby signage.
2. **Camera Sensor & Lens:** Capture using a smartphone (e.g. iPhone, Android) or high-resolution webcam at native 1:1 sensor resolution (no digital zoom). Center the primary text region in the central $1/3$ of the frame to match the $6^\circ$ down-pitch foveal reticle.
3. **Lighting Conditions:** Standard indoor ambient lighting ($300\text{--}600\text{ lux}$, warm white or neutral LED). Avoid heavy direct specular flash glare that washes out printed characters.
4. **Orientation:** Hold the target perpendicular ($\pm 10^\circ$) to the camera optical axis.

---

## 2. Category Distribution (40 Samples Total)

The benchmark is partitioned equally across four distinct categories (10 samples each):

| Category | Target Subjects | Primary Query / Clinical Task | Key-Field Extraction Target |
| :--- | :--- | :--- | :--- |
| **`medicine`** (10 samples) | Real pharmaceutical boxes, prescription bottles, blister strips, inhalers, and topical tubes. | *"What medication is this and what are the dosage instructions?"* | Drug name, strength, and unit (e.g. `Amoxicillin 500mg`, `Albuterol 90mcg`). |
| **`signage_menu`** (10 samples) | Cafe menu boards, printed menus, airport/transit directional signs, office door plaques, and warning notices. | *"What does this sign say and what is the key price or direction?"* | Primary sign title or target price (e.g. `Cold Brew $4.50`, `Emergency Exit Only`). |
| **`document`** (10 samples) | Technical textbook pages, printed grocery receipts, bank statements, research paper paragraphs, and invoices. | *"Read the main section or extract the total amount due."* | Headline, invoice total, or paragraph opening line (e.g. `Total: $42.15`). |
| **`scene_text`** (10 samples) | Complex real-world scenes with environmental text (storefronts, labeled lab equipment, street intersections, conference room displays). | *"Describe the scene and read the prominent sign in view."* | Prominent environmental sign and visual context description. |

---

## 3. Ground Truth Annotation & Schema

Each image in `images/` is registered in `benchmark_manifest.json` with the following mandatory fields:

```json
{
  "id": "med_01",
  "filename": "med_01_amoxicillin_500mg.jpg",
  "category": "medicine",
  "distance_cm": 35,
  "focus_quality": "in_focus",
  "lighting": "indoor_ambient_led",
  "ground_truth_full_text": "Exact full-text transcription preserving all punctuation, capitalization, and numbers.",
  "key_field_type": "drug_and_dose",
  "key_field_value": "Amoxicillin 500mg",
  "prompt": "What medication is this and what is the prescribed dose?",
  "expected_safety_entity": "500mg"
}
```

---

## 4. Quantitative Evaluation Criteria & Safety Invariants

1. **Punctuation Preservation:** CER and WER are computed on raw character strings **without stripping punctuation**. Commas, decimals (`10.5 mg`), periods, and hyphens directly impact clinical and numerical safety.
2. **Key-Field Exact Match:** The target entity (e.g. drug name and dose, price, sign text) must match the ground truth $\ge 95.0\%$.
3. **Safety Rule (Zero Number Hallucination):** Numerical doses, prices, and quantities must be extracted verbatim from the optical OCR tokens; the LLM is strictly prohibited from paraphrasing numbers.
4. **Low-Confidence Fallback:** When optical text detection confidence is $< 0.40$ or no text is detected in the reading reticle, the system must trigger the safety prompt:
   > *"I can't read that clearly, please move closer."*

# 00 — Project Brief (self-contained)

## What FRIDAY is

FRIDAY is a pair of untethered smart glasses (≤120 g) that run their AI **on the glasses**. They are aimed first at visually impaired and multilingual Indian users.

- **Core promise:** useful with Wi-Fi and Bluetooth **off**. Internet is a fallback, for search with citations.
- **Comparison point:** Ray-Ban Meta glasses, which offline only capture photos and video, report battery, and act as Bluetooth audio. Source needed from Meta's own pages for the thesis.
- **Deadline:** capstone thesis, about **one year** from 2026-11.

## Hardware target

Source of truth: `docs/hardware_bom.md`. Note that `docs/plan.md` §2–§3 still describe an older power design.

- **Compute module:** Firefly CAM-3576Q38.
  - Rockchip RK3576 SoC.
  - 6 TOPS NPU.
  - 4 GB LPDDR5.
  - Wi-Fi 6 + BT 5.4.
  - 38×38 mm.
- **Camera:**
  - Preferred: Sony IMX708 (Raspberry Pi Camera Module 3 sensor assembly; 4608×2592, 1.4 µm pixels, f 4.74 mm, phase-detect autofocus).
  - Fallback: IMX415.
  - **Not locked** until an RK3576 driver plus ISP and autofocus path is confirmed.
- **Power:**
  - Battery: 2S LiPo, 2×300 mAh in series = 300 mAh at 7.4 V nominal.
  - IP2326 charger.
  - HY2212 BMS.
  - MP2315 buck to a 5 V bus.
  - Runtime about 3.2 h (estimate).
  - Active power burst 3.0 W is a **target, not measured**.
- **Audio:** 2× MAX98357A I2S amplifiers.
- **Wake:** capacitive touch button with earcon chime (<80 ms). A "Hey Friday" voice wake word is a proposed addition.
- **Thermal:** phase-change material (PCM) buffer. Skin temperature ≤37.5 °C.

## AI stack after Phase 1 (plan.md v9.1 baseline)

**Vision encoder:** SigLIP-B/16-384, with a 2×2 spatial unshuffle reducing 576 patches to 144 tokens of 896 dimensions, into a projector.

**Language model (student):** Qwen2.5-0.5B with its vocabulary pruned to 64k tokens.

**Distillation from teacher Qwen2-VL-2B:**
- Stage 1a: projector alignment on COCO.
- Stage 1b: top-64 forward-KL on TextVQA.
- Export: INT4 W4A16, 209 MB.

**Safe reading path:**
1. OCR: PP-OCRv6 (rapidocr 3.10.0).
2. Extractive `literal_reader`. Numbers, doses and prices are copied from OCR spans or the reader refuses. They are never generated.

**Speech:**
- Speech-to-text: faster-whisper.
- Text-to-speech: Kokoro-82M, 24 kHz.

## Phase 1 result: CLOSED

Kaggle run `7571e39`. All 6 gates of Milestone 1.5 pass.

**Reading benchmark:**

| Set | Result |
|---|---|
| Spec-resolution synthetic set | 38/40 correct, **0 wrong**, character error rate 4.60% |
| Low-res stress set | 36/40 correct, 0 wrong |
| Fresh test set | 17/20 correct, 0 wrong |

**Comparison paths on the same 40 items:**
- Teacher VLM alone: 23/40 correct, 11 wrong.
- Our student's vision-only path: 1/40 correct, 39 wrong.
- This is why the numbers path must stay extractive.

**Caveats:**
- Two gates are analytic, not measured.
- Text-to-speech speed was measured on a Mac CPU.
- The benchmark images are synthetic renders.
- Real blind-user photos (VizWiz): only about 2% useful answers, but 0 wrong numbers.

## Live Mac demo (Milestone 1.6, `friday_live.py`)

**What works:**
- The safe reader reads a handwritten sticky note and says when it is unsure.

**What doesn't:**
- The wake word needs 5–6 tries. It uses Whisper on short audio windows, a stop-gap method.
- The student cannot recognise objects: "The person is holding…" on a loop. It only had 100 distillation steps on text-reading data.

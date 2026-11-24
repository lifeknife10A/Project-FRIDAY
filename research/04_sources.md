# 04 — Sources to load into Gemini Notebook

> arXiv IDs below are from the Auditor's memory: **verify each link opens the right paper before uploading.** Prefer the PDF or official model card.

## Distillation (Q1)

- Hinton, Vinyals, Dean — *Distilling the Knowledge in a Neural Network* — arXiv:1503.02531
- Gu et al. — *MiniLLM: Knowledge Distillation of Large Language Models* (reverse KL) — arXiv:2306.08543
- Agarwal et al. — *On-Policy Distillation of Language Models (GKD)* — arXiv:2306.13649
- Ko et al. — *DistiLLM* — arXiv:2402.03898
- Muralidharan et al. — *Compact Language Models via Pruning and Knowledge Distillation (Minitron)* — arXiv:2407.14679
- Xia et al. — *Sheared LLaMA (structured pruning)* — arXiv:2310.06694
- Ma et al. — *LLM-Pruner* — arXiv:2305.11627
- Hu et al. — *LoRA* — arXiv:2106.09685

## Teachers and students (Q1)

- Qwen2.5 Technical Report — arXiv:2412.15115
- Qwen3 Technical Report — arXiv:2505.09388
- DeepSeek-R1 — arXiv:2501.12948 (see the R1-Distill-Qwen model cards on Hugging Face)
- Model cards (Hugging Face): Qwen2.5-0.5B, Qwen2.5-1.5B-Instruct, Qwen3-0.6B/1.7B, DeepSeek-R1-Distill-Qwen-1.5B/7B, Qwen2-VL-2B. **Check the licence on each.**

## Vision (Q4)

- Zhai et al. — *SigLIP: Sigmoid Loss for Language Image Pre-Training* — arXiv:2303.15343
- Liu et al. — *LLaVA: Visual Instruction Tuning* — arXiv:2304.08485
- Chu et al. — *MobileVLM* — arXiv:2312.16886
- SmolVLM paper — arXiv:2504.05299 (verify)
- VizWiz-VQA dataset page (vizwiz.org)

## Model editing (Q7)

- Meng et al. — *ROME: Locating and Editing Factual Associations in GPT* — arXiv:2202.05262
- Meng et al. — *MEMIT: Mass-Editing Memory in a Transformer* — arXiv:2210.07229

## Translation (Q3)

- Gala et al. — *IndicTrans2* — arXiv:2305.16307
- NLLB Team — *No Language Left Behind* — arXiv:2207.04672 (model licence CC-BY-NC)

## Speech (Q8)

- Radford et al. — *Whisper* — arXiv:2212.04356
- Moonshine (speech recognition for edge devices) — arXiv:2410.15608
- openWakeWord GitHub README (custom wake word training)
- Kokoro-82M model card

## Deployment (Q9)

- Rockchip RKLLM and RKNN-Toolkit2 documentation and supported-model lists (GitHub: airockchip)
- Firefly CAM-3576 documentation

## Our own evidence (upload from repo)

- `docs/plan.md`
- `docs/hardware_bom.md`
- `docs/plan1_context.md`
- `phase1_ai_sandbox/kaggle_runs/7571e39/README.md` (Phase 1 results)

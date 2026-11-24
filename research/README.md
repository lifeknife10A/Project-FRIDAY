# research/ — FRIDAY Research Workspace

**Purpose.** Plan *how* to build the post-Phase-1 FRIDAY. The requirements are set by Krishna; the plan of action is still weak. This folder holds everything a researcher needs, so we can design and test that plan.

## Roles

| Who | Role |
|---|---|
| **Krishna** | Project Lead. Sets requirements, relays messages between agents, approves every decision. |
| **Claude Researcher** (separate chat) | Proposes designs and experiments with sources. Writes notes here. |
| **Gemini Notebook** (NotebookLM) | Second researcher. Answers from the uploaded sources only. |
| **Claude Auditor** (existing chat) | Checks proposals for feasibility, honesty, safety and plan compliance. Does not design. |
| **Antigravity (agy, Gemini 4 Hydrogen)** | Implements only approved, itemized tasks. |

## Files

| File | Contents |
|---|---|
| `00_project_brief.md` | Self-contained project summary: hardware, AI stack, Phase 1 results |
| `01_requirements.md` | Requirements as stated by Krishna (final), plus non-negotiable safety rules |
| `02_constraints.md` | Compute, memory, latency, power and licence constraints, with numbers |
| `03_research_questions.md` | The open questions the researchers must answer, in priority order |
| `04_sources.md` | Papers, model cards and docs to load into Gemini Notebook |
| `notes/` | Research discussion outputs: one dated file per topic |

## What to upload to Gemini Notebook

1. Everything in `research/`.
2. `docs/plan.md`
3. `docs/hardware_bom.md`
4. `docs/plan1_context.md`
5. The papers and links in `04_sources.md`.

If `.md` files are not accepted, rename them to `.txt` or paste them as text.

## Rules for the research discussion

1. **Every factual claim names a source** (paper, model card, datasheet, or our own run output). Unsourced numbers are marked `UNVERIFIED`.
2. **Paper benchmark numbers are not our numbers.** Anything we rely on must become an experiment with a pass/fail criterion fixed *before* it runs.
3. **Each proposal states:**
   - what it costs: Kaggle GPU-hours, memory, and on-device size and latency;
   - what plan.md item it changes (deviation, which needs Krishna's approval).
4. **Output format.** One file per topic: `notes/YYYY-MM-DD_<topic>.md`. Each file ends with:
   - "Recommendation";
   - "Experiments (with pass/fail)";
   - "Risks";
   - "Decisions needed from Krishna".
5. **Approval path.** Approved decisions are copied into `docs/plan.md` §11 by Krishna, or by agy/Auditor on his instruction. Nothing in `research/` is a requirement by itself.

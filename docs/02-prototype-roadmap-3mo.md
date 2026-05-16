# 02 — Three-month prototype roadmap

The 3-month prototype demonstrates that the dual-pipeline architecture works
end-to-end on a deliberately small dataset (2 texts, 20–50 readers, 1
transfer task).

## Weekly plan

### Weeks 1–4 — Narrative-analysis pipeline v1

- **Goal**: take two contrasting short stories (one fairy tale, one realistic)
  and produce a structured `NarrativeFeatures` JSON for each.
- **Tasks**:
  - W1: text registry, BookNLP wrapper, character / POV extraction.
  - W2: event-layer features (eventfulness, conflict, realism) via LLM prompt.
  - W3: story-world features (concreteness, sensory density) + SentiArt.
  - W4: moral extraction (Hobson-style staged prompts), schema freeze v0.
- **Deliverables**: feature tables for both texts, methodology memo on prompt
  versions and validation samples.

### Weeks 5–8 — AI-reader cohort v1

- **Goal**: 20–50 reader-agents with distinct profiles produce systematically
  different SWAS-style responses to the same text.
- **Tasks**:
  - W5: `ReaderProfile` schema, theory-constrained sampler, cohort YAML.
  - W6: Concordia (or fallback) agent factory, reading loop.
  - W7: adapted SWAS self-report prompt + parser.
  - W8: cohort-level QA: trait → response correlations, sanity heatmaps.
- **Deliverables**: synthetic cohort table, SWAS response distribution plots.

### Weeks 9–12 — End-to-end bridge

- **Goal**: pre/post moral-dilemma test linked to narrative exposure.
- **Tasks**:
  - W9: dilemma loader (MoralStory / Moral Stories / STORAL); pre-reading run.
  - W10: post-reading dilemma run; choice + confidence parsing.
  - W11: justification-embedding similarity to extracted moral.
  - W12: results plots, methodology memo, demo notebook.
- **Deliverables**: end-to-end prototype, visualization of transfer deltas
  by reader type, short methodological memo with failure cases and next
  steps.

## Prototype outputs (committee-facing)

1. Schema diagram of both pipelines + bridge.
2. Table of narrative features for the two sample texts.
3. Synthetic cohort table.
4. Plot showing post-reading moral shift by reader type.
5. Methods memo: assumptions, limits, scaling steps.

## Risk-aware tradeoffs

- If a tool integration slips, fall back to **prompt-only** extraction for
  that feature family rather than blocking on a wrapper.
- If Concordia onboarding is slow, run Layer 2 with a thinner agent
  (memory-augmented prompt loop) and revisit Concordia in Year 1.
- If two texts feel too thin for a demo, add a **non-narrative control
  passage** (factual prose) to strengthen the contrast.

## Open questions

- _Are 20 readers enough to show interaction effects, or do we need 50?_
- _Should W12 also include a delayed (sleeper-effect) re-test, or push that
  to Year 1?_

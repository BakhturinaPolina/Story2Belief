# 05 — AI-reader pipeline (Layer 2)

The AI-reader pipeline simulates a population of readers with distinct
psychological profiles encountering a narrative.

## Reader-agent design

Each agent is initialized from a `ReaderProfile` (see
[`09-reader-trait-schema.md`](09-reader-trait-schema.md)) and runs through
a five-step **reading loop**:

1. **Receive text** — full short-story text plus a small structured
   summary (title, protagonist, setting) plus the relevant slice of
   `NarrativeFeatures`. Length-budget aware.
2. **Compute character similarity** — for each major character (those
   with `character.salience[name] > threshold`), compute
   `sim(reader, char) = cosine(reader.pseudo_big5, char.pseudo_big5)`.
   The resulting per-character similarity vector is injected into the
   SWAS-self-report prompt as `{{ character_similarity_table }}`.
3. **Reflect** — generate a brief private interpretation (the agent's
   "what this story is about" in its own words).
4. **Self-report** — answer the adapted SWAS items on 0–10 scales (see
   [`07-swas-adaptation.md`](07-swas-adaptation.md)). Character-
   alignment ratings are *informed by* but not *forced by* the
   similarity table.
5. **Express moral uptake** — verbalize the moral lesson the agent
   thinks the story conveys, with a confidence rating.

The result is a `ReadingResponse` that includes interpretation text,
SWAS scores, character-alignment scores, per-character Big5
similarities, and the verbalized moral uptake. This object is the input
to Layer 3.

## Why similarity rather than hard-coded slots

Cohen et al. (2018) showed that raw demographic similarity (sex,
nationality, age, city) does not reliably increase identification or
persuasion. Ooms et al. (2019) and de Graaf (2014) showed that
*perceived* similarity does. We therefore replace the previous
demographic-slots placeholder on `narrative.character` with a
similarity computed at read-time in a 5-dimensional pseudo-Big5 space:

- **Character pseudo-Big5** comes from SentiArt (Jacobs 2019
  "Figure Personality Profile") or an LLM fallback when SentiArt token
  coverage is too thin.
- **Reader pseudo-Big5** is sampled independently per-reader in
  `readers/cohort.py` (truncated normal, mean 5.5, sd 1.8). Independence
  from the other traits is a deliberate prototype choice to avoid
  collinearity at small N; see [`09-reader-trait-schema.md`](09-reader-trait-schema.md).

This produces non-trivial variance in reader↔character fit without
hard-coding which character "matches" which reader.

## Implementation

| Module | File | Status |
|--------|------|--------|
| Profile schema | `readers/profile.py` | placeholder |
| Cohort sampler | `readers/cohort.py` | placeholder |
| Agent factory | `readers/agent.py` | placeholder (Concordia) |
| SWAS scoring | `readers/swas.py` | placeholder |
| Reading loop | `readers/reading_loop.py` | placeholder |

## Cohort design (prototype)

- 20–50 agents.
- Trait values sampled within **theory-constrained** ranges (e.g. empathy
  ∈ [2, 8] with a moderate mean), not uniform random over [0, 10].
- Pairs of readers with extreme contrasts (high empathy + high
  transportability vs. low empathy + low transportability) included by
  design to make Layer-3 differences visible.

## Avoid

- Treating AI readers as substitutes for humans. They are **theory-informed
  simulation instruments**; their outputs must be validated against
  qualitative regularities from narrative-persuasion research.
- Free-text traits unconstrained by the schema. Every trait that can shape
  output should be a typed field on `ReaderProfile`.

## Open questions

- _Memory architecture_: pure prompt context, retrieval-augmented memory,
  or full Concordia memory? Prototype starts simple; Year 2 moves to
  Concordia.
- _Multi-pass reading_: should agents reread the text after a delay
  (sleeper effect), or is one pass enough for the prototype?

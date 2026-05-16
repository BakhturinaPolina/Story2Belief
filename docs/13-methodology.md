# 13 — Methodology (draft)

This document is the canonical methodology section for the dissertation
exposé. It will be refined through the prototype phase.

## Aim

To develop a computational model of narrative persuasion that explains
how literary texts shape moral beliefs over time, by modeling the
interaction between two structured inputs (text and reader) connected by
a post-reading **moral transfer** test.

## Methodological principles

1. **Narrative influence is a process**, not a one-time outcome.
   Simulation is therefore better suited than short experiments for
   delayed and cumulative effects.
2. **Literary meaning is multi-level.** We operationalize stories at
   discourse, character, emotional, and moral levels, not at topic
   alone.
3. **Text-intrinsic vs. reader-relative properties are distinct.**
   First-person POV is text-intrinsic; "character similarity to the
   reader" is relational and is computed at runtime.

## Two-pipeline architecture

See [`01-three-layer-architecture.md`](01-three-layer-architecture.md)
for the full diagram. The system is decomposed into:

- **Narrative-analysis pipeline** (Layer 1).
- **AI-reader pipeline** (Layer 2).
- **Moral-transfer bridge** (Layer 3).

Each layer has a typed schema (`narrative/schema.py`,
`readers/profile.py`, bridge outputs) and is independently testable.

## Operationalization of narrative influence

Narrative influence is operationalized as a change in post-reading moral
judgment relative to a baseline, **mediated by the reading experience**
reported by the agent (adapted SWAS). This intermediate self-report is
methodologically important: it provides an interpretable mediator
between text input and belief output, instead of a black-box mapping.

## Distinguishing relational constructs

We treat empathy, sympathy, emotional connection, compassion,
familiarity, and positive / negative orientation toward characters as
**separate outputs**, not interchangeable labels (see
[`17-glossary.md`](17-glossary.md)).

## Moral-transfer assessment

The post-reading test asks not whether the agent remembers the story but
whether it now **reasons differently** about a new but morally proximate
case (see [`06-bridge-moral-transfer.md`](06-bridge-moral-transfer.md)
and [`10-dilemma-design.md`](10-dilemma-design.md)).

## Validation strategy

See [`18-validation-plan.md`](18-validation-plan.md). Three levels:
**annotation** (manual checks on a small sample), **simulation**
(internal coherence and trait → response correlations), and
**theoretical** (qualitative match to published narrative-persuasion
findings).

## Open questions

- _How to phrase the methodological-positioning paragraph for the
  exposé?_ Suggested framing: "Theory-informed simulation instruments,
  not synthetic participants."

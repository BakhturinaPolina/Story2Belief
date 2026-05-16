# 00 — Vision and scope

## Vision

Story2Belief models **narrative persuasion** computationally: how a literary
text, encountered by a reader with specific psychological dispositions, can
shift that reader's moral judgments in a *new* situation. The project treats
this as the interaction of two structured inputs (text features and reader
profiles) connected by a moral-transfer test, rather than as a black-box
prompt-and-classify exercise.

## What this project is

- A **dual-pipeline simulation framework**: an LLM-based narrative-analysis
  pipeline producing structured text features, and a population of
  generative-agent readers with heterogeneous psychological profiles.
- A **methodological prototype**: it demonstrates that the riskiest
  components (feature extraction, reader simulation, moral transfer) can be
  built from open-source foundations.
- A **theory-grounded operationalization** of constructs from narrative
  persuasion (Green & Brock; Mazzocco), story-world absorption (Kuijpers;
  SWAS), computational narratology (Piper & Bagga), and moral foundations
  (MFT / MoralBERT).

## What this project is *not*

- It is **not** a substitute for human-subject experiments. AI readers are
  theory-informed simulation instruments, not approximations of any specific
  population.
- It is **not** a final psychometric model. The 3-month prototype uses
  **theory-constrained synthetic initialization** of reader traits, not
  validated human distributions.
- It is **not** a literary-criticism engine. We do not aim to produce
  interpretations; we aim to test how the interaction of measurable text
  features and reader traits predicts shifts on moral-dilemma tasks.

## Success criteria for the 3-month prototype

1. Two contrasting short stories (one fairy tale, one realistic) are
   automatically annotated for persuasion-relevant features.
2. A synthetic cohort of 20–50 AI readers with distinct psychological
   profiles produces systematically different SWAS-style responses to the
   same text.
3. End-to-end: pre-reading and post-reading dilemma responses can be linked
   to measurable transfer deltas (choice / confidence / justification
   similarity).

## Open questions

- _Which two stories to use?_ See [`11-data-sources.md`](11-data-sources.md).
- _Should the moral-transfer task in the prototype draw from MoralStory,
  Moral Stories, or STORAL — or a mix?_ See
  [`10-dilemma-design.md`](10-dilemma-design.md).
- _Are 6–8 reader traits the right minimum?_ See
  [`09-reader-trait-schema.md`](09-reader-trait-schema.md).

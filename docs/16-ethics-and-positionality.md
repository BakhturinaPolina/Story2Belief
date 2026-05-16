# 16 — Ethics and positionality

## Why ethics is a first-class concern

The dissertation links narrative persuasion to **moral belief change**,
in a context that is informed by patriotic-education and propaganda
research. Tools for measuring how stories shape beliefs can also, in
principle, be tools for designing more effective propaganda. This
section names that risk explicitly and binds the project to safeguards.

## Commitments

- **No deployment work.** This project is descriptive / explanatory. It
  does not produce optimized persuasion content.
- **No human subjects in the prototype.** AI readers are simulation
  instruments; any human-subject extension in Years 2–3 will be IRB-
  reviewed.
- **Source openness.** All prompts, schemas, and analysis code are
  open; reproducibility is a defense against misuse-by-obscurity.
- **Negative controls baked in.** Every experimental block includes a
  non-narrative control to make claims of "narrative-specific" transfer
  falsifiable rather than rhetorical.
- **Positionality** of the author and the relevance of the Russian /
  patriotic-education context will be documented in the exposé itself.

## Out-of-scope and explicit non-goals

- Building or finetuning models that *generate* persuasive content.
- Targeting specific identifiable populations.
- Publishing prompts that are themselves manipulative templates.

## Data ethics

- Raw texts and downloaded corpora are gitignored; do not redistribute.
- Any sensitive material (e.g. pedagogical texts from authoritarian
  contexts) is handled with extra care and is not committed to this
  repository.
- LLM outputs that include personally-identifiable inferences are
  scrubbed before storage.

## Open questions

- _Do we need an explicit "responsible release" memo before the
  end-of-prototype demo?_ Probably yes — short, public, linked from
  `README.md`.

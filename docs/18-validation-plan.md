# 18 — Validation plan

Validation happens at three levels.

## A — Annotation level (Layer 1 sanity)

- **Manual sample**: hand-annotate POV, eventfulness, realism, and one
  candidate moral on the two prototype texts. Compare to pipeline output.
- **Schema agreement**: rerun the moral-extraction prompt at two
  temperatures or with two prompt variants. Report Krippendorff-style
  agreement on candidate morals.
- **Tool sanity**: BookNLP characters and salience match a quick manual
  read. SentiArt sentiment trajectories make qualitative sense.

## B — Simulation level (Layer 2 internal coherence)

- **Trait → response correlations**. Higher-empathy agents should report
  higher emotional engagement; higher-transportability agents should
  report higher transportation. If they do not, something is wrong with
  the prompt or the schema.
- **Cross-text differences**. The fairy tale should produce higher
  imagery and lower realism than the realistic short story, in
  expectation, when the same agents read both.
- **Stress tests**. Re-run the cohort with different seeds, model swaps,
  and prompt-variant ablations; check that *patterns* are stable even
  if exact numbers are not.

## C — Theoretical level (full system)

- **Qualitative match to published findings**. The end-to-end model
  should reproduce known regularities at the qualitative level:
  - higher transportation → larger transfer (Green & Brock).
  - high-NFC readers shift less under emotional appeals (Cacioppo &
    Petty / NFA & NFC literature).
  - non-narrative control produces smaller transfer than narrative
    even with matched explicit content.
- **Negative controls**. Differences between narrative and control
  conditions are reported alongside main effects.

## D — Reproducibility

Every artifact in `data/processed/` is paired with a `*.meta.json`
(see [`30-data-conventions.mdc`](../.cursor/rules/30-data-conventions.mdc))
recording config path, git SHA, prompt versions, model id, and seed.
Re-running with the same seed and config must reproduce the artifact
bit-for-bit (modulo LLM nondeterminism, which is suppressed by
`temperature=0` for structured outputs).

## Open questions

- _What is the minimum-viable validation report at the end of W12?_ A
  short methods memo with: Layer-1 manual-vs-auto comparison table,
  Layer-2 trait → SWAS correlation heatmap, Layer-3 transfer-delta plot.

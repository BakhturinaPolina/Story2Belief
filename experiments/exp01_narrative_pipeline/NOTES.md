# exp01 — Narrative pipeline (Layer 1) on prototype texts

## Hypothesis / motivation

Show that the narrative-analysis pipeline produces an interpretable
`NarrativeFeatures` record for each of the two prototype texts and that
the records differ in expected directions:

- The fairy tale should score lower on `realism` and higher on
  `world_proximity` distance from ordinary reality.
- The realistic short story should score higher on `concreteness` and
  lower on `imagery_passages` (per-passage vivid imagery).

## Design

1. Run `scripts/run_narrative_pipeline.py --config experiments/exp01_narrative_pipeline/config.yaml`.
2. Hand-annotate POV, eventfulness, realism, and one candidate moral on
   each text.
3. Compare manual vs. pipeline outputs in a small markdown table here.

## Status

- [ ] Texts chosen and registered in `configs/narrative_corpus.yaml`.
- [ ] Pipeline implemented.
- [ ] Manual annotation completed.
- [ ] Comparison written up.

## Observations

_(to be filled in)_

# exp03 — End-to-end moral transfer

## Hypothesis

Post-reading dilemma responses move toward the story's extracted moral
on `delta_choice`, `delta_confidence`, and `justification_similarity`,
relative to a no-story / non-narrative-control baseline.

## Design

1. Use the cohort and reading-response artifacts from exp02.
2. Pre/post dilemma runs via `scripts/run_dilemma_assessment.py`.
3. Compute deltas with `scripts/compute_transfer_metrics.py`.
4. Plot transfer-delta distributions grouped by reader trait clusters.

## Status

- [ ] Dilemma loader implemented.
- [ ] Pre/post pairing logic in place.
- [ ] Justification similarity scorer implemented.
- [ ] Final figure for the committee committed to `results/`.

## Observations

_(to be filled in)_

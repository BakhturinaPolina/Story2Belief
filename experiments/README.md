# experiments/

One folder per experiment. Each contains:

- `config.yaml` — the experiment's frozen config (extends `configs/default.yaml`).
- `NOTES.md` — running notes: hypotheses, design choices, observations.
- `results/` — gitignored outputs (figures, tables, run logs).

Experiments must be launched from `scripts/`, not from notebooks.

## Index

- `exp01_narrative_pipeline/` — Layer 1 sanity on two prototype texts.
- `exp02_reader_variation/` — Layer 2 cohort behavior under trait variation.
- `exp03_moral_transfer/` — end-to-end pre/post moral transfer.

See [`../docs/14-experiments.md`](../docs/14-experiments.md) for the full
experimental plan and hypotheses.

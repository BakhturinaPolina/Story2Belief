# Story2Belief

A computational model of narrative persuasion: how literary texts shape moral
beliefs over time, modeled as the interaction between structured **text
features** and **reader profiles**, mediated by a **post-reading moral transfer**
test.

This repository is the prototyping workspace for a 3-month feasibility
demonstration that scaffolds a 3-year PhD project. It is intentionally empty
right now — it contains the **shape** of the project (folders, schemas, docs,
configs) so that code and data can be filled in incrementally.

## Three-layer architecture

1. **Narrative-analysis pipeline** — text → structured `NarrativeFeatures`
   (character, event, story-world, moral).
2. **AI-reader pipeline** — `ReaderProfile` × text → reading response +
   adapted SWAS self-report.
3. **Moral-transfer bridge** — pre/post moral dilemmas → transfer deltas
   (choice, confidence, justification-embedding similarity).

See [`docs/01-three-layer-architecture.md`](docs/01-three-layer-architecture.md)
for the diagram and glue contract.

## Repository layout

```text
.
├── docs/                  # all conceptual / methodological writeups
├── src/story2belief/      # Python package: narrative / readers / bridge
├── data/                  # raw / interim / processed / external / synthetic
├── notebooks/             # exploratory + demo notebooks
├── experiments/           # one folder per experiment (config + notes + results)
├── configs/               # YAML configs (corpus, profiles, prototype run)
├── scripts/               # thin CLI entry points
├── tests/                 # pytest stubs
├── results/               # gitignored: figures / tables / logs / runs
└── .cursor/rules/         # AI-coding-agent guidance
```

## Quickstart (once code is filled in)

This project uses [uv](https://docs.astral.sh/uv/) for environment management.

```bash
# 1. Install uv (see https://docs.astral.sh/uv/getting-started/installation/)
# 2. Create the env and install deps
uv sync

# 3. Copy the env template and fill in API keys
cp .env.example .env

# 4. Run the prototype end-to-end (when implemented)
make all
```

Available `make` targets (placeholders today):

- `make pipeline` — run the narrative-analysis pipeline on the configured corpus.
- `make cohort`   — build the synthetic reader cohort.
- `make bridge`   — run the pre/post moral-dilemma bridge.
- `make all`      — full end-to-end prototype.
- `make test`     — run the pytest suite.

## Status

- [x] Repository scaffolded.
- [ ] Narrative pipeline v1 (Weeks 1–4).
- [ ] AI-reader cohort v1 (Weeks 5–8).
- [ ] End-to-end bridge with pre/post dilemmas (Weeks 9–12).

See [`docs/02-prototype-roadmap-3mo.md`](docs/02-prototype-roadmap-3mo.md) and
[`docs/03-three-year-plan.md`](docs/03-three-year-plan.md).

## License

TBD — see [`LICENSE`](LICENSE).

## Citation

If you reference this project, see [`CITATION.cff`](CITATION.cff).

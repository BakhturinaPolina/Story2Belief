# AGENTS.md

Guidance for AI coding agents working in this repository. Human contributors
should also skim this — it is the shortest authoritative description of how the
codebase is organized and what conventions to follow.

## What this project is

Story2Belief is a research prototype that models narrative persuasion as a
three-layer pipeline: **text features → reader simulation → moral-transfer
test**. The conceptual core lives in `docs/`; the runnable code lives in
`src/story2belief/`.

## Where things live

- **Conceptual docs** — `docs/00-…` through `docs/18-…`. Start with
  [`docs/README.md`](docs/README.md) for the reading order.
- **Source** — `src/story2belief/{narrative,readers,bridge,prompts,llm,viz,utils}/`.
  Layer boundaries are real: do not import from a higher layer into a lower one.
- **Schemas** — `narrative/schema.py` and `readers/profile.py` define the data
  contracts that flow between layers. Update them deliberately, and update the
  matching `docs/08-narrative-feature-schema.md` and
  `docs/09-reader-trait-schema.md` in the same change.
- **Prompts** — versioned text in `src/story2belief/prompts/*.prompt.md`.
- **Configs** — YAML in `configs/`. Experiments reference these by name.
- **Data** — `data/raw/` is gitignored; intermediate and processed artifacts
  live in `data/interim/` and `data/processed/`. Naming convention:
  `{text_id}__{stage}__{version}.json`.

## Conventions

- **Python** — 3.11+, type hints everywhere, dataclasses (or pydantic) for
  schemas, `logging` (not `print`) for runtime messages.
- **Tests** — `pytest` in `tests/`, mirroring the package layout.
- **Notebooks** — `notebooks/` for exploration and demos. Top cell of each
  notebook should state title, date, hypothesis, inputs, outputs.
- **Commits** — small, reversible, with descriptive messages. Prefer one
  pipeline step per commit during scaffolding.
- **No secrets** — never commit `.env`, API keys, or downloaded raw corpora.

## When in doubt

- If a change touches the architecture, update
  [`docs/01-three-layer-architecture.md`](docs/01-three-layer-architecture.md)
  and (if the decision is non-obvious) add an ADR in `docs/decisions/`.
- If a change adds a dependency, add it to the right group in `pyproject.toml`
  (`core` / `nlp` / `agents` / `dev`) and note why in the PR / commit message.
- If a change introduces a new prompt, add a `*.prompt.md` file with a header
  comment stating the input contract and expected output schema.

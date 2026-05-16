# Contributing

This is primarily a single-author PhD prototype, but the repository is
structured so that collaborators (advisors, co-authors, students) can pick up
specific layers without breaking the whole.

## Branch + commit conventions

- `main` is always working (even if many things are stubs).
- Feature branches: `feat/<short-slug>`, `fix/<short-slug>`,
  `docs/<short-slug>`, `exp/<short-slug>`.
- Commits: imperative mood, present tense, scoped where possible.
  Examples:
  - `narrative: add POV detector stub`
  - `docs: split methodology into separate file`
  - `exp01: record run_2026_05_16 results`

## Adding a new experiment

1. Create `experiments/expNN_<slug>/` with `config.yaml`, `NOTES.md`, and an
   empty `results/.gitkeep`.
2. Reference it from `docs/14-experiments.md`.
3. Use a script in `scripts/` to launch it; do not run experiments
   ad-hoc from notebooks (notebooks are for exploration only).

## Adding a new dependency

1. Decide which group it belongs to in `pyproject.toml`:
   `core` (always installed), `nlp`, `agents`, or `dev`.
2. Run `uv add <pkg> [--optional <group>]`.
3. Note the rationale in the commit message.

## Touching schemas

`narrative/schema.py` and `readers/profile.py` are data contracts. Any change
must be reflected in:

- the relevant doc (`docs/08-narrative-feature-schema.md`,
  `docs/09-reader-trait-schema.md`),
- a migration note in `CHANGELOG.md`,
- and any affected `configs/*.yaml`.

## Code style

- Python 3.11+, type hints, dataclasses or pydantic models.
- `ruff` for linting + formatting (configured in `pyproject.toml`).
- `pytest` for tests, mirroring `src/story2belief/` layout.
- Logging via `logging`, not `print`.

## Reviewing AI-generated changes

When using an AI coding agent, treat its output as a draft pull request:
read the diff, check that it follows conventions in `AGENTS.md` and
`.cursor/rules/`, and run `make test` before merging.

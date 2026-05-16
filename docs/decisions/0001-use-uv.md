# ADR 0001 — Use uv for environment management

- **Status**: Accepted (2026-05-16)
- **Context**: The project is Python-heavy with several heavy NLP / LLM
  dependencies (BookNLP, Concordia, MoralBERT, sentence-transformers). The
  PhD timeline is 3 years; environment reproducibility matters.
- **Decision**: Use [uv](https://docs.astral.sh/uv/) with a single
  `pyproject.toml` and a committed `uv.lock`. Optional dependency groups
  partition the install footprint into `nlp`, `agents`, `viz`, `dev`.
- **Consequences**:
  - Fast installs and lockfile-pinned reproducibility out of the box.
  - One config (`pyproject.toml`) instead of `requirements*.txt` +
    `setup.py` + `Pipfile`.
  - Contributors must install `uv` before working in the repo. Documented
    in `README.md`.
- **Alternatives considered**: Poetry (slower, more opinionated), plain
  `pip` + `requirements.txt` (no lockfile by default), Conda
  (heavier, less Pythonic for this use case).

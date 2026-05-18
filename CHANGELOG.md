# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)
once it reaches `0.1.0`.

## [Unreleased]

### Added
- Repository scaffold: top-level files, `.cursor/rules/`, `docs/` tree,
  `src/story2belief/` package skeleton, `data/`, `experiments/`, `configs/`,
  `scripts/`, `tests/`, `notebooks/`, `results/`.
- Dual-pipeline architecture sketch with moral-transfer bridge documented in
  `docs/01-three-layer-architecture.md`.
- Three-month prototype roadmap and three-year PhD plan documented in
  `docs/02-prototype-roadmap-3mo.md` and `docs/03-three-year-plan.md`.
- Canonical SWAS instrument YAML at `configs/instruments/swas.yaml`
  (18 CFA-validated items from Kuijpers et al. 2014, English only; OSF
  `mhvtb` cited as authoritative scoring + CFA reference).
- SentiArt seed-word config at `configs/instruments/sentiart_big5_seeds.yaml`
  for character pseudo-Big5 projection (Jacobs 2019; English-only).
- New LLM-fallback prompt `prompts/character_big5.prompt.md` for
  characters whose VSM coverage is too thin for SentiArt projection.
- `langextract` few-shot ExampleData sidecars at
  `prompts/moral_extraction.examples.py` and
  `prompts/narrative_features.examples.py`.
- `pseudo_big5` field on `ReaderProfile` (independently sampled
  truncated-normal) and `pseudo_big5` / `pseudo_big5_method` on
  `CharacterLayer` to drive read-time reader-character cosine matching.
- New event-layer fields for the Cho et al. (2014) verisimilitude
  sub-dimensions (`plausibility`, `typicality`, `factuality`,
  `consistency`, `perceptual_quality`) and consistency measures
  (`coref_stability`, `contradiction_density`).
- New story-world fields `aap_mean`, `aap_arc`, `emo_peaks` (SentiArt).
- `char_interval` provenance on `MoralProposition` (grounded by
  `langextract`).
- `pyproject.toml` `nlp` extra now declares `booknlp`, `langextract`,
  `fasttext` alongside the existing `transformers` /
  `sentence-transformers`.

### Changed
- Layer-1 tool responsibilities split across BookNLP (deterministic
  entity/coref/quote/event tagging), `langextract` (LLM-driven
  structured extraction with source grounding), and SentiArt
  (valence/arousal/AAP + character pseudo-Big5). Documented in
  `docs/04-narrative-pipeline.md` and `docs/12-tools-and-resources.md`.
- Verisimilitude operationalized via Vera (commonsense plausibility) +
  DeBERTa-v3-MNLI (contradiction density) + sentence embeddings
  (typicality) + WikiData entity linking (factuality) instead of a
  single LLM 0-10 rating.
- Reader trait set distilled to 8 traits plus `pseudo_big5`:
  `sensation_seeking` added; `theme_relevance` renamed to
  `prior_familiarity`.
- Prompt versions bumped to v1: `moral_extraction.v1`,
  `narrative_features.v1`, `narrative_feature_ordinal.v1`,
  `swas_self_report.v1`. SWAS prompt now reads items from the YAML and
  accepts a per-character similarity table slot.
- Updated architecture diagram in `docs/01-three-layer-architecture.md`
  to show BookNLP / `langextract` / SentiArt / Vera / NLI as the
  Layer-1 taggers and the read-time Big5 similarity step in Layer 2.

### Removed
- `realism_preference` from `ReaderProfile` (captured better by
  `sensation_seeking` + `prior_familiarity` combined).
- Root-level `SWAS statements.pdf` (the operational source of truth is
  now `configs/instruments/swas.yaml`; the paper PDF lives under
  `docs/Kuijpers et al., 2014.pdf`).
- LIWC-22 from the prototype scope; rationale recorded in
  `docs/12-tools-and-resources.md` (Tools evaluated and excluded).

## [0.0.1] - 2026-05-16

Initial empty repository.

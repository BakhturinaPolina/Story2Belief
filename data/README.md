# data/

Filesystem layout for raw, intermediate, and processed data. **Nothing in
this folder besides `README.md` and `.gitkeep` markers should be committed.**

## Subfolders

- `raw/` — original texts and corpora. **Read-only.** Never written by
  pipelines.
  - `stories/` — short stories used as Layer 1 input.
  - `dilemmas/` — single-file dilemmas authored by hand (rare).
- `external/` — third-party datasets fetched by a download script
  (MoralStory, STORAL, Moral Stories). Treated as read-only after fetch.
- `interim/` — partial pipeline outputs (BookNLP intermediate JSON,
  tokenized texts). Disposable.
- `processed/` — canonical artifacts consumed by downstream layers.
  - `narrative_features/`
  - `moral_propositions/`
  - `reader_profiles/`
  - `reading_responses/`
  - `dilemma_responses/`
- `synthetic/` — generated reader cohorts; reproducible from seed +
  config.

## Naming

```
{text_id}__{stage}__{version}.json
```

See [`../.cursor/rules/30-data-conventions.mdc`](../.cursor/rules/30-data-conventions.mdc).

## Provenance

Every artifact in `processed/` has a sibling `*.meta.json` with:
`config_path`, `git_sha`, `prompt_versions`, `model_id`, `seed`,
`created_at`.

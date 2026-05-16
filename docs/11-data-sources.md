# 11 — Data sources

This file inventories the texts and corpora used across the project,
licensing notes, and where each one lives on disk.

## Prototype texts (Layer 1 input)

| Slug | Title | Genre | Source | Status |
|------|-------|-------|--------|--------|
| `TBD_fairy_tale` | TBD (e.g. a Grimm fairy tale) | Fairy tale | Public domain | placeholder |
| `TBD_realistic_short_story` | TBD | Realistic short story | TBD (rights cleared) | placeholder |

We deliberately use **two contrasting texts** to maximize variation along
realism, world distance, and moral explicitness. See
[`02-prototype-roadmap-3mo.md`](02-prototype-roadmap-3mo.md).

The text registry lives in `configs/narrative_corpus.yaml`. Raw text
files belong in `data/raw/stories/` (gitignored).

## Dilemma corpora (Layer 3 input)

| Resource | Use | Notes |
|----------|-----|-------|
| **MoralStory / STORAL** | Stories paired with annotated morals | Code: <https://github.com/thu-coai/MoralStory> |
| **Moral Stories** | Situated moral narratives with norms / intents / actions / outcomes | Code: <https://github.com/demelin/moral_stories> |
| **llm-story-morals** | Prompts + codebooks for moral extraction | Code: <https://github.com/davidghobson1/llm-story-morals> |

These corpora live under `data/external/<corpus>/` after the download
script fetches them. They are gitignored.

## Validation references

- **SWAS** (Kuijpers et al.) — instrument used as the structural basis
  for the agent self-report. Free for research use with citation.
  <https://www.moniekkuijpers.com/swas>.

## Negative-control texts

For experiments that need a non-narrative control (Layer 1 still runs,
but Layer 2 should produce a flatter SWAS profile), we will use short
factual / encyclopedic prose matched on length and topic. Source TBD.

## Licensing / ethics notes

- Raw texts are gitignored — do not commit them, even if public domain.
- Translations or modernized versions: track the source and any rights
  explicitly in `configs/narrative_corpus.yaml`.
- Patriotic / propagandistic Russian-language material (relevant to the
  larger thesis) is held to extra ethical review; see
  [`16-ethics-and-positionality.md`](16-ethics-and-positionality.md).

## Open questions

- _Which two texts for the prototype?_ Decide before W1.
- _Use English-only for the prototype, or include one Russian text?_
  Tentative: English-only for the prototype to reduce variance.

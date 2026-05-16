# 07 — SWAS adaptation for AI readers

The Story World Absorption Scale (SWAS; Kuijpers et al.) measures reading
experience along four dimensions:

- **Attention** — focus on the story; difficulty being distracted.
- **Emotional engagement** — feeling for / with characters.
- **Mental imagery** — vividness of the imagined world.
- **Transportation** — sense of being in the story world.

Source: <https://www.moniekkuijpers.com/swas>. The scale is free for
research use with citation. We do not redistribute the items here; we
reference them and adapt them for an AI-reader context.

## Adaptation for AI readers

For each of the four SWAS dimensions, the agent provides a **probabilistic
0–10 rating** rather than a binary or Likert-5 response. This allows
finer-grained variance to surface from prompt-level differences and is
appropriate for stochastic LLM outputs.

We **add two fields** beyond the original SWAS:

- **Character alignment** (per major character): whether the agent
  identifies with, is sympathetic to, or is antagonistic toward each
  character. Stored as a small dict keyed by character name.
- **Moral-uptake confidence** (0–10): how confident the agent is in its
  verbalized moral interpretation of the story.

These additions make the SWAS output directly useful as input to Layer 3
without losing comparability with the original four dimensions.

## Distinguishing relational constructs

Per [`17-glossary.md`](17-glossary.md), we keep these separate (not all
captured by SWAS):

- perspective taking
- sympathy
- emotional connection
- empathy
- compassion
- familiarity
- positive / negative orientation toward specific characters

Where helpful, we elicit these as fine-grained sub-fields on the
character-alignment dict.

## Implementation note

`readers/swas.py` will:

1. Build the prompt from `prompts/swas_self_report.prompt.md`.
2. Call the LLM with `temperature=0` and JSON mode.
3. Validate the response against a pydantic `SwasResponse` schema.
4. Re-prompt once if validation fails before raising.

## Open questions

- _Should we elicit per-passage SWAS estimates (attention spike on the
  vivid imagery scene), or only story-level?_
- _Is "moral-uptake confidence" redundant with the confidence field on
  the dilemma response in Layer 3?_ Likely no — one measures
  comprehension, the other belief.

# 07 — SWAS adaptation for AI readers

The Story World Absorption Scale (SWAS; Kuijpers, Hakemulder, Tan, &
Doicaru, 2014) measures reading experience along four CFA-validated
dimensions:

- **Attention** — focus on the story; difficulty being distracted.
- **Emotional engagement** — feeling for / with characters.
- **Mental imagery** — vividness of the imagined world.
- **Transportation** — sense of being in the story world.

Reference: Kuijpers et al. (2014), *Exploring absorbing reading
experiences*, Scientific Study of Literature 4(1).
[doi:10.1075/ssol.4.1.05kui](https://doi.org/10.1075/ssol.4.1.05kui).
Project page: <https://www.moniekkuijpers.com/swas>. Local PDF (gitignored):
[`references/kuijpers-2014-swas.pdf`](references/kuijpers-2014-swas.pdf).

## Operational instrument

The canonical item list and metadata live in
[`configs/instruments/swas.yaml`](../configs/instruments/swas.yaml).
That file is the single source of truth — prompts and Python code load
from it; this document only describes the adaptations applied on top of
the original scale.

The 18 items in the YAML are the final CFA solution from Kuijpers et
al. (2014), Table 6: **5 Attention + 5 Transportation + 5 Emotional
Engagement + 3 Mental Imagery**. We do **not** invent new items.

The prototype targets English texts only; the YAML stores `text_en`
per item and is extensible to other language codes without schema
changes.

## Authoritative scoring + CFA reference

Kuijpers' own R analysis script — `psych::alpha()` for per-dimension
Cronbach's α and `lavaan::cfa()` (MLR estimator, first-order and
second-order models) across all 5 SWAS studies — is published on OSF:

- Project: <https://osf.io/zf439/>
- File: <https://osf.io/mhvtb/> — `SWAS dimensions script.R` (1,919 LOC)

When we build the synthetic AI-reader cohort (20–50 agents), we will
port this workflow to Python (`semopy` or `factor_analyzer`) and run
it on the synthetic responses as a manipulation check. The expected
result is *qualitatively* similar α / CFA fit to Kuijpers' human
samples; **systematic divergence is itself a finding** (e.g., synthetic
readers are too internally consistent → insufficient simulated
variance).

## Adaptation for AI readers

Two adaptations applied on top of the original SWAS — encoded as
top-level `scale.adapted` and `additions:` blocks in the YAML so they
remain easy to switch off when comparing against the original 7-point
Likert version:

1. **Probabilistic 0–10 ratings** instead of -3..+3 Likert. This
   allows finer-grained variance to surface from prompt-level
   differences and is appropriate for stochastic LLM outputs.
2. **Two added fields**, kept conceptually separate from the SWAS:
   - **Character alignment** per major character — relational valence
     in `[-10, 10]`. Stored as a dict keyed by character name. Drives
     Layer-3 character-conditioned moral transfer.
   - **Moral-uptake confidence** — single 0–10 rating of comprehension
     confidence in the verbalized moral. Distinct from Layer-3
     dilemma-response confidence.

## Conditioning by reader↔character similarity

The reading-loop step that produces the SWAS self-report passes a
`{{ character_similarity_table }}` slot into the prompt: per-character
cosine similarities between the reader's pseudo-Big5 and each major
character's pseudo-Big5. This *informs* but does not *force* the
character-alignment ratings. See [`05-reader-pipeline.md`](05-reader-pipeline.md)
and [`09-reader-trait-schema.md`](09-reader-trait-schema.md).

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

1. Load items from `configs/instruments/swas.yaml` (cached at process
   start; never inlined into the prompt file).
2. Build the prompt from `prompts/swas_self_report.prompt.md`, passing
   the items list and the character-similarity table as template
   variables.
3. Call the LLM with `temperature=0` and JSON mode.
4. Validate the response against a pydantic `SwasResponse` schema.
5. Re-prompt once if validation fails before raising.

## Open questions

- _Should we elicit per-passage SWAS estimates (attention spike on the
  vivid imagery scene), or only story-level?_
- _Is "moral-uptake confidence" redundant with the confidence field on
  the dilemma response in Layer 3?_ Likely no — one measures
  comprehension, the other belief.
- _When do we replicate the OSF α / CFA workflow on synthetic data?_
  Tentatively, end of prototype Week 8 (after the cohort is sampled).

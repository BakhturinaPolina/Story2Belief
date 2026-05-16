# 17 — Glossary

The literature on narrative engagement uses several terms loosely. This
project keeps the following constructs distinct, both in code (typed
fields) and in writing.

## Reader-side relational constructs

- **Perspective taking** — cognitively imagining what a character thinks
  or sees from their position. *Cognitive*.
- **Empathy** — feeling-with: experiencing affect that resembles the
  character's affect. *Affective*.
- **Sympathy** — feeling-for: a benevolent concern for the character
  *without* sharing their affect.
- **Compassion** — sympathy plus a motivational pull to help.
- **Emotional connection** — a sustained affective bond, not tied to a
  single moment.
- **Familiarity** — recognition: the reader has met someone or something
  like this before. May be cued by similarity slots.
- **Character alignment** — the *valence* of the reader's stance toward
  a character (positive / neutral / negative). Stored per character on
  the SWAS-adapted self-report.

## Narrative engagement constructs (SWAS-aligned)

- **Attention** — focus on the story; resistance to distraction.
- **Emotional engagement** — affective involvement at a story level.
- **Mental imagery** — vividness of the imagined world.
- **Transportation** — sense of being inside the story world.
- **Transportability** — *trait-level* susceptibility to transportation
  across texts. Distinct from a single text's transportation score.
- **Absorption** — the experiential state SWAS measures, of which the
  four dimensions above are facets.

## Persuasion constructs

- **Narrative persuasion** — attitude change produced by narrative
  exposure (Green & Brock).
- **Sleeper effect** — delayed *increase* in attitude change after the
  source of the message has been forgotten or discounted.
- **Source-memory decay** — agent-level parameter representing weakening
  of memory for *where* a belief came from.
- **Moral transfer** — the dependent variable of this project: change in
  moral judgment on a *new* dilemma after narrative exposure.

## Architectural terms (ours)

- **Layer 1 / Narrative pipeline** — text → `NarrativeFeatures`.
- **Layer 2 / AI-reader pipeline** — `ReaderProfile` × text → `ReadingResponse`.
- **Layer 3 / Bridge** — pre/post dilemmas → `TransferDeltas`.
- **Theory-constrained synthetic initialization** — the prototype's way
  of seeding reader traits: not validated population estimates, but
  non-arbitrary ranges informed by the literature.

## Open questions

- _Where does "identification" live_ — is it a special case of
  experience-taking, or a separate construct? Tentative: special case;
  expressed via character alignment + perspective taking + empathy.

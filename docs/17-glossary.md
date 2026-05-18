# 17 — Glossary

The literature on narrative engagement uses several terms loosely. This
project keeps the following constructs distinct, both in code (typed
fields) and in writing. Operational definitions for Layer 1 and Layer 2
are in [`04-narrative-pipeline.md`](04-narrative-pipeline.md),
[`08-narrative-feature-schema.md`](08-narrative-feature-schema.md),
[`09-reader-trait-schema.md`](09-reader-trait-schema.md), and
[`07-swas-adaptation.md`](07-swas-adaptation.md).

## Reader-side relational constructs

These are **reader-relative** — they describe the reader's stance toward
a character or the story, not properties of the text alone.

- **Perspective taking** — cognitively imagining what a character thinks
  or sees from their position. *Cognitive*. Distinct from empathy.
- **Empathy** — feeling-with: experiencing affect that resembles the
  character's affect. *Affective*. Trait-level field: `ReaderProfile.empathy`.
- **Sympathy** — feeling-for: benevolent concern for the character
  *without* sharing their affect.
- **Compassion** — sympathy plus a motivational pull to help.
- **Emotional connection** — a sustained affective bond, not tied to a
  single moment.
- **Prior familiarity** — topic, genre, or lived-experience overlap with
  the story before reading (`ReaderProfile.prior_familiarity`). Distinct
  from demographic match.
- **Perceived similarity** — the reader's subjective sense of being like
  a character (`ReadingResponse.perceived_similarity`, 0–10). Ooms et
  al. (2019) show this predicts identification and transportation better
  than raw demographic matching (Cohen et al. 2018).
- **Self-referencing** — relating story content to the self
  (`ReadingResponse.self_referencing`, 0–10; de Graaf 2014).
- **Character alignment** — the *valence* of the reader's stance toward
  a character (positive / neutral / negative), on `[-10, 10]`. Stored
  per character on the adapted SWAS self-report
  (`SwasResponse.character_alignment`).

## Reader–character matching (prototype)

- **Pseudo-Big5** — a five-dimensional computational proxy
  `(Openness, Conscientiousness, Extraversion, Agreeableness,
  Neuroticism)` ∈ [0, 10]⁵, inspired by Jacobs (2019) and the OCEAN
  model but **not** a validated personality test. Characters: projected
  from text via SentiArt seed words (`configs/instruments/sentiart_big5_seeds.yaml`)
  or an LLM fallback (`character.pseudo_big5`). Readers: sampled
  independently per cohort (`ReaderProfile.pseudo_big5`).
- **Character similarity** — cosine similarity between a reader's
  pseudo-Big5 and a character's pseudo-Big5, computed at read-time
  (`SwasResponse.character_similarity`). Informs but does not force
  character-alignment ratings in the SWAS prompt.

## Narrative engagement constructs (SWAS-aligned)

Source instrument: Kuijpers et al. (2014); operational items in
[`configs/instruments/swas.yaml`](../configs/instruments/swas.yaml).
Local PDF: [`references/kuijpers-2014-swas.pdf`](references/kuijpers-2014-swas.pdf)
(gitignored).

- **Story world absorption** — the experiential state the SWAS measures:
  focused attention on the alternate story world, with reduced awareness
  of the real world and time.
- **Attention** — focus on the story; resistance to distraction. SWAS
  sub-scale (5 items).
- **Emotional engagement** — affective involvement with characters and
  events at a story level. SWAS sub-scale (5 items). Not the same as
  trait empathy.
- **Mental imagery** — vividness of the imagined story world (characters,
  situations, settings). SWAS sub-scale (3 items).
- **Transportation** — sense of being inside or overlapping with the
  story world (deictic shift). SWAS sub-scale (5 items).
- **Transportability** — *trait-level* susceptibility to transportation
  across texts (`ReaderProfile.transportability`). Distinct from a single
  reading's transportation score.
- **Absorption** — umbrella term for the SWAS state; the four dimensions
  above are facets, not causes of each other in every text.

## Narrative text features (Layer 1)

Story-intrinsic measures on `NarrativeFeatures`. See the tool table in
[`04-narrative-pipeline.md`](04-narrative-pipeline.md).

- **Verisimilitude** — degree to which events seem like they could
  happen in the story's world (Cho et al. 2014). Five sub-dimensions on
  `EventLayer`: **plausibility** (Vera commonsense scorer), **typicality**
  (embedding distance to genre reference), **factuality** (WikiData entity
  resolution), **consistency** (cross-link to coherence measures),
  **perceptual_quality** (concreteness + SentiArt AAP).
- **Narrative consistency / coherence** — internal logical fit of the
  story world (Busselle & Bilandzic 2008). Operationalized as
  **coref stability** (BookNLP cluster quality) and **contradiction
  density** (DeBERTa-MNLI sentence-pair contradictions per 100 pairs).
- **Identifiable characters** — characters with stable names, attributed
  quotes, and extractable traits/goals (`character.identifiability`).
- **Emotional figure profile** — per-character valence / arousal / Emotion-
  Potential percentiles within the text (Jacobs 2019; SentiArt).
- **Emotion Potential (EP)** — `|valence| × arousal` at word or scene level;
  story-level mean and scene arc on `story_world.aap_mean` / `aap_arc`.
- **Moral proposition** — a candidate value claim implied by the story,
  with MFT foundation scores, confidence, and ambiguity. May carry a
  **char_interval** (source span from `langextract`) for grounded Layer-3
  comparison.
- **Moral-uptake confidence** — how confident the reader-agent is in its
  verbalized moral interpretation (`SwasResponse.moral_uptake_confidence`).
  Distinct from dilemma-response confidence in Layer 3.

## Persuasion constructs

- **Narrative persuasion** — attitude or belief change produced by
  narrative exposure (Green & Brock 2000; Slater & Rouner 2002).
- **Identification** — alignment with a character's perspective, goals,
  or values. In this project expressed via character alignment, perspective
  taking, empathy, and perceived similarity rather than a separate scale.
- **Experience-taking** — temporarily adopting a character's identity or
  perspective (Kaufman & Libby 2012). Related to but narrower than
  transportation.
- **Sleeper effect** — delayed increase in persuasion after the message
  source is forgotten or discounted (Appel & Richter 2007).
- **Source-memory decay** — agent parameter (`ReaderProfile.source_memory_decay`,
  0–1) modelling weakening of memory for *where* a belief came from.
- **Moral transfer** — dependent variable of Layer 3: change in moral
  judgment on a *new* dilemma after narrative exposure (choice, confidence,
  justification similarity to the story's moral).

## Instruments and configs (ours)

- **SWAS (adapted)** — Story World Absorption Scale items elicited from
  AI readers on 0–10 scales instead of the original −3..+3 Likert. Items
  loaded from `configs/instruments/swas.yaml`; not redistributed in prompts.
- **Theory-constrained synthetic initialization** — reader traits sampled
  from literature-informed ranges, not from a representative human population.

## Architectural terms (ours)

- **Layer 1 / Narrative pipeline** — text → `NarrativeFeatures` (BookNLP,
  `langextract`, SentiArt, Vera, NLI).
- **Layer 2 / AI-reader pipeline** — `ReaderProfile` × text → `ReadingResponse`
  (Concordia-style agent + adapted SWAS).
- **Layer 3 / Bridge** — pre/post dilemmas → `TransferDeltas`.

## Deferred / out of prototype scope

- **Foregrounding** — stylistic deviation from linguistic norm that draws
  attention to form (Miall & Kuiken; Shklovsky). Hypothesized to *oppose*
  transportation (Kuijpers et al. 2014 H2). Year 1+ only.
- **LIWC-22** — lexicon-based psycholinguistic tagger (Pennebaker et al.
  2022). Evaluated and excluded from the prototype; local manual at
  [`references/liwc-22-manual.pdf`](references/liwc-22-manual.pdf) (gitignored).

## Open questions

- _Should "identification" become a first-class field_, or remain a
  composite of alignment + perspective taking + perceived similarity?
- _Do we need a separate scale for narrative presence_ distinct from
  transportation, following Busselle & Bilandzic (2009)?

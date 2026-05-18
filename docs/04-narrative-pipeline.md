# 04 — Narrative-analysis pipeline (Layer 1)

The narrative pipeline turns each text into a structured
`NarrativeFeatures` record (see
[`08-narrative-feature-schema.md`](08-narrative-feature-schema.md) for the
schema). It is **interpretable by design**: each feature has a clear
provenance (BookNLP, `langextract`, SentiArt, Vera, an NLI model, an LLM
prompt, or a hand-coded heuristic).

The prototype targets **English texts only**.

## Tool responsibilities per feature family

The pipeline uses three complementary primary taggers plus a small set
of supporting models. Tools are **not substitutes**:

- **BookNLP** is deterministic and cheap; it handles the "who/what is
  mentioned, who said what, where, when" layer.
- **`langextract`** is LLM-driven with source grounding; it handles
  the semantic / interpretive features (morals, scene boundaries, POV,
  character traits and goals, causal links).
- **SentiArt** computes valence / arousal / Emotion-Potential at word,
  scene, and story level, plus pseudo-Big5 per character.

| # | Feature family | Primary tagger | Operationalization | Output fields |
|---|---|---|---|---|
| 1 | **Verisimilitude** (Cho et al. 2014) | **Vera** + sentence-embedding NN + WikiData + LLM fallback | Plausibility from Vera over event statements; typicality from `all-MiniLM-L6-v2` distance to per-genre reference corpus; factuality from WikiData entity-linking ratio over BookNLP entities; consistency cross-linked from family #2; perceptual quality cross-linked from family #5. | `event.{plausibility, typicality, factuality, consistency, perceptual_quality}` |
| 2 | **Narrative consistency** (Busselle & Bilandzic 2008) | **BookNLP coref** + **DeBERTa-v3-MNLI** | Coref-chain stability (BookNLP cluster mention ratio) + contradiction density (sliding-window sentence-pair NLI, `P(contradiction) > 0.7`, per 100 pairs). | `event.coref_stability`, `event.contradiction_density` |
| 3 | **Identifiable-character density** (van Laer 2014 ρ≈.20) | **BookNLP** + `langextract` | Named characters with stable coref cluster, ≥1 quote (BookNLP), ≥1 attributed trait/goal (`langextract`). | `character.count`, `character.salience`, `character.identifiability` |
| 4 | **POV / focalization** | `langextract` + BookNLP pronoun-ratio sanity check | Categorical with confidence. | `character.pov_type`, `character.pov_confidence` |
| 5 | **Imaginable plot / scene concreteness** (van Laer 2014 ρ≈.29) | **SentiArt** + Brysbaert concreteness norms + BookNLP supersense densities | Scene-level concreteness + sensory density + named-place density + AAP arc. | `story_world.{concreteness, sensory_density, named_place_density, aap_arc}` |
| 6 | **Eventfulness / conflict / causal clarity** | **BookNLP** event tagger + `langextract` causal-link extraction | Events per 100 tokens; conflict-tagged subset; LLM-rated causal clarity with grounded evidence spans. | `event.{eventfulness, conflict_density, causal_clarity}` |
| 7 | **Emotional intensity** | **SentiArt** | Mean EP + emotional-peak count (scene EP z-score > 2). | `story_world.{aap_mean, emo_peaks}` |
| 8 | **Character pseudo-Big5** (Jacobs 2019) | **SentiArt** seed-word projection; LLM fallback | OCEAN percentiles via fastText `cc.en.300`; LLM fallback uses BookNLP quotes + `langextract` traits. | `character.pseudo_big5[name]`, `character.pseudo_big5_method[name]` |
| 9 | **Character emotional figure profile** | **SentiArt** | Per-character within-text percentiles of valence / arousal / EP. | `character.affect_map[name].{valence_percentile, arousal_percentile, ep_percentile}` |
| 10 | **Moral propositions + MFT** | **`langextract`** with Hobson-style staged prompts | Each proposition carries a `char_interval` for downstream grounded comparisons in Layer 3. | `moral.propositions` |

## Why `langextract` rather than hand-rolled LLM calls

Four properties we would otherwise have to reinvent:

1. **Source grounding by construction.** Every extracted entity carries
   a `char_interval`. For moral propositions this is critical: Layer 3's
   justification-embedding similarity can be computed against the
   grounded supporting passage rather than the whole story.
2. **Few-shot schema enforcement** via controlled generation (Gemini)
   or JSON mode (OpenAI). Failures become explicit alignment warnings,
   not silent garbage.
3. **Multi-pass + chunking + parallelism** out of the box.
4. **Interactive HTML viz** (`lx.visualize`) for prototype QA.

See [`12-tools-and-resources.md`](12-tools-and-resources.md) for repo
links and pinned versions.

## Modules

| Module | File | Status |
|--------|------|--------|
| Schema | `narrative/schema.py` | placeholder |
| Characters / POV (BookNLP wrapper) | `narrative/characters.py` | placeholder |
| Sentiment / aesthetics (SentiArt) | `narrative/sentiment.py` | placeholder |
| Discourse (`langextract` scenes/POV/traits) | `narrative/discourse.py` | placeholder |
| Story-world (concreteness + supersense) | `narrative/story_world.py` | placeholder |
| Moral extraction (`langextract` + Hobson) | `narrative/moral_extraction.py` | placeholder |
| Verisimilitude (Vera + NLI) | `narrative/verisimilitude.py` | not yet stubbed |
| Orchestration | `narrative/pipeline.py` | placeholder |

## Validation strategy

- **Manual sample**: hand-annotate a handful of features on the two
  prototype texts; compare against pipeline outputs.
- **Inter-prompt agreement**: run moral extraction at two temperatures /
  two prompt variants; report agreement.
- **Theory checks**: the fairy tale should score lower
  plausibility/factuality and higher story-world distance than the
  realistic short story.
- **Optional cross-check** (Year 1+): run [`andyreagan/core-stories`](https://github.com/andyreagan/core-stories)
  on the two prototype texts and compare its emotional-arc decomposition
  against our SentiArt `aap_arc`.

## Year 1+ extensions (deliberately out of scope for the prototype)

- **Foregrounding / style deviation** (Miall & Kuiken 1995; Hakemulder
  2004). Stylistic deviation from norm — phonetic, lexical, syntactic,
  or semantic — that arrests automatic comprehension and draws
  attention to the form. In SWAS terms it *opposes* transportation
  (Kuijpers et al. 2014 H2). Operationalization is contested (gold
  standard is hand-coding "striking" passages per 100 words);
  computational proxies include metaphor density, simile count, and
  lexical-rarity z-scores against a reference corpus. Out of scope for
  the prototype because (a) two prototype texts make norm-relative
  metrics noisy, (b) it does not sit on the moral-transfer DV path,
  and (c) it requires a larger reference corpus.
- **Passage-level attention maps** — per-passage SWAS-attention
  estimates rather than story-level averages.
- **Narrative event chains** ([`kirubarajan/narrative_chains`](https://github.com/kirubarajan/narrative_chains))
  for causal-density analysis beyond an LLM rating.
- **Story knowledge graphs** for richer relational features.

## Open questions

- _Where do we draw the line between story-intrinsic and reader-relative
  features?_ Reader-similarity is computed only at Layer-2 read-time.
- _Should the pipeline emit passage-level features for downstream
  attention modeling, or only story-level?_
- _Do we fold the BookNLP supersense distribution into
  `story_world.sensory_density` directly, or keep it as a separate
  `supersense_distribution` field?_

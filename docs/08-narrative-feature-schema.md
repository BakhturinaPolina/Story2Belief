# 08 — Narrative feature schema

The canonical schema lives in `src/story2belief/narrative/schema.py`. This
document mirrors it in JSON-shape form so it can be cited from prompts and
from external tools.

## Top-level shape

```json
{
  "text_id": "string",
  "title": "string",
  "genre": "fairy_tale | realistic | …",
  "language": "string",
  "character": {
    "count": 0,
    "protagonist": "string",
    "pov_type": "first_person | close_third | omniscient | multi_perspective",
    "pov_confidence": 0.0,
    "dialogue_share": 0.0,
    "identifiability": 0.0,
    "salience": { "<character_name>": 0.0 },
    "affect_map": {
      "<character_name>": {
        "sympathy": 0.0,
        "compassion": 0.0,
        "empathy": 0.0,
        "perspective_taking": 0.0,
        "valence": 0.0,
        "valence_percentile": 0.0,
        "arousal_percentile": 0.0,
        "ep_percentile": 0.0
      }
    },
    "pseudo_big5": {
      "<character_name>": [0.0, 0.0, 0.0, 0.0, 0.0]
    },
    "pseudo_big5_method": {
      "<character_name>": "sentiart | llm_fallback"
    }
  },
  "event": {
    "eventfulness": 0.0,
    "conflict_density": 0.0,
    "causal_clarity": 0.0,
    "temporal_linearity": 0.0,
    "narrative_distance": 0.0,
    "realism": 0.0,
    "plausibility": 0.0,
    "typicality": 0.0,
    "factuality": 0.0,
    "consistency": 0.0,
    "perceptual_quality": 0.0,
    "coref_stability": 0.0,
    "contradiction_density": 0.0
  },
  "story_world": {
    "concreteness": 0.0,
    "sensory_density": 0.0,
    "named_place_density": 0.0,
    "world_proximity": 0.0,
    "imagery_passages": 0,
    "aap_mean": 0.0,
    "aap_arc": [],
    "emo_peaks": 0
  },
  "moral": {
    "propositions": [
      {
        "text": "string",
        "foundations": {
          "care_harm": 0.0,
          "fairness_cheating": 0.0,
          "loyalty_betrayal": 0.0,
          "authority_subversion": 0.0,
          "sanctity_degradation": 0.0
        },
        "confidence": 0.0,
        "ambiguity": 0.0,
        "char_interval": [0, 0]
      }
    ],
    "behavioral_lessons": ["string"]
  },
  "provenance": {
    "prompt_versions": { "moral_extraction": "v0" },
    "tool_versions": {
      "booknlp": "x.y.z",
      "langextract": "x.y.z",
      "sentiart_commit": "abcdef0",
      "vera_model": "liujch1998/vera",
      "nli_model": "microsoft/deberta-v3-large-mnli",
      "fasttext_vsm": "cc.en.300"
    },
    "model_id": "string",
    "git_sha": "string",
    "created_at": "ISO-8601 timestamp"
  }
}
```

## Notes on field semantics

- All `[0.0–1.0]` fields are normalized 0-to-1; all `[0–10]` fields are
  rounded 0-to-10 ratings; percentile fields are 0-to-100. The schema
  enforces ranges.
- `affect_map` keys are character names; values use the distinct relational
  constructs from [`17-glossary.md`](17-glossary.md). The three percentile
  fields (`valence_percentile`, `arousal_percentile`, `ep_percentile`) are
  Jacobs (2019) *emotional figure profile* values: each character's
  position within the within-text distribution of characters.
- `pseudo_big5[name]` is a 5-tuple `(Openness, Conscientiousness,
  Extraversion, Agreeableness, Neuroticism)` ∈ [0, 10]⁵, produced by
  SentiArt's seed-word projection (Jacobs 2019 §"Pseudo-Big 5") or by an
  LLM fallback when SentiArt token coverage for the character is too thin.
  `pseudo_big5_method` records which path was taken. This is **not** a
  validated personality measurement; it is an interpretable computational
  proxy that drives reader↔character similarity matching at read-time.
- `event.plausibility` is the Vera (`liujch1998/vera`) commonsense-
  plausibility score aggregated over events extracted by BookNLP +
  `langextract`. `event.typicality` is one minus the mean
  sentence-embedding distance to a small genre reference corpus.
  `event.factuality` is the fraction of BookNLP-extracted entities that
  resolve to WikiData. `event.consistency` is cross-linked to
  `event.coref_stability` and `event.contradiction_density`.
- `event.coref_stability` ∈ [0, 1] is the BookNLP cluster-mention
  consistency. `event.contradiction_density` is the count of sentence-pair
  contradictions (DeBERTa-v3-MNLI, `P(contradiction) > 0.7`) per 100
  sentence pairs in a sliding window.
- `story_world.aap_arc` is a list of per-scene Emotion-Potential
  percentiles in scene order; `story_world.aap_mean` is the story-level
  mean; `story_world.emo_peaks` is the count of scenes with EP z-score
  > 2. Provenance: SentiArt over a per-text fastText VSM (`cc.en.300`).
- `moral.propositions` is a list — we deliberately allow multiple
  candidate morals with confidence and ambiguity, instead of forcing one
  canonical moral. Each proposition carries a `char_interval` pointing
  into the source text (provided by `langextract`); Layer 3 can compute
  justification-embedding similarity against the *grounded supporting
  passage* rather than the whole story.
- `provenance` is required for every record; it is what makes the output
  reproducible. `tool_versions` records the exact tagger versions so we
  can compare runs across BookNLP / Vera / NLI model upgrades.

## Tool responsibilities per family

See [`04-narrative-pipeline.md`](04-narrative-pipeline.md) for the full
table mapping each feature family to its primary tagger. In brief:

- **BookNLP** — characters, coref, quotes, supersense, events.
- **`langextract`** — morals, scenes, POV, traits, goals, causal links.
- **SentiArt** — valence, arousal, EP arc, character emotional and
  pseudo-Big5 profiles.
- **Vera** + sentence embeddings + WikiData — verisimilitude sub-dims.
- **DeBERTa-v3-MNLI** — within-text contradiction density.

## Worked example

A worked example for one fairy tale and one realistic short story will be
generated by `scripts/run_narrative_pipeline.py` and stored under
`data/processed/narrative_features/`. This file will be linked here once
those records exist.

## Open questions

- _Do we want a passage-level addendum (`scenes: [...]`) for downstream
  attention modeling?_
- _Should the foundation distribution sum to 1, or be independent
  intensities?_ Tentative answer: independent intensities, since stories
  often touch multiple foundations at once.

# 04 — Narrative-analysis pipeline (Layer 1)

The narrative pipeline turns each text into a structured
`NarrativeFeatures` record (see
[`08-narrative-feature-schema.md`](08-narrative-feature-schema.md) for the
schema). It is **interpretable by design**: each feature has a clear
provenance (BookNLP, SentiArt, an LLM prompt, or a hand-coded heuristic).

## Feature families

### Character layer

- Number of characters, protagonist salience, dialogue share.
- Character-network position (BookNLP-derived).
- POV / focalization: `first_person`, `close_third`, `omniscient`,
  `multi_perspective`.
- Character-affect map: emotions toward protagonist / antagonist /
  secondary characters.
- Reader-similarity slots (computed at runtime, not stored on the text):
  age, gender, biographical, occupational, value overlap.

### Event layer

- Eventfulness score, conflict density, causal clarity.
- Temporal linearity vs. nonlinearity.
- Presentness / pastness, narrative distance.
- Realism / plausibility (0–10).

### Story-world layer

- Concreteness, sensory detail density, named-place density.
- World proximity to ordinary reality vs. fantastic setting.
- Imagery-promoting passages (count + locations).

### Moral layer

- One or more **moral propositions** (with confidence + ambiguity score).
- Associated moral-foundation distribution (care/harm, fairness/cheating,
  loyalty/betrayal, authority/subversion, sanctity/degradation).
- Behavioral lessons (`if X, then Y` style).

## Modules

| Module | File | Status |
|--------|------|--------|
| Schema | `narrative/schema.py` | placeholder |
| Characters / POV | `narrative/characters.py` | placeholder (BookNLP wrapper) |
| Sentiment / aesthetics | `narrative/sentiment.py` | placeholder (SentiArt) |
| Discourse | `narrative/discourse.py` | placeholder (LLM prompt) |
| Story-world | `narrative/story_world.py` | placeholder (LLM prompt) |
| Moral extraction | `narrative/moral_extraction.py` | placeholder (Hobson-style) |
| Orchestration | `narrative/pipeline.py` | placeholder |

## Validation strategy

- **Manual sample**: hand-annotate a handful of features on the two
  prototype texts; compare against pipeline outputs.
- **Inter-prompt agreement**: run moral extraction at two temperatures /
  two prompt variants; report agreement.
- **Theory checks**: the fairy tale should score lower realism and higher
  story-world distance than the realistic short story.

## Open questions

- _Where do we draw the line between story-intrinsic and reader-relative
  features?_ Reader-similarity is computed only at Layer-2 read-time.
- _Should the pipeline emit passage-level features for downstream
  attention modeling, or only story-level?_

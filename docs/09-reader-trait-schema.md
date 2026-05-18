# 09 — Reader trait schema

The canonical schema lives in `src/story2belief/readers/profile.py`.

The trait set distils the meta-analytic and high-citation evidence from
the Core Narrative Transportation and Persuasion literature synthesis
(van Laer et al. 2014; Mazzocco et al. 2010; Appel & Richter 2010;
Zwarun & Hall 2012; Thompson et al. 2018; Cohen et al. 2018) into a
parsimonious 8-trait set plus a pseudo-Big5 field.

## Core traits (prototype)

| Trait | Range | Source | Why included |
|-------|-------|--------|--------------|
| `transportability` | 0–10 | Mazzocco et al. 2010 | van Laer meta-analysis ρ ≈ .30 with transportation — strongest reader-side moderator. |
| `empathy` (trait) | 0–10 | IRI / Thompson et al. 2018 | Independently predicts transportation across film genres. |
| `need_for_affect` | 0–10 | Appel & Richter 2010 | Mediates persuasion via transportation; Sobel z ≈ 2.0–2.5 in two experiments. |
| `need_for_cognition` | 0–10 | Zwarun & Hall 2012 | Keeps cognitive-style variation on the table even in affective contexts. |
| `sensation_seeking` | 0–10 | Thompson et al. 2018 | Independent of empathy as a transportation predictor across genres. |
| `prior_familiarity` | 0–10 | Green 2004; van Laer et al. 2014 ρ ≈ .21 | Topic + genre + lived-experience familiarity (renamed from `theme_relevance`). |
| `reading_exposure` | 0–10 | Author Recognition Test family | Habitual exposure to literary fiction. |
| `baseline_moral_foundation_scores` | dict[5] of 0–10 | MFQ-style | Pre-existing moral profile for Layer-3 deltas. |
| `pseudo_big5` | tuple[5] of 0–10 | OCEAN | Drives reader↔character similarity matching; **sampled independently** of the other traits. |
| `source_memory_decay` | 0–1 | Sleeper-effect parameter | Year-1 use; kept on the schema for forward-compat. |

## Dropped from the previous schema

- `realism_preference` — too thin a construct on its own; the same
  variance is captured by `sensation_seeking` (inversely) combined with
  `prior_familiarity` for realistic-genre readers.

## Renamed

- `theme_relevance` → `prior_familiarity` (matches the meta-analysis
  vocabulary and broadens to topic + genre + lived experience).

## Pseudo-Big5 — important caveats

`pseudo_big5` is a 5-tuple `(O, C, E, A, N)` ∈ [0, 10]⁵ used to compute
reader↔character cosine similarity at read-time. Two deliberate prototype
choices:

1. **Independent sampling.** Each Big5 dimension is drawn from a
   truncated-normal `N(5.5, 1.8²)` clipped to `[0, 10]`, independent of
   the other traits. This is to avoid collinearity at small N (20–50
   readers) and to maximise variance for matching, **not** because the
   true Big5 is statistically independent of NFC / NFA / empathy.
2. **Not a personality measurement.** Following Jacobs (2019), we call
   this "pseudo-Big5" to make clear it is an *interpretable
   computational proxy* used for matching, not a validated psychometric
   instrument. We make no claims about real-population correspondence.

The matching itself happens at read-time in `readers/reading_loop.py`:

```text
sim(reader, char) = cosine(reader.pseudo_big5, char.pseudo_big5)
```

The similarity vector is passed into the SWAS-self-report prompt
(`{{ character_similarity_table }}`) so that character-alignment ratings
are *informed by* but not *forced by* it, and stored on the
`ReadingResponse` for analysis.

## Computed at read-time (not stored on `ReaderProfile`)

These are reader-relative features that depend on the specific text and
therefore live on `ReadingResponse`, not `ReaderProfile`:

- `character_similarity` — per-character cosine similarities (Big5).
- `perceived_similarity` — agent-elicited one-item rating, 0–10 (Ooms
  et al. 2019).
- `self_referencing` — agent-elicited 0–10 after reading (de Graaf 2014).

We deliberately do **not** model demographic similarity slots on the
text-side schema: Cohen et al. (2018) showed that raw demographic match
(sex, nationality, age, city) does not reliably increase identification
or persuasion. Perceived similarity, captured at read-time, does.

## Encoding choice

For the prototype, all scalar traits are **0–10 floats**. This is
*theory-constrained synthetic initialization*: we do not claim to mirror
a real population, only to demonstrate model tractability and causal
structure.

## Sampling

`readers/cohort.py` samples from theory-constrained ranges and ensures
coverage of extreme contrasts (high transportability + low NFC vs. its
mirror, high empathy + low sensation-seeking vs. its mirror) so that
trait-driven differences are visible at small N.

## Open questions

- _Should `baseline_moral_foundation_scores` be drawn jointly (clusters
  of liberal / conservative profiles) or independently?_
- _Should `sensation_seeking` and `prior_familiarity` get their own
  contrast pairs in `configs/reader_profiles.yaml`?_ Probably yes — they
  are the two new traits with the strongest meta-analytic backing.
- _How do we represent the "Russian patriotic education" scenario in
  the trait schema for later years — as a covariate, a bias on baseline
  foundations, or a separate context object?_

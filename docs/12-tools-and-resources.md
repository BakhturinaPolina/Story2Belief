# 12 — Tools and resources

A concise appendix of the open-source tools, datasets, and conceptual
references used across the project. This file is also reusable for
funding applications.

The prototype targets **English texts only**. Tool versions / commits
are pinned in `provenance.tool_versions` on every record; this file
records the *current pinned versions* used by the prototype.

## A. Computational tools and datasets

### Layer-1 primary taggers

- **BookNLP** — NLP pipeline for books and other long English documents:
  POS tagging, dependency parsing, NER, cross-document character
  clustering, coreference resolution (big-model F1 ≈ 79.0), quote
  attribution, supersense tagging (`animal`, `artifact`, `body`,
  `cognition`, …), event tagging (F1 ≈ 74.1), referential gender
  inference. Outputs `.tokens`, `.entities`, `.supersense` per text.
  Used for feature families #3, #4, #6 and as the entity provider for
  #1, #2, #8.
  Repo: <https://github.com/booknlp/booknlp> (915★, MIT).
  Pinned commit: TBD on first wire-up.

- **`langextract`** — Python library from Google for LLM-driven
  structured extraction with **source grounding** (`char_interval` on
  every entity), few-shot schema enforcement, multi-pass + chunking +
  parallelism, and an interactive HTML viewer. Supports Gemini, OpenAI,
  Ollama-served local models. Used for feature families #4, #6, #10
  (morals).
  Repo: <https://github.com/google/langextract> (Apache 2.0).
  Pinned version: `langextract>=1.0` (PyPI).

- **SentiArt** — VSM-based literary-sentiment tool (Jacobs 2019). No
  dictionary required; runs on top of any fastText VSM (≥150 languages
  available). Used for valence / arousal / Emotion-Potential per word,
  scene, story, and for the per-character emotional figure profile and
  pseudo-Big5 (Jacobs 2019 §"Pseudo-Big 5"). Used for families #5
  (concreteness contribution), #7, #8, #9.
  Repo: <https://github.com/matinho13/SentiArt>.
  Pinned commit: TBD on first wire-up.
  VSM: public fastText `cc.en.300.bin` (English-only prototype).

### Layer-1 supporting models

- **Vera** — General-purpose commonsense plausibility classifier
  (Liu et al. EMNLP 2023; T5-XXL). Returns a calibrated 0–1 score per
  declarative statement; trained on ~7M commonsense statements;
  outperforms GPT-3.5 / 4 on plausibility benchmarks. Used for the
  plausibility sub-dimension of verisimilitude (#1).
  Repo: <https://github.com/liujch1998/vera>.
  HF model: `liujch1998/vera`.
  Pinned model rev: TBD on first wire-up.

- **`microsoft/deberta-v3-large-mnli`** — NLI classifier used for
  within-text contradiction density (#2). Sliding window over scene
  sentence-pairs; count pairs where `P(contradiction) > 0.7`.
  HF model: `microsoft/deberta-v3-large-mnli`.

- **`sentence-transformers/all-MiniLM-L6-v2`** — Sentence embeddings
  used for typicality (k-NN distance to per-genre reference corpus) and
  for Layer 3 justification-similarity.

- **Brysbaert et al. (2014) concreteness ratings** — 40k English-word
  concreteness norms (CSV). Used for the concreteness sub-component of
  family #5.
  Paper: <http://crr.ugent.be/papers/Brysbaert_Warriner_Kuperman_BRM.pdf>.

- **WikiData** — Entity-resolution target for the factuality
  sub-dimension of #1. Optional dependency on `wikidata-graph-builder`
  or REL for entity linking; if not installed, factuality reverts to an
  LLM-fallback rating.

### Year-1+ / optional Layer-1 references

- **`andyreagan/core-stories`** — Reagan et al. (2016) "Emotional arcs
  of stories": classifies texts into six fundamental arc shapes via
  matrix decomposition + supervised + unsupervised learning. Useful as
  a Year-1 cross-check for our SentiArt `aap_arc`.
  Repo: <https://github.com/andyreagan/core-stories>.

- **`kirubarajan/narrative_chains`** — Chambers & Jurafsky (2008)
  narrative event chains over spaCy dependency parses. Useful for
  Year-1 causal-density features beyond an LLM rating.
  Repo: <https://github.com/kirubarajan/narrative_chains>.

- **`LIAAD/Text2StoryPackage`** — Events, participants, temporal
  expressions, semantic-role and objectal links. Year-1+ for richer
  event-chain analysis.
  Repo: <https://github.com/LIAAD/Text2StoryPackage>.

- **`tangg555/NGEP-eventplan`** — Graph-based event planning for
  stories. Year-1+ if we add scene-graph features.
  Repo: <https://github.com/tangg555/NGEP-eventplan>.

- **Piper & Bagga (2024)** — *Using Large Language Models for
  Understanding Narrative Discourse* (ACL WNU 2024). Annotation scheme
  for narrative discourse across dialogue / entities / tense /
  emotionality / conflict / eventfulness over 18 genres; their
  few-shot examples are a useful reference for our `langextract`
  prompt design.
  Paper: <https://aclanthology.org/2024.wnu-1.4/>.

- **`davidghobson1/llm-story-morals`** (a.k.a. `llm-story-morals`) —
  Hobson et al. (2024) staged moral-extraction prompts, codebooks, and
  validation code. Used as the prompt template basis for our
  `langextract` moral-extraction examples.
  Repo: <https://github.com/davidghobson1/llm-story-morals>.

### Moral content in stories and dilemmas

- **MoralStory / STORAL** — short stories paired with annotated morals.
  <https://github.com/thu-coai/MoralStory>.
- **Moral Stories** — situated moral narratives with norms, intents,
  actions, outcomes.
  <https://github.com/demelin/moral_stories>.
- **MoralBERT** — Moral-Foundations-aligned classifier for text.
  <https://github.com/vjosapreniqi/MoralBERT>.

### Narrative structure (legacy references kept for citation)

- **Narrative-Discourse** — LLM-based narrative-discourse code (Piper &
  Bagga lineage). <https://github.com/PlusLabNLP/Narrative-Discourse>.

### Generative agent-based modeling

- **Concordia** — DeepMind library for generative agent-based modeling
  with memory, reflection, and grounded action.
  <https://github.com/google-deepmind/concordia>.

### Tools evaluated and excluded from the prototype

- **LIWC-22** (Pennebaker et al. 2022). Closed-source, paid (~US$90
  academic licence), English-first. Local manual (gitignored):
  [`references/liwc-22-manual.pdf`](references/liwc-22-manual.pdf).
  Categories we considered useful
  (Narrative Arc, Moralization, Perception subscales, Analytic /
  Clout / Authentic / Tone summary variables) are covered well enough
  for the prototype by SentiArt + `langextract` + BookNLP supersense
  densities. Re-evaluate in Year 1 if an experiment specifically needs
  Boyd et al.'s Narrative Arc module or LIWC's validated
  linguistic-style summary variables. No further integration work for
  the prototype.

## B. Conceptual / empirical references

### Reading experience and absorption

- Kuijpers et al. (2014) — Story World Absorption Scale (SWAS).
  <https://www.moniekkuijpers.com/swas>.
  Authoritative scoring + CFA script: OSF
  <https://osf.io/zf439> file `mhvtb` (`SWAS dimensions script.R`,
  `psych::alpha` + `lavaan::cfa` MLR over 5 studies).
- Piper & Bagga (2024) — *Using Large Language Models for Understanding
  Narrative Discourse*.
  <https://aclanthology.org/2024.wnu-1.4/>.

### Moral extraction and moral evolution

- Hobson et al. (2024) — *Story morals: Surfacing value-driven narrative
  schemas using large language models* (EMNLP 2024).
- Chuang et al. (2024) — *Simulating opinion dynamics with networks of
  LLM-based agents* (NAACL Findings).

### LLMs, generative agents, ABM

- Gao et al. (2024) — survey on LLM-empowered ABM.
- Park et al. (2023) — *Generative Agents: Interactive Simulacra of
  Human Behavior* (UIST).
- Vezhnevets et al. (2023) — Concordia paper.
- Aher et al. (2023) — LLMs simulating multiple humans.

### Narrative persuasion and individual differences

(See the local literature synthesis at
[`references/core-narrative-transportation-persuasion-phd.pdf`](references/core-narrative-transportation-persuasion-phd.pdf)
— gitignored, not on GitHub. Key papers below.)

- Green & Brock (2000) — narrative transportation and persuasion.
- Slater & Rouner (2002) — entertainment-education and reduced
  counterarguing.
- Green (2004) — prior knowledge and perceived realism.
- Busselle & Bilandzic (2008) — fictionality and perceived realism;
  mental-model framework.
- Busselle & Bilandzic (2009) — narrative engagement scale.
- Escalas (2007) — self-referencing as a route to persuasion.
- de Graaf et al. (2012) — identification as a mechanism of narrative
  persuasion (perspective manipulation).
- Mazzocco et al. (2010) — transportability as an individual difference.
- Appel & Richter (2010) — need for affect → transportation →
  persuasion.
- Zwarun & Hall (2012) — need for cognition in narrative film.
- Cho et al. (2014) — perceived realism dimensions (plausibility,
  typicality, factuality, narrative consistency, perceptual quality).
- van Laer et al. (2014) — meta-analysis of antecedents and
  consequences of narrative transportation.
- de Graaf (2014); Chen et al. (2016); Cohen et al. (2018);
  Ooms et al. (2019) — protagonist similarity, perceived similarity,
  and self-referencing.
- Thompson et al. (2018) — empathy and sensation seeking as
  transportation predictors.
- Appel & Richter (2007) — sleeper effect in narrative persuasion.
- Marsh & Fazio (2006) — learning errors from fiction.
- Kaufman & Libby (2012) — experience-taking.
- Mar, Oatley & Peterson (2009) — fiction reading and empathy.
- Nijhof & Willems (2015) — fMRI evidence on individual differences in
  fiction simulation.
- Jacobs & Willems (2017) — neurocognitive correlates of literary
  engagement.
- Zunshine (2006) — theory-of-mind account of fiction reading.
- Gerrig (1993) — *Experiencing Narrative Worlds*.

### Moral contagion, conformity, AI as social mirror

- Brady, Crockett & Van Bavel (2020) — MAD model.
- Kuran (1995) — preference falsification.
- Alava (2025) — patriotic education in contemporary Russia.
- Ge et al. (2024) — cultural variation in what people want from AI.
- Guingrich & Graziano (2025) — chatbots as social companions.

## C. Citations

BibTeX for all of the above lives in `references.bib`. Always cite the
exact version / commit when using a tool from a public repo.

## Open questions

- _Which fastText VSM size for SentiArt?_ `cc.en.300.bin` is ~4.5 GB.
  We may prefer a smaller `wiki.en.bin` or a domain-trained VSM trained
  on our two prototype texts (Jacobs 2019's approach for Harry Potter).
  Decide when the sentiment module is wired.
- _Do we need a dedicated audio-narrative tool family?_ Not for the
  prototype.

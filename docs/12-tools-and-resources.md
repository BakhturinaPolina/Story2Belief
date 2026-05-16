# 12 — Tools and resources

A concise appendix of the open-source tools, datasets, and conceptual
references used across the project. This file is also reusable for funding
applications.

## A. Computational tools and datasets

### Narrative sentiment, imagery, aesthetics

- **SentiArt** — vector-space model for literary sentiment and imagery.
  Useful for emotional tone, aesthetic valence, imagery features.
  <https://github.com/matinho13/SentiArt>

### Moral content in stories and dilemmas

- **MoralStory / STORAL** — short stories paired with annotated morals.
  <https://github.com/thu-coai/MoralStory>
- **llm-story-morals** — prompts, codebooks, and validation code for
  Hobson et al.'s moral-extraction pipeline.
  <https://github.com/davidghobson1/llm-story-morals>
- **Moral Stories** — situated moral narratives with norms, intents,
  actions, outcomes.
  <https://github.com/demelin/moral_stories>
- **MoralBERT** — Moral-Foundations-aligned classifier for text.
  <https://github.com/vjosapreniqi/MoralBERT>

### Narrative structure, characters, events

- **BookNLP** — long-form narrative entity extraction; characters,
  coreference, quotation attribution.
  <https://github.com/dbamman/book-nlp>
- **Narrative-Discourse** — LLM-based narrative-discourse code (Piper &
  Bagga lineage).
  <https://github.com/PlusLabNLP/Narrative-Discourse>

### Generative agent-based modeling

- **Concordia** — DeepMind library for generative agent-based modeling
  with memory, reflection, and grounded action.
  <https://github.com/google-deepmind/concordia>

## B. Conceptual / empirical references

### Reading experience and absorption

- Kuijpers et al. — Story World Absorption Scale (SWAS).
  <https://www.moniekkuijpers.com/swas>.
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

- Gerrig (1993) — *Experiencing Narrative Worlds*.
- Green & Brock (2000) — narrative transportation and persuasion.
- Appel & Richter (2007) — sleeper effect in narrative persuasion.
- Marsh & Fazio (2006) — learning errors from fiction.
- Kaufman & Libby (2012) — experience-taking.
- Mar, Oatley & Peterson (2009) — fiction reading and empathy.
- Mazzocco et al. (2010) — transportability as an individual difference.
- Nijhof & Willems (2015) — fMRI evidence on individual differences in
  fiction simulation.
- Jacobs & Willems (2017) — neurocognitive correlates of literary
  engagement.
- Zunshine (2006) — theory-of-mind account of fiction reading.

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

- _Should we add a dedicated audio-narrative tool family?_ Probably not
  for the prototype.

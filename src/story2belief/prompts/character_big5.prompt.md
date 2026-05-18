<!--
prompt_id: character_big5.v0
purpose: >-
  LLM fallback for character pseudo-Big5 when SentiArt VSM coverage on
  the character's tokens is too thin to project them reliably. Produces
  a 5-tuple (Openness, Conscientiousness, Extraversion, Agreeableness,
  Neuroticism) on 0-10 scales for a single character given evidence
  spans extracted by BookNLP (quotes) and langextract (traits, goals,
  backstory markers).
inputs:
  - text_id (str)
  - character_name (str)
  - quotes (list[str]) -- attributed quotes from BookNLP
  - traits (list[str]) -- traits extracted by langextract
  - goals (list[str]) -- goals extracted by langextract
  - backstory_markers (list[str]) -- optional, from langextract
outputs (JSON, must validate against narrative.schema.PseudoBig5):
  - openness (0-10)
  - conscientiousness (0-10)
  - extraversion (0-10)
  - agreeableness (0-10)
  - neuroticism (0-10)
  - rationale (str, brief) -- one-sentence summary of the evidence used
written_for: gpt-4o-class models with JSON mode, temperature=0
source:
  - Jacobs (2019) "Pseudo-Big 5" pole conventions.
  - Goldberg (1992); Thompson (2008) Big-Five Mini-Markers.
notes:
  - This is a FALLBACK only. The primary path is the SentiArt seed-word
    projection driven by configs/instruments/sentiart_big5_seeds.yaml.
  - Record provenance: set NarrativeFeatures.character.pseudo_big5_method[name] = "llm_fallback".
  - Pseudo-Big5 is not a validated personality measurement; it is a
    computational proxy that feeds reader-character similarity at
    read-time. See docs/09-reader-trait-schema.md.
-->

# Character pseudo-Big5 (LLM fallback, v0)

You are an expert literary analyst. Given a single character and the
evidence below, produce a five-dimensional **pseudo-Big5** profile on
0-10 scales using the OCEAN convention:

- **Openness to experience / Intellect** — imaginative, curious,
  reflective vs. conventional, incurious, shallow.
- **Conscientiousness** — organized, careful, reliable vs. careless,
  reckless, undependable.
- **Extraversion** — outgoing, energetic, assertive vs. reserved, shy,
  withdrawn.
- **Agreeableness** — warm, cooperative, compassionate vs. cold,
  hostile, unsympathetic.
- **Neuroticism / Emotional Instability** — anxious, moody, insecure
  vs. calm, stable, even-tempered. **High score = more neurotic.**

Use **only** the evidence below; do not infer from outside knowledge.

## Evidence

- **Character**: {{ character_name }}
- **Text id**: {{ text_id }}
- **Attributed quotes** (from BookNLP):
{% for q in quotes %}  - {{ q }}
{% endfor %}
- **Traits** (from langextract):
{% for t in traits %}  - {{ t }}
{% endfor %}
- **Goals** (from langextract):
{% for g in goals %}  - {{ g }}
{% endfor %}
- **Backstory markers** (from langextract):
{% for b in backstory_markers %}  - {{ b }}
{% endfor %}

## Output schema

Respond with a single JSON object validating against
`narrative.schema.PseudoBig5`:

```json
{
  "openness": 0.0,
  "conscientiousness": 0.0,
  "extraversion": 0.0,
  "agreeableness": 0.0,
  "neuroticism": 0.0,
  "rationale": "..."
}
```

Output only the JSON object. Do not include any commentary outside it.

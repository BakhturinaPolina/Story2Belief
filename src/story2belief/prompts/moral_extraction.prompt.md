<!--
prompt_id: moral_extraction.v1
purpose: >-
  Extract candidate moral propositions, behavioral lessons, and value
  judgments from a narrative, with source grounding via langextract.
  Replaces v0 (free-form staged prompt) with explicit extraction classes
  and few-shot ExampleData. Each extraction carries a char_interval into
  the source text so Layer 3 can compute justification-embedding
  similarity against the grounded supporting passage rather than the
  whole story.
inputs:
  - text (str): full story text, UTF-8
  - text_id (str)
outputs (list[langextract.data.Extraction], must validate against
  narrative.schema.MoralProposition / MoralLayer):
  - extraction_class = "moral_proposition"
    - extraction_text: verbatim span supporting the moral
    - attributes:
        proposition: str          # the moral, paraphrased succinctly
        foundations: {care_harm, fairness_cheating, loyalty_betrayal,
                      authority_subversion, sanctity_degradation} (each 0-10)
        confidence: 0-10
        ambiguity: 0-10
  - extraction_class = "behavioral_lesson"
    - extraction_text: verbatim span supporting the lesson
    - attributes:
        lesson: "if X, then Y" style paraphrase
  - extraction_class = "value_judgment"
    - extraction_text: verbatim span where a character/narrator endorses
      or condemns a value
    - attributes:
        valence: "endorse" | "condemn"
        target_value: str
  - extraction_class = "mft_evidence" (optional supporting evidence)
    - extraction_text: verbatim span
    - attributes:
        foundation: care_harm | fairness_cheating | loyalty_betrayal |
                    authority_subversion | sanctity_degradation
        polarity: "uphold" | "violate"
written_for:
  - langextract 1.x + gemini-2.5-flash (default) or gpt-4o (compare)
  - extraction_passes=3, max_char_buffer=1000, max_workers=10 for stories > 1k words
source:
  - Hobson et al. (2024) "Story morals: Surfacing value-driven narrative schemas..."
  - Haidt's Moral Foundations Theory (5 foundations).
  - See prompts/moral_extraction.examples.py for the few-shot ExampleData.
notes:
  - Examples can leak into outputs (langextract README warning).
    Always filter `[e for e in result.extractions if e.char_interval]`.
  - Set temperature=0 in the calling code; rely on langextract's
    controlled generation for JSON schema enforcement.
  - Re-prompt once if pydantic validation of the assembled
    MoralPropositions fails.
-->

# Moral-extraction prompt (v1, langextract few-shot)

You are an expert literary analyst trained in Moral Foundations Theory
(Haidt). Read the story below and extract:

1. **Moral propositions** — value-driven claims the story implies
   (e.g., *"loyalty matters more than truth"*). Allow MULTIPLE
   candidates per story; each gets its own grounded span.
2. **Behavioral lessons** — concrete *if-X-then-Y* prescriptions the
   story dramatizes (e.g., *"if you stray from the path, harm follows"*).
3. **Value judgments** — passages where a character or the narrator
   explicitly endorses or condemns a value.
4. **MFT evidence** (optional) — short spans that uphold or violate a
   specific moral foundation, useful for scoring `foundations` on the
   propositions.

For each extraction, **use the exact verbatim text** as `extraction_text`
(do NOT paraphrase). The paraphrase belongs in `attributes.proposition`,
`attributes.lesson`, etc.

Score each moral proposition's `foundations` independently (a story can
touch multiple foundations at once; the five scores need not sum to 1).

`confidence` reflects how confident you are this is *a* moral of the
story. `ambiguity` reflects how contested or open-to-interpretation
the moral is, given the story.

Order extractions in their order of appearance in the text.

The list of few-shot exemplars is stored in
`prompts/moral_extraction.examples.py` and is injected by the calling
code via `lx.extract(... examples=MORAL_EXTRACTION_EXAMPLES)`.

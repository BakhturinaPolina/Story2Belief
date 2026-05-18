<!--
prompt_id: narrative_features.v1
purpose: >-
  Extract event / discourse / story-world features from a short story
  with source grounding via langextract. Replaces v0 (free-form prompt)
  with explicit extraction classes and few-shot ExampleData. Outputs
  feed the discourse / story-world / character modules of Layer 1.
inputs:
  - text (str): full story text, UTF-8
  - text_id (str)
outputs (list[langextract.data.Extraction], must aggregate into fields on
  narrative.schema.NarrativeFeatures):
  - extraction_class = "scene"
    - extraction_text: verbatim opening sentence(s) of the scene
    - attributes:
        scene_index: int            # 0-based, in narrative order
        setting: str
        dominant_event_type: "action" | "dialogue" | "reflection" | "description"
  - extraction_class = "pov_marker"
    - extraction_text: verbatim phrase that disambiguates POV
    - attributes:
        pov_type: "first_person" | "close_third" | "omniscient" | "multi_perspective"
        evidence: brief gloss
  - extraction_class = "imagery_passage"
    - extraction_text: verbatim sensory-rich span
    - attributes:
        modality: "visual" | "auditory" | "tactile" | "olfactory" | "gustatory" | "kinesthetic"
        vividness: 0-10
  - extraction_class = "character_trait"
    - extraction_text: verbatim span attributing a trait
    - attributes:
        character_name: str
        trait: str                  # paraphrased trait label
  - extraction_class = "character_goal"
    - extraction_text: verbatim span expressing a goal
    - attributes:
        character_name: str
        goal: str
  - extraction_class = "setting_change"
    - extraction_text: verbatim span marking a change of place/time
    - attributes:
        prev_setting: str
        new_setting: str
  - extraction_class = "causal_link"
    - extraction_text: verbatim span where one event causes another
    - attributes:
        cause: str
        effect: str
        explicitness: "explicit" | "implicit"
written_for:
  - langextract 1.x + gemini-2.5-flash (default)
  - extraction_passes=2, max_char_buffer=1200 for stories <= 3k words
source:
  - See prompts/narrative_features.examples.py for the few-shot ExampleData.
  - Piper & Bagga (2024) annotation scheme for narrative discourse
    (dialogue / entities / tense / emotionality / conflict / eventfulness)
    provided reference few-shot patterns.
notes:
  - Examples can leak into outputs. Always filter
    `[e for e in result.extractions if e.char_interval]`.
  - The number of `scene` extractions is the eventfulness denominator;
    causal_link count contributes to event.causal_clarity.
  - When multiple POV markers conflict, take the modal pov_type
    weighted by pov_confidence (computed in the caller).
-->

# Narrative-features prompt (v1, langextract few-shot)

You are an expert literary analyst. Extract structured features from
the story text using the seven extraction classes above. For every
extraction, **use the verbatim text span** as `extraction_text`; put
labels and paraphrases in `attributes`.

Order extractions by appearance. Keep extractions concise — short
verbatim spans are preferred over long ones, except for `scene` openers
which may run up to two sentences.

If a feature is absent from the story, emit no extraction for that
class. Do not fabricate.

The list of few-shot exemplars is stored in
`prompts/narrative_features.examples.py` and is injected by the calling
code via `lx.extract(... examples=NARRATIVE_FEATURES_EXAMPLES)`.

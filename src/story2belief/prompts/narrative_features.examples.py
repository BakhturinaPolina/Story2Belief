"""Few-shot exemplars for the narrative-features prompt.

These are passed to ``langextract.extract(...)`` as ``examples``. See
``prompts/narrative_features.prompt.md`` for the prompt description and
schema.

Convention (per the langextract README):
    - Use **verbatim** spans from the example text for ``extraction_text``.
    - Order extractions by appearance.
    - Filter results in the caller with
      ``[e for e in result.extractions if e.char_interval]`` to drop
      ungrounded extractions that leak from these examples.
"""

from __future__ import annotations

try:
    import langextract as lx
except ImportError:  # pragma: no cover - langextract is an optional dep.
    lx = None  # type: ignore[assignment]


def _build_examples() -> list:
    """Return the narrative-features ExampleData list."""
    if lx is None:
        return []

    return [
        lx.data.ExampleData(
            text=(
                "I had not slept for two days when the letter arrived. "
                "The hallway smelled of damp paper and old coffee. "
                "Anna, my sister, wanted nothing more than to leave the city, "
                "but the news in the envelope would make that impossible. "
                "She tore it open in the kitchen. "
                "Because the bank had foreclosed, the house would be sold by Friday."
            ),
            extractions=[
                lx.data.Extraction(
                    extraction_class="pov_marker",
                    extraction_text="I had not slept for two days",
                    attributes={
                        "pov_type": "first_person",
                        "evidence": "first-person pronoun 'I' anchoring the narration",
                    },
                ),
                lx.data.Extraction(
                    extraction_class="scene",
                    extraction_text=(
                        "I had not slept for two days when the letter arrived."
                    ),
                    attributes={
                        "scene_index": 0,
                        "setting": "hallway of the narrator's home",
                        "dominant_event_type": "description",
                    },
                ),
                lx.data.Extraction(
                    extraction_class="imagery_passage",
                    extraction_text="The hallway smelled of damp paper and old coffee.",
                    attributes={
                        "modality": "olfactory",
                        "vividness": 7.0,
                    },
                ),
                lx.data.Extraction(
                    extraction_class="character_goal",
                    extraction_text="wanted nothing more than to leave the city",
                    attributes={
                        "character_name": "Anna",
                        "goal": "leave the city",
                    },
                ),
                lx.data.Extraction(
                    extraction_class="setting_change",
                    extraction_text="She tore it open in the kitchen.",
                    attributes={
                        "prev_setting": "hallway",
                        "new_setting": "kitchen",
                    },
                ),
                lx.data.Extraction(
                    extraction_class="causal_link",
                    extraction_text=(
                        "Because the bank had foreclosed, the house would be sold by Friday."
                    ),
                    attributes={
                        "cause": "the bank had foreclosed",
                        "effect": "the house would be sold by Friday",
                        "explicitness": "explicit",
                    },
                ),
            ],
        ),
        lx.data.ExampleData(
            text=(
                "Tom Sawyer was always restless. "
                "He scaled the fence and bolted toward the river, "
                "leaving Aunt Polly shouting after him."
            ),
            extractions=[
                lx.data.Extraction(
                    extraction_class="pov_marker",
                    extraction_text="Tom Sawyer was always restless.",
                    attributes={
                        "pov_type": "close_third",
                        "evidence": "third-person narration centered on Tom",
                    },
                ),
                lx.data.Extraction(
                    extraction_class="character_trait",
                    extraction_text="Tom Sawyer was always restless.",
                    attributes={
                        "character_name": "Tom Sawyer",
                        "trait": "restless",
                    },
                ),
                lx.data.Extraction(
                    extraction_class="scene",
                    extraction_text=(
                        "He scaled the fence and bolted toward the river, "
                        "leaving Aunt Polly shouting after him."
                    ),
                    attributes={
                        "scene_index": 0,
                        "setting": "yard near the fence, toward the river",
                        "dominant_event_type": "action",
                    },
                ),
            ],
        ),
    ]


#: Lazily-built ExampleData list. Empty if langextract is not installed.
NARRATIVE_FEATURES_EXAMPLES = _build_examples()

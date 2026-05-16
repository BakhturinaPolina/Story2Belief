"""Layer 1 orchestration: text -> NarrativeFeatures."""

from __future__ import annotations

from story2belief.narrative.schema import NarrativeFeatures


def run(text_id: str, text: str, *, language: str = "en") -> NarrativeFeatures:
    """Run the full narrative-analysis pipeline on a single text.

    Composes :func:`narrative.characters.extract_characters`,
    :func:`narrative.discourse.extract_event_layer`,
    :func:`narrative.story_world.extract_story_world`, and
    :func:`narrative.moral_extraction.extract_morals` into a single record.
    """
    raise NotImplementedError("narrative.pipeline.run is a stub.")

"""Character / coreference / POV extraction (BookNLP wrapper, placeholder)."""

from __future__ import annotations

from story2belief.narrative.schema import CharacterLayer


def extract_characters(text: str) -> CharacterLayer:
    """Return the character layer for a given text.

    Will wrap BookNLP for character clustering, quotation attribution, and
    coreference, plus an LLM prompt for POV / focalization classification.
    """
    raise NotImplementedError("characters.extract_characters is a stub.")

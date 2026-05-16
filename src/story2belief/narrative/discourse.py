"""Event-layer / discourse features.

Computed via an LLM prompt (``prompts/narrative_features.prompt.md``)
following Piper & Bagga (2024).
"""

from __future__ import annotations

from story2belief.narrative.schema import EventLayer


def extract_event_layer(text: str) -> EventLayer:
    """Return the event-layer features for the given narrative text."""
    raise NotImplementedError("discourse.extract_event_layer is a stub.")

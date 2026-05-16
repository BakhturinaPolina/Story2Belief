"""Adapted SWAS scoring for AI readers.

See ``docs/07-swas-adaptation.md`` for the rationale and field definitions.
"""

from __future__ import annotations

from story2belief.readers.profile import ReadingResponse, SwasResponse


def score_swas(reading_response_text: str) -> SwasResponse:
    """Parse an LLM JSON response into a :class:`SwasResponse`."""
    raise NotImplementedError("swas.score_swas is a stub.")


def attach_swas(response: ReadingResponse, swas: SwasResponse) -> ReadingResponse:
    """Return a copy of ``response`` with ``swas`` attached."""
    raise NotImplementedError("swas.attach_swas is a stub.")

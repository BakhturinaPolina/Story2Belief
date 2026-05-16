"""Moral-extraction pipeline (Hobson et al. style).

Implements the staged prompt sequence: summary -> protagonists -> tone ->
candidate morals -> behavioral lessons. Each stage is a separate prompt
with a versioned id, allowing later stages to inspect earlier ones.
"""

from __future__ import annotations

from story2belief.narrative.schema import MoralLayer


def extract_morals(text: str) -> MoralLayer:
    """Return one or more candidate moral propositions for a text.

    Allows multiple candidates with confidence + ambiguity, rather than
    forcing a single canonical moral.
    """
    raise NotImplementedError("moral_extraction.extract_morals is a stub.")

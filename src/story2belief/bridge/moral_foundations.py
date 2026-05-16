"""Moral-foundation scoring (MoralBERT wrapper, placeholder).

Maps a free-text utterance (story passage, agent justification, dilemma
option) onto a :class:`FoundationDistribution`.
"""

from __future__ import annotations

from story2belief.narrative.schema import FoundationDistribution


def score_foundations(text: str) -> FoundationDistribution:
    """Return a moral-foundations distribution for a text."""
    raise NotImplementedError("moral_foundations.score_foundations is a stub.")

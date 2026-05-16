"""Loaders for moral-dilemma corpora.

Supports MoralStory / STORAL (thu-coai), Moral Stories (demelin), and the
prompts/codebooks from Hobson et al. See ``docs/11-data-sources.md``.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from story2belief.narrative.schema import FoundationDistribution


@dataclass(frozen=True, slots=True)
class Dilemma:
    """A single moral-dilemma item."""

    dilemma_id: str
    text: str
    options: tuple[str, ...] = ()
    foundations: FoundationDistribution = field(default_factory=FoundationDistribution)
    source_corpus: str = ""


def load_dilemmas(corpus: str, root: Path | str) -> list[Dilemma]:
    """Load dilemma items from a named corpus directory."""
    raise NotImplementedError("dilemmas.load_dilemmas is a stub.")

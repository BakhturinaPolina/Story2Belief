"""Transfer-delta computation: pre/post -> change."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class DilemmaResponse:
    """An agent's response to a single dilemma at one point in time."""

    reader_id: str
    dilemma_id: str
    chosen_option: str
    confidence: float
    justification: str


@dataclass(frozen=True, slots=True)
class TransferDeltas:
    """Pre/post deltas for one (reader, story, dilemma) triple."""

    reader_id: str
    text_id: str
    dilemma_id: str
    delta_choice: bool
    delta_confidence: float
    justification_similarity: float


def compute_deltas(
    pre: DilemmaResponse, post: DilemmaResponse, *, story_moral: str, text_id: str
) -> TransferDeltas:
    """Compute :class:`TransferDeltas` from pre/post responses + story moral."""
    raise NotImplementedError("transfer.compute_deltas is a stub.")

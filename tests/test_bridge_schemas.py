"""Schema-shape tests for the bridge layer."""

from __future__ import annotations

from story2belief.bridge.dilemmas import Dilemma
from story2belief.bridge.transfer import DilemmaResponse, TransferDeltas


def test_dilemma_default_construction() -> None:
    d = Dilemma(dilemma_id="d0001", text="Should you keep the promise?")
    assert d.options == ()
    assert d.source_corpus == ""


def test_transfer_deltas_construction() -> None:
    deltas = TransferDeltas(
        reader_id="r0001",
        text_id="demo",
        dilemma_id="d0001",
        delta_choice=False,
        delta_confidence=0.0,
        justification_similarity=0.0,
    )
    assert deltas.reader_id == "r0001"


def test_dilemma_response_construction() -> None:
    r = DilemmaResponse(
        reader_id="r0001",
        dilemma_id="d0001",
        chosen_option="A",
        confidence=5.0,
        justification="placeholder",
    )
    assert 0.0 <= r.confidence <= 10.0

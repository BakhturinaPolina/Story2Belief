"""Schema-shape tests for the reader layer."""

from __future__ import annotations

from story2belief.readers.profile import ReaderProfile, ReadingResponse, SwasResponse


def test_reader_profile_has_default_traits() -> None:
    p = ReaderProfile(reader_id="r0001")
    assert 0.0 <= p.transportability <= 10.0
    assert 0.0 <= p.empathy <= 10.0
    assert 0.0 <= p.source_memory_decay <= 1.0


def test_reading_response_attaches_swas() -> None:
    resp = ReadingResponse(
        reader_id="r0001",
        text_id="demo",
        interpretation="placeholder",
        swas=SwasResponse(),
        verbalized_moral="",
    )
    assert isinstance(resp.swas, SwasResponse)

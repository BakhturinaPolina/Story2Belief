"""Smoke test: package imports and version is set."""

from __future__ import annotations


def test_import_package() -> None:
    import story2belief

    assert hasattr(story2belief, "__version__")
    assert isinstance(story2belief.__version__, str)

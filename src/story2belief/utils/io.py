"""I/O helpers: JSON read/write with provenance metadata."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def write_json(path: Path | str, data: Any, *, meta: dict[str, Any] | None = None) -> None:
    """Write ``data`` as JSON. If ``meta`` is given, also write a sibling
    ``<path>.meta.json`` with reproducibility metadata.
    """
    raise NotImplementedError("utils.io.write_json is a stub.")


def read_json(path: Path | str) -> Any:
    """Read a JSON file."""
    raise NotImplementedError("utils.io.read_json is a stub.")

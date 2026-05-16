"""Logging configuration helpers.

Use ``get_logger(__name__)`` instead of ``logging.getLogger(__name__)`` so
that all modules share a consistent format and respect ``S2B_LOG_LEVEL``.
"""

from __future__ import annotations

import logging
import os


def get_logger(name: str) -> logging.Logger:
    """Return a configured logger for ``name``."""
    level_name = os.environ.get("S2B_LOG_LEVEL", "INFO").upper()
    level = getattr(logging, level_name, logging.INFO)
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter("%(asctime)s %(levelname)s %(name)s | %(message)s")
        )
        logger.addHandler(handler)
        logger.setLevel(level)
        logger.propagate = False
    return logger

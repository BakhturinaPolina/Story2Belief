"""Seed helpers for reproducible cohort sampling and LLM-based runs."""

from __future__ import annotations

import os
import random


def seed_all(seed: int) -> None:
    """Seed ``random`` and any other RNGs the project relies on.

    Note: LLM nondeterminism is suppressed via ``temperature=0`` in calling
    code, not via a seed here.
    """
    random.seed(seed)
    os.environ["PYTHONHASHSEED"] = str(seed)

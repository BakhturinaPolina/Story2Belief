"""Project-wide configuration loaded from environment + YAML.

This module centralizes filesystem paths, model identifiers, and run
metadata so that no other module hardcodes them. It is intentionally a
stub: real loading logic is added when the first pipeline runs.
"""

from __future__ import annotations

from pathlib import Path

REPO_ROOT: Path = Path(__file__).resolve().parents[2]
DATA_DIR: Path = REPO_ROOT / "data"
RESULTS_DIR: Path = REPO_ROOT / "results"
CONFIGS_DIR: Path = REPO_ROOT / "configs"


def load_config(name: str = "default") -> dict:
    """Load a YAML config file from ``configs/`` by name (without extension).

    Parameters
    ----------
    name : str
        Stem of the YAML file under ``configs/`` (e.g. ``"prototype"``).

    Returns
    -------
    dict
        Parsed config dictionary. Empty ``{}`` placeholder until implemented.
    """
    raise NotImplementedError("load_config is a stub; wire up YAML loading.")

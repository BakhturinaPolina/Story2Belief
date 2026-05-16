"""Run pre/post moral-dilemma assessment for the configured cohort.

Usage::

    uv run python scripts/run_dilemma_assessment.py --config configs/prototype.yaml
"""

from __future__ import annotations

import argparse
from pathlib import Path

from story2belief.utils.logging import get_logger

logger = get_logger(__name__)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, default=Path("configs/prototype.yaml"))
    args = parser.parse_args()
    logger.info("[stub] would run dilemma assessment with config=%s", args.config)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

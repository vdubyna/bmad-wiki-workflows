#!/usr/bin/env python3
"""Compatibility placeholder for future Wiki Workflows cleanup.

BMAD multi-skill setup skills often include a cleanup step for obsolete
installer-owned directories. This module has no safe legacy cleanup to perform
yet, so the script is intentionally non-destructive.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", required=True)
    args = parser.parse_args()

    project_root = Path(args.project_root).expanduser().resolve()
    if not (project_root / "_bmad").exists():
        print(f"BMAD directory not found in {project_root}; legacy cleanup skipped.")
        return 0
    print("No legacy Wiki Workflows directories require cleanup; cleanup skipped.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

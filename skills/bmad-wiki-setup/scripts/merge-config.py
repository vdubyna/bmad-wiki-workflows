#!/usr/bin/env python3
"""Check module config for the Wiki Workflows setup skill.

The module intentionally ships without shared configuration variables for now.
This script keeps the multi-skill setup surface stable and can grow a real
config merge later without changing setup instructions.
"""

from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", required=True)
    parser.add_argument("--module-yaml", required=True)
    args = parser.parse_args()

    project_root = Path(args.project_root).expanduser().resolve()
    module_yaml = Path(args.module_yaml).expanduser().resolve()
    if not (project_root / "_bmad").exists():
        print(f"BMAD directory not found in {project_root}; config merge skipped.")
        return 0
    if not module_yaml.exists():
        print(f"Module yaml not found at {module_yaml}; config merge skipped.")
        return 0
    print("No shared module configuration values are required; config merge skipped.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

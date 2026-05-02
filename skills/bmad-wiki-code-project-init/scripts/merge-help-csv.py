#!/usr/bin/env python3
"""Merge this module's help rows into a BMAD help CSV.

The script uses an anti-zombie merge: rows for the same module are removed before
new rows are appended.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


HEADER = [
    "module",
    "skill",
    "display-name",
    "menu-code",
    "description",
    "action",
    "args",
    "phase",
    "after",
    "before",
    "required",
    "output-location",
    "outputs",
]


def read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_rows(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=HEADER)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in HEADER})


def target_help_path(project_root: Path) -> Path:
    current = project_root / "_bmad" / "_config" / "bmad-help.csv"
    if current.exists():
        return current
    return project_root / "_bmad" / "module-help.csv"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-root", required=True)
    parser.add_argument("--module-help", required=True)
    args = parser.parse_args()

    project_root = Path(args.project_root).expanduser().resolve()
    module_help = Path(args.module_help).expanduser().resolve()
    target = target_help_path(project_root)

    new_rows = read_rows(module_help)
    module_names = {row["module"] for row in new_rows if row.get("module")}
    existing_rows = read_rows(target)
    kept_rows = [row for row in existing_rows if row.get("module") not in module_names]
    write_rows(target, kept_rows + new_rows)

    print(f"Merged {len(new_rows)} help row(s) into {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

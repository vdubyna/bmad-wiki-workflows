---
name: bmad-wiki-setup
description: Register Wiki Workflows module. Use when setting up bmad-wiki workflows, registering BMAD help entries, configuring Wiki Workflows, or refreshing installed module metadata.
---

# BMAD Wiki Setup

Goal: register the multi-skill Wiki Workflows module with BMAD help/config surfaces.

This is the module setup skill. It does not scan sources, initialize wiki content, or run any wiki
workflow. It only registers the module-level metadata that lets `bmad-help` discover and recommend
the installed workflows.

## Safety Rules

- Do not modify wiki content.
- Do not scan target projects or external sources.
- Do not commit changes without explicit user approval.
- If `_bmad/` is not present in the current project root, explain that BMAD is not installed here and
  skip registration.

## Setup Workflow

1. Resolve `{project-root}` as the current project root.
2. Resolve `{skill-root}` as the folder containing this `SKILL.md`.
3. Read `assets/module.yaml` and `assets/module-help.csv` for module identity and help entries.
4. If `{project-root}/_bmad/` does not exist, stop after explaining that registration was skipped.
5. Run:

   ```sh
   python3 {skill-root}/scripts/merge-help-csv.py --project-root {project-root} --module-help {skill-root}/assets/module-help.csv
   ```

6. Run:

   ```sh
   python3 {skill-root}/scripts/merge-config.py --project-root {project-root} --module-yaml {skill-root}/assets/module.yaml
   ```

7. Run:

   ```sh
   python3 {skill-root}/scripts/cleanup-legacy.py --project-root {project-root}
   ```

8. Summarize registration results and next available workflows.

## Output Contract

The minimum successful output is:

- Wiki Workflows help rows merged into `_bmad/module-help.csv` or `_bmad/_config/bmad-help.csv`;
- module config merge checked;
- no wiki content changed.

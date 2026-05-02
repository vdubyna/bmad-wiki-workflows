---
name: bmad-wiki-maintenance
description: Maintain wiki source registrations. Use when the user wants to scan for new sources, find unregistered files, refresh source status, prepare source registrations, or keep a wiki current over time.
---

# BMAD Wiki Maintenance

Goal: keep an evidence-first Obsidian/LLM wiki current by finding new or changed sources and routing
them into source registration.

This workflow is maintenance-oriented. It scans bounded locations, compares candidates against
existing source summaries/log entries, and prepares registration work. It should stay conservative:
inventory first, register only clear candidates, and ask before broad or external scans.

## Safety Rules

- Do not run unbounded filesystem scans.
- Do not access external URLs, connected apps, or private systems unless explicitly approved.
- Do not read secrets, credentials, private keys, runtime caches, dependency folders, dumps, or large
  binary archives.
- Do not rewrite raw evidence.
- Do not mark stale sources as superseded or archived without human approval.

## Workflow

1. Read and follow `prompts/01-maintenance-scope.md`.
2. Read and follow `prompts/02-inventory-current-wiki.md`.
3. Read and follow `prompts/03-scan-candidates.md`.
4. Read and follow `prompts/04-triage-and-register.md`.
5. Read and follow `prompts/05-maintenance-report.md`.

Use the templates in `resources/` when creating maintenance candidate records.

## Output Contract

The minimum successful output is:

- maintenance candidate record in `raw/inbox/YYYY-MM-DD-maintenance-source-candidates.md`;
- updated `wiki/log.md`;
- source-registration handoff list;
- source summaries created or updated only for clearly approved candidates.

If scan roots or maintenance purpose are missing, ask for them before scanning.

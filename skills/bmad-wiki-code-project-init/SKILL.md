---
name: bmad-wiki-code-project-init
description: Initialize a code repository wiki from source evidence. Use when the user wants to create or update an Obsidian/LLM wiki for a codebase, run wiki-code-project-init, register a target code repo, create raw packets/source summaries/project profiles, or plan deep scans from code.
---

# BMAD Wiki Code Project Init

Goal: initialize or update an evidence-first Obsidian/LLM wiki for a target code repository.

This is a complex workflow. Keep this file as the routing layer and load stage prompts only when
needed.

## Safety Rules

- Work read-only against the target code repo unless the user explicitly asks for code changes.
- Do not read secrets, private keys, runtime caches, dependency folders, build output, or large dumps.
- Do not mutate installer-owned BMAD files directly.
- Do not commit changes without explicit user approval.
- Keep raw evidence, source summaries, concepts, decisions, experiments, and logs as separate pages.
- Mark source authority clearly: `current behavior`, `planned direction`, `generated dirty context`,
  or `external/raw context`.

## Setup And Help Registration

If the user invokes this skill with `setup`, `configure`, `registration`, or asks to register it with
BMAD help, read and follow `assets/module-setup.md`, then stop unless they also asked to run the
workflow.

If setup cannot run because `_bmad/` is not present, continue with the workflow and mention that help
registration was skipped.

## Workflow

1. Read and follow `prompts/01-intake-and-scope.md`.
2. Read and follow `prompts/02-scaffold-wiki.md`.
3. Read and follow `prompts/03-quick-scan.md`.
4. Read and follow `prompts/04-compile-initial-wiki.md`.
5. Read and follow `prompts/05-review-and-next-scan.md`.

Use `resources/scan-scope-presets.md` when inferring scan scope. Use the templates in `resources/`
when creating missing wiki infrastructure or first wiki pages.

## Output Contract

The minimum successful output is:

- raw init packet in `raw/project/YYYY-MM-DD-<project-slug>-repo-initial-scan.md`;
- source summary in `wiki/sources/YYYY-MM-DD-<project-slug>-repo-initial-scan.md`;
- project profile in `wiki/concepts/<project-slug>-project-profile.md`;
- updated `wiki/index.md`;
- updated `wiki/log.md`;
- proposed deep scan plan.

When the user says "сам розберися" or "figure it out", use conservative read-only defaults, record
assumptions in the raw packet, and continue.

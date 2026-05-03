---
name: bmad-wiki-project-init
description: Initialize docs-oriented wiki projects. Use when the user wants to create or update an Obsidian/LLM wiki for a general documentation-oriented project, register foundational docs, create a project profile, or seed a source backlog.
---

# BMAD Wiki Project Init

Goal: initialize or update an evidence-first Obsidian/LLM wiki for a general docs-oriented project.

This scaffold is for non-code-first projects: product docs, operating docs, research docs,
knowledge-base projects, strategy packs, or mixed source folders where code is not the primary
source of truth.

## Safety Rules

- Work read-only against supplied source locations unless the user explicitly asks for changes.
- Do not read secrets, private notes, credentials, runtime caches, dependency folders, dumps, or
  large binary archives.
- Do not infer a source location from sibling folders, git remotes, or project names.
- Keep raw evidence, source summaries, concepts, decisions, experiments, and logs as separate pages.
- Mark source authority clearly: `canonical project docs`, `working notes`, `external/raw context`,
  `generated context`, `compiled synthesis`, or `human-reviewed decision`.

## Workflow

1. Read and follow `prompts/01-intake-and-project-shape.md`.
2. Read and follow `prompts/02-scaffold-docs-wiki.md`.
3. Read and follow `prompts/03-register-foundational-docs.md`.
4. Read and follow `prompts/04-compile-project-index.md`.
5. Read and follow `prompts/05-review-and-source-backlog.md`.

Use the templates in `resources/` when creating missing wiki infrastructure or first wiki pages.

## Output Contract

The minimum successful output is:

- raw project intake in `raw/project/YYYY-MM-DD-<project-slug>-docs-project-intake.md`;
- foundational source summary in `wiki/sources/YYYY-MM-DD-<project-slug>-foundational-docs.md`;
- project profile in `wiki/concepts/<project-slug>-project-profile.md`;
- updated `wiki/index.md`;
- updated `wiki/log.md`;
- proposed source backlog for follow-up registration.

If the project identity, source locations, or privacy boundaries are missing, ask for those details
instead of guessing.

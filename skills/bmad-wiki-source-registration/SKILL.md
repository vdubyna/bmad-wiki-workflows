---
name: bmad-wiki-source-registration
description: Register wiki sources by type. Use when the user wants to add a source to the wiki, classify a source, capture source metadata, create a raw source record, or create/update a wiki source summary.
---

# BMAD Wiki Source Registration

Goal: register sources of different types in an evidence-first Obsidian/LLM wiki.

This workflow turns a supplied source into a traceable wiki source record. It is intentionally narrow:
capture metadata, classify authority, create raw evidence when appropriate, create or update a source
summary, and update index/log surfaces.

## Safety Rules

- Do not access private systems, external URLs, or connected apps unless the user explicitly supplied
  the source and approved access.
- Do not read secrets, credentials, private keys, runtime caches, dependency folders, dumps, or large
  binary archives.
- Do not edit raw evidence after creation. Add a new raw record for corrections.
- Do not treat generated notes, transcripts, or AI output as canonical without a lower-authority
  marker.
- Do not register a source if ownership, permission, or privacy boundaries are unclear.

## Source Types

Use this starter taxonomy and refine it later as the module grows:

- `local-file`;
- `local-directory`;
- `git-repository`;
- `web-url`;
- `document-export`;
- `dataset`;
- `media-asset`;
- `transcript-or-notes`;
- `external-reference`.

## Workflow

1. Read and follow `prompts/01-source-intake.md`.
2. Read and follow `prompts/02-inspect-and-capture.md`.
3. Read and follow `prompts/03-classify-source.md`.
4. Read and follow `prompts/04-write-registration.md`.
5. Read and follow `prompts/05-review-and-handoff.md`.

Use the templates in `resources/` when creating raw source records or source summaries.

## Output Contract

The minimum successful output is:

- raw source record in `raw/inbox/YYYY-MM-DD-<source-slug>-source-registration.md`;
- source summary in `wiki/sources/YYYY-MM-DD-<source-slug>.md`;
- updated `wiki/index.md` or source registry section if present;
- updated `wiki/log.md`;
- unresolved questions or follow-up registration tasks.

If the source location, type, access permission, or intended wiki use is missing, ask for those
details before inspecting the source.

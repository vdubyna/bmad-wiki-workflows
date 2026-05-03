---
type: schema
status: draft
topic: wiki-schema
tags:
  - wiki
  - schema
sources: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# Wiki Schema

## Page Types

- `index`
- `log`
- `schema`
- `target-repo`
- `concept`
- `source-summary`
- `project-profile`
- `experiment`
- `benchmark-report`
- `decision`
- `workflow`
- `glossary`

## Status Values

- `draft`
- `review`
- `approved`
- `stale`
- `archived`

## Required Frontmatter

```yaml
---
type: concept
status: draft
topic:
tags: []
sources: []
target_id:
verified_commit:
needs-refresh: false
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

## Evidence Rules

- Keep target repo code outside the wiki repo.
- Keep raw scan packets, source registration records, metadata, excerpts, and benchmark outputs in
  `raw/`.
- Keep compiled wiki pages in `wiki/`.
- Use `[[wikilinks]]` between related pages.
- Mark authority:
  - code/tests/manifests: current behavior;
  - official docs/README: canonical project docs;
  - AI research/deep research: generated context;
  - wiki pages: compiled synthesis, not source of truth;
  - decisions: valid only after human review.
- Do not mix source summary, concept note, decision record, and experiment note in one file.

## Traceability Rules

- Code-derived claims should trace through:
  `claim -> source summary -> raw scan packet -> repo commit + file path + symbol/line range`.
- Use line ranges only when they were inspected. Otherwise cite path, symbol, or section.
- Pages that depend on code should include `target_id`, `verified_commit`, and `depends_on_paths`
  when useful.

## Stale Detection Rules

- Compare the target registration `last_scanned_commit` with the current target repo commit.
- List changed files between those commits.
- If a changed file appears in a page dependency or source summary trace, mark the page
  `status: stale` or `needs-refresh: true`.
- Do not rewrite stale pages automatically without human review.

## Retrieval-First Rule For Coding Answers

1. Use `wiki/index.md` for navigation.
2. Use source summaries for context.
3. Verify against the registered target repo code.
4. Label statements as fact, inference, or hypothesis.

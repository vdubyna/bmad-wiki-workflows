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
- `concept`
- `source-summary`
- `project-profile`
- `experiment`
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
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

## Evidence Rules

- Keep raw source capture and intake in `raw/`.
- Keep compiled wiki pages in `wiki/`.
- Use `[[wikilinks]]` between related pages.
- Mark authority: canonical project docs, working notes, external/raw context, generated context,
  compiled synthesis, or human-reviewed decision.
- Wiki pages are compiled synthesis, not source of truth.
- Decision records are valid only after human review.
- Do not mix source summary, concept note, decision record, and experiment note in one file.

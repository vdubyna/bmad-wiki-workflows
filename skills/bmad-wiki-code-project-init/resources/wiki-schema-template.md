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

- Keep raw sources in `raw/`.
- Keep compiled wiki pages in `wiki/`.
- Use `[[wikilinks]]` between related pages.
- Mark authority: current behavior, planned direction, generated dirty context, or external/raw
  context.
- Do not mix source summary, concept note, decision record, and experiment note in one file.

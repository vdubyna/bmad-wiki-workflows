# Stage 4: Write Registration

Create or update the wiki artifacts for the source.

## Raw Source Record

Create:

```text
raw/inbox/YYYY-MM-DD-<source-slug>-source-registration.md
```

Use `resources/raw-source-registration-template.md`.

Include:

- source identity;
- locator;
- source type;
- authority layer;
- status;
- inspection method;
- target repo commit/path/symbol/line range for code-derived sources when available;
- privacy exclusions;
- evidence summary;
- unresolved questions.

## Source Summary

Create or update:

```text
wiki/sources/YYYY-MM-DD-<source-slug>.md
```

Use `resources/source-summary-template.md`.

Include:

- what the source is;
- what it is authoritative for;
- what it should not be used for;
- key claims or facts;
- evidence chain for each code-derived claim when available;
- links to related concepts, decisions, experiments, or project profiles;
- raw record link.

## Index And Log

- Update `wiki/index.md` or an existing source registry section if present.
- Append a `wiki/log.md` entry.

## Continue When

The source is traceable from wiki summary back to raw record and original locator.

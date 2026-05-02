# Stage 4: Compile Project Index

Convert intake evidence into the initial docs-oriented wiki artifacts.

## Raw Intake

Create:

```text
raw/project/YYYY-MM-DD-<project-slug>-docs-project-intake.md
```

Include:

- project identity;
- supplied source locations;
- scan purpose;
- include/exclude boundaries;
- authority layers;
- assumptions;
- unresolved questions;
- foundational source candidates.

## Source Summary

Create:

```text
wiki/sources/YYYY-MM-DD-<project-slug>-foundational-docs.md
```

Summarize the first canonical source bundle and list follow-up source candidates.

## Project Profile

Create or update:

```text
wiki/concepts/<project-slug>-project-profile.md
```

Keep status as `draft` unless the user explicitly approves.

## Index And Log

- Update `wiki/index.md` with the source summary and project profile.
- Append a `wiki/log.md` entry.

## Continue When

The wiki has a reviewable project profile and a concrete source backlog.

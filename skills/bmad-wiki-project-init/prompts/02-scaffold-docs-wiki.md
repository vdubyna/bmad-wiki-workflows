# Stage 2: Scaffold Docs Wiki

Create or verify wiki infrastructure in the current project root.

## Required Structure

```text
raw/
  inbox/
  project/
  datasets/
  assets/

wiki/
  concepts/
  sources/
  experiments/
  decisions/
  index.md
  log.md
  schema.md

docs/
  templates/
  workflows/
```

## Rules

- Do not overwrite existing files without explicit confirmation.
- If `wiki/schema.md`, `wiki/index.md`, or `wiki/log.md` already exist, read them and adapt.
- Create missing directories with `.gitkeep`.
- Add `.obsidian/`, runtime caches, and editor noise to `.gitignore` when appropriate.
- Never edit `raw/` files after creation. Add a new raw file for corrections.

## Continue When

The wiki can store raw intake, source summaries, project profile, index updates, and log entries.

# Stage 2: Scaffold Wiki

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
- If missing, create them from:
  - `resources/wiki-schema-template.md`;
  - `resources/wiki-index-template.md`;
  - `resources/wiki-log-template.md`.
- Create missing directories with `.gitkeep`.
- Add `.obsidian/`, runtime caches, and editor noise to `.gitignore` when appropriate.
- Never edit `raw/` files after creation. Add a new raw file for corrections.

## Continue When

The wiki has enough structure to store:

- raw packet;
- source summary;
- project profile;
- index/log updates.

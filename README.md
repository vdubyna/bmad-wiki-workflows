# BMAD Wiki Code Project Init

BMAD custom workflow skill for initializing an Obsidian/LLM wiki from a code repository.

The workflow creates or updates:

- `raw/project/*` raw evidence packets;
- `wiki/sources/*` source summaries;
- `wiki/concepts/*` project profiles and concept pages;
- `wiki/experiments/*` experiment plans when useful;
- `wiki/decisions/*` decision records when useful;
- `wiki/index.md` and `wiki/log.md`.

It is designed for evidence-first wiki maintenance: code, tests, canonical docs, planning artifacts,
generated artifacts, and external research are kept in separate authority layers.

## Install From Local Path

From a target wiki repo:

```sh
npx bmad-method install --directory . --custom-source /absolute/path/to/bmad-wiki-code-project-init --tools codex --yes
```

Or run the interactive installer:

```sh
npx bmad-method install
```

When prompted for a custom source, provide the path or Git URL for this repository.

## Install After Publishing

```sh
npx bmad-method install --directory . --custom-source https://github.com/vdubyna/bmad-wiki-code-project-init --tools codex --yes
```

If your BMAD setup uses another tool integration, replace `codex` with the tool option you use.

## Invoke

In the target wiki repo:

```text
Run bmad-wiki-code-project-init for target repo: /path/to/code
```

For first-run help registration:

```text
Run bmad-wiki-code-project-init setup
```

## Module Shape

This repository uses the standalone single-skill module pattern:

```text
.claude-plugin/marketplace.json
module.yaml
skills/bmad-wiki-code-project-init/SKILL.md
skills/bmad-wiki-code-project-init/prompts/
skills/bmad-wiki-code-project-init/resources/
skills/bmad-wiki-code-project-init/assets/
skills/bmad-wiki-code-project-init/scripts/
```

## Release Checklist

- Update `.claude-plugin/marketplace.json` version.
- Tag the release with the same semantic version.
- Run BMAD Builder Validate Module if available.
- Test local install through `--custom-source /path/to/repo`.
- Update repository URLs in `marketplace.json` if the GitHub location changes.

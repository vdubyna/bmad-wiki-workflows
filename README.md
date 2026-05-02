# BMAD Wiki Workflows

BMAD custom workflow module for initializing and maintaining evidence-first Obsidian/LLM wikis.

The module currently contains these workflows:

- `bmad-wiki-code-project-init`: initialize a wiki from an explicitly supplied code repository;
- `bmad-wiki-project-init`: initialize a general docs-oriented project wiki;
- `bmad-wiki-source-registration`: register sources of different types in the wiki;
- `bmad-wiki-maintenance`: scan for new or changed sources and register them through the wiki flow;
- `bmad-wiki-setup`: register the multi-skill module with BMAD help/config surfaces.

The workflows create or update:

- `raw/project/*` raw evidence packets;
- `raw/inbox/*` captured source-registration and maintenance evidence;
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
npx bmad-method install --directory . --custom-source /absolute/path/to/bmad-wiki-workflows --tools codex --yes
```

Or run the interactive installer:

```sh
npx bmad-method install
```

When prompted for a custom source, provide the path or Git URL for this repository.

## Install After Publishing

```sh
npx bmad-method install --directory . --custom-source https://github.com/vdubyna/bmad-wiki-workflows --tools codex --yes
```

If your BMAD setup uses another tool integration, replace `codex` with the tool option you use.

## Invoke

In the target wiki repo:

```text
Run bmad-wiki-setup
```

Then run the workflow you need:

```text
Run bmad-wiki-code-project-init for target repo: /path/to/code
Run bmad-wiki-project-init for project docs: /path/to/docs
Run bmad-wiki-source-registration for source: /path/or/url
Run bmad-wiki-maintenance for inbox/source scan
```

The code project workflow must receive an explicit target repo path or URL. It should not guess the
code repo from the current directory, sibling folders, wiki repo name, or git remotes. If the target
is missing, it should ask for the repo location and minimum project context before scanning.

## Module Shape

This repository uses the BMAD multi-skill module pattern:

```text
.claude-plugin/marketplace.json
module.yaml
skills/bmad-wiki-setup/
  SKILL.md
  assets/module.yaml
  assets/module-help.csv
  scripts/
skills/bmad-wiki-code-project-init/SKILL.md
skills/bmad-wiki-code-project-init/prompts/
skills/bmad-wiki-code-project-init/resources/
skills/bmad-wiki-project-init/SKILL.md
skills/bmad-wiki-project-init/prompts/
skills/bmad-wiki-source-registration/SKILL.md
skills/bmad-wiki-source-registration/prompts/
skills/bmad-wiki-maintenance/SKILL.md
skills/bmad-wiki-maintenance/prompts/
```

## Release Checklist

- Update `.claude-plugin/marketplace.json` version.
- Update `module.yaml` and `skills/bmad-wiki-setup/assets/module.yaml` version.
- Tag the release with the same semantic version.
- Run BMAD Builder Validate Module if available.
- Test local install through `--custom-source /path/to/repo`.
- Update repository URLs in `marketplace.json` if the GitHub location changes.

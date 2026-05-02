# Stage 3: Quick Scan

Run a read-only quick scan of the verified target code repo.

Do not start this stage until Stage 1 has verified a user-supplied or explicitly saved target repo
path/URL. If verification is missing or inconclusive, return to Stage 1 and ask for the missing
repo location or project context.

## Read-Only Commands

Use these when available:

- `git status --short`;
- `git rev-parse --abbrev-ref HEAD`;
- `git rev-parse HEAD`;
- `git remote -v`;
- `rg --files`.

If the target is not a Git repo, record that fact and continue with filesystem inventory.

## Scan Scope

Use `resources/scan-scope-presets.md` to choose starter include/exclude rules.

Quick scan is not a deep source reading pass. It should:

- inventory matching paths;
- read canonical docs;
- read package/config manifests;
- read small source entry points only when needed;
- inventory tests and major source folders;
- inventory planning/generated artifacts with lower authority markers.

## Authority Layers

- `current behavior`: current code, tests, canonical docs, package/config manifests.
- `planned direction`: PRD, roadmap, architecture plan, BMAD planning artifacts.
- `generated dirty context`: generated implementation artifacts, dirty generated files.
- `external/raw context`: transcripts, copied research notes, external sources.

## Continue When

You can summarize:

- target repo identity and commit/worktree state;
- canonical docs found;
- package/config manifests found;
- high-level source tree shape;
- test/benchmark surfaces;
- planning/generated artifacts;
- scan boundaries and assumptions.

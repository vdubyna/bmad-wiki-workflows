# Stage 3: Quick Scan

Run a read-only quick scan of the verified and registered target code repo.

Do not start this stage until Stage 1 has verified a user-supplied or explicitly saved target repo
path/URL. If verification is missing or inconclusive, return to Stage 1 and ask for the missing
repo location or project context.

Do not scan until a target registration contract is ready. If `wiki/targets/<target_id>.md` already
exists, read it and compare its last scanned commit/scope/exclusions against the current target
state before scanning.

## Read-Only Commands

Use these when available:

- `git status --short`;
- `git rev-parse --abbrev-ref HEAD`;
- `git rev-parse HEAD`;
- `git remote -v`;
- `rg --files`.
- changed-file comparison when a previous scanned commit exists:
  `git diff --name-only <last-scanned-commit>..HEAD`.

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

- `current behavior`: current code, tests, package/config manifests.
- `canonical project docs`: official docs, README, changelog, contributing docs.
- `planned direction`: PRD, roadmap, architecture plan, BMAD planning artifacts.
- `generated context`: AI research, deep research, generated implementation artifacts, dirty
  generated files.
- `compiled synthesis`: wiki pages compiled from evidence; never source of truth.
- `human-reviewed decision`: decision records only after explicit human review.

## Snapshot Packet Requirements

The scan must produce raw packet material, not only a narrative summary. Capture:

- target registration identity;
- commit, branch, remote, worktree state, and dirty-change policy;
- scan scope and exclusions;
- commands used;
- files inspected;
- skipped files or folders and reasons;
- findings;
- unresolved questions;
- changed files since the last scanned commit when available.

Do not copy the whole codebase into `raw/`. Store metadata, bounded excerpts, command output, and
benchmark output only.

## Continue When

You can summarize:

- target repo identity and commit/worktree state;
- target registration status;
- changed files since last scan, if any;
- canonical docs found;
- package/config manifests found;
- high-level source tree shape;
- test/benchmark surfaces;
- planning/generated artifacts;
- scan boundaries and assumptions.

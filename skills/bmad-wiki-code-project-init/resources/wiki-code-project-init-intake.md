# Wiki Code Project Init Intake

Use this as an optional intake template. The user does not need to fill every field, but the target
repo location must be explicit before scanning.

Do not guess the repo location from the wiki repo, current working directory, sibling folders,
recent context, or git remotes. If the location is missing, ask for it and any minimum project
context needed to verify the scan target.

## Minimum Useful Intake

- Target ID:
- Project name:
- Short project description:
- Local repo path or remote URL:
- Remote URL:
- Can read-only commands run in the target repo?
- Branch/tag/commit to document:
- Dirty changes: `ignore`, `include`, or `unknown`:
- Purpose: onboarding, architecture, search/retrieval, benchmark, audit, migration, debugging:
- Must include:
- Must exclude:
- Expected stack:
- First useful output:

## Defaults

- Scan mode: quick scan.
- Target repo: no default; requires a user-supplied or explicitly saved path/URL.
- Target registration: required before scan/ingest.
- Dirty changes: ignore unless explicitly included.
- Include: README/docs/manifests/config/source/tests inventory.
- Exclude: secrets, dependencies, caches, build output, binaries, dumps.
- Output: raw packet, source summary, project profile, deep scan plan.

## Verification Before Scan

- Local path exists and is readable:
- Target is Git repo, non-Git directory, or remote URL:
- Branch/commit/remotes/status captured when Git is available:
- Confirmed target is not the wiki repo unless self-documentation was requested:
- Visible evidence found: docs, manifests, configs, source folders, tests:
- Target registration path:
- Last scanned commit, if already registered:
- Missing information to ask the user:

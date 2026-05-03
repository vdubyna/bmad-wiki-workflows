# Stage 3: Scan Candidates

Scan bounded roots for source candidates.

## Rules

- Use `rg --files` for local inventories when available.
- Keep scans shallow first; deepen only when the user asked for it or a root is clearly bounded.
- Exclude secrets, caches, dependency folders, build output, binaries, dumps, and editor noise.
- For URLs or external systems, inspect only explicitly approved locations.
- For registered target repos, run read-only Git checks only:
  - current branch;
  - current commit;
  - worktree state;
  - remote;
  - changed files since `last_scanned_commit` when available.
- Do not copy code into `raw/`; capture changed paths, metadata, bounded excerpts, and command
  output summaries only.

## Candidate Metadata

Capture:

- path or URL;
- likely source type;
- reason it appears relevant;
- whether already registered;
- last modified date if available;
- size/scope;
- recommended action: `register`, `review`, `ignore`, or `defer`.

## Registered Target Refresh Metadata

Capture for each target repo in scope:

- `target_id`;
- registered repo path and remote;
- registered branch and last scanned commit;
- current branch and commit;
- worktree state;
- changed files between last scanned commit and current commit;
- source summaries/wiki pages that depend on changed files;
- recommended action: `fresh`, `mark-stale`, `refresh-source-summary`, `run-code-project-scan`,
  `review`, or `defer`.

## Continue When

You have a concise candidate list with registration recommendations and, when target repos were in
scope, a stale/refresh candidate list.

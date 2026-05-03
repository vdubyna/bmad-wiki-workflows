# Stage 1: Maintenance Scope

Define a bounded maintenance pass before scanning.

## Steps

1. Check the current wiki repo status with `git status --short`.
2. Identify maintenance purpose:
   - find unregistered sources;
   - detect changed sources;
   - refresh stale source statuses;
   - refresh from registered target repos;
   - prepare source-registration backlog;
   - audit wiki freshness.
3. Identify scan roots only from user input, existing wiki references, registered targets in
   `wiki/targets/`, or explicit saved workflow context.
4. Ask before scanning broad roots, external systems, or URLs.
5. If registered target repos are in scope, confirm the pass is read-only and bounded to:
   - check registered target repos;
   - compare last scanned commit with current commit;
   - list changed files;
   - map changed files to source summaries/wiki pages;
   - propose refresh tasks.
6. Record must-include and must-exclude boundaries.

## Continue When

You can state scan roots or registered targets, exclusions, maintenance purpose, whether
registration may happen during this pass, and whether stale pages may be marked but not rewritten.

# Stage 1: Maintenance Scope

Define a bounded maintenance pass before scanning.

## Steps

1. Check the current wiki repo status with `git status --short`.
2. Identify maintenance purpose:
   - find unregistered sources;
   - detect changed sources;
   - refresh stale source statuses;
   - prepare source-registration backlog;
   - audit wiki freshness.
3. Identify scan roots only from user input, existing wiki references, or explicit saved workflow
   context.
4. Ask before scanning broad roots, external systems, or URLs.
5. Record must-include and must-exclude boundaries.

## Continue When

You can state scan roots, exclusions, maintenance purpose, and whether registration may happen during
this pass.

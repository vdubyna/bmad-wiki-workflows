# Stage 5: Maintenance Report

Close with a compact maintenance record.

## Raw Candidate Record

Create when candidates were found:

```text
raw/inbox/YYYY-MM-DD-maintenance-source-candidates.md
```

Use `resources/maintenance-source-candidates-template.md`.

Include:

- scan roots;
- registered targets checked;
- exclusions;
- known source baseline;
- last scanned commit versus current target commit;
- changed files;
- stale page candidates;
- candidate table;
- triage decisions;
- registrations completed;
- deferred work.

## Log

Append `wiki/log.md` with:

- maintenance purpose;
- scan roots;
- registered targets checked;
- counts by action;
- stale/refresh task count;
- files created or updated;
- next recommended registration.

## Ask

Ask only the next decision needed:

- Which review/deferred candidate should be registered next?
- Should any source be marked superseded or archived?
- Should any code-derived page be marked stale or refreshed from a new target snapshot?
- Should this maintenance scope become a recurring practice?

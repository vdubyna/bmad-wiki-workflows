---
type: target-repo
status: draft
target_id:
topic:
tags:
  - target-repo
  - codebase
repo_path:
remote:
branch:
current_commit:
last_scanned_commit:
worktree_state:
scan_scope: []
exclusions: []
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# <Target> Target Registry

## Target Identity

```yaml
target_id:
repo_path:
remote:
branch:
current_commit:
last_scanned_commit:
worktree_state: clean|dirty|non-git|unknown
dirty_changes: ignore|include|inventory-only|unknown
```

## Scan Scope

```yaml
scan_scope:
  - src/
  - tests/
  - docs/
exclusions:
  - vendor/
  - node_modules/
  - .git/
```

## Authority Layers

- Code/tests/manifests: current behavior.
- Official docs/README: canonical project docs.
- AI research/deep research: generated context.
- Wiki pages: compiled synthesis, not source of truth.
- Decisions: valid only after human review.

## Last Scan

- Last scanned commit:
- Last snapshot packet:
- Last source summary:
- Last scanned at:
- Scanner/workflow:

## Stale Detection

- Current commit checked:
- Changed files since last scan:
- Wiki pages needing refresh:

## Dependent Wiki Pages

| Wiki Page | Evidence Source | Depends On | Verified Commit | Status |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## Notes

## Open Questions

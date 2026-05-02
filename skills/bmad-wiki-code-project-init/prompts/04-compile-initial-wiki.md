# Stage 4: Compile Initial Wiki

Convert quick-scan evidence into wiki artifacts.

## Raw Packet

Create:

```text
raw/project/YYYY-MM-DD-<project-slug>-repo-initial-scan.md
```

Use `resources/raw-packet-template.md`.

The raw packet must include a scan scope contract:

```yaml
scan_scope:
  target:
    path_or_url:
    branch_or_commit:
    commit_hash:
    worktree_state:
    dirty_changes: none|include|ignore|unknown
  purpose:
  mode: quick|focused-deep|exhaustive
  include:
    dirs: []
    file_types: []
    canonical_docs: []
  exclude:
    dirs: []
    file_types: []
    reasons: []
  authority:
    current_behavior: []
    planned_direction: []
    generated_dirty_context: []
  assumptions: []
  unresolved_questions: []
```

## Source Summary

Create:

```text
wiki/sources/YYYY-MM-DD-<project-slug>-repo-initial-scan.md
```

Use `resources/source-summary-template.md`.

## Project Profile

Create or update:

```text
wiki/concepts/<project-slug>-project-profile.md
```

Use `resources/project-profile-template.md`.

## Index And Log

- Update `wiki/index.md` with new source summary and project profile links.
- Append a `wiki/log.md` entry.
- Keep status as `draft` unless the user explicitly approves.

## Continue When

The wiki has a reviewable initial profile and a concrete deep scan proposal.

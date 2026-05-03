# Stage 4: Compile Initial Wiki

Convert quick-scan evidence into wiki artifacts.

## Target Registration

Create or update before writing scan-derived wiki pages:

```text
wiki/targets/<target-id>.md
```

Use `resources/target-registry-template.md`.

The target registration must include:

```yaml
target_id:
repo_path:
remote:
branch:
current_commit:
worktree_state: clean|dirty|non-git|unknown
scan_scope: []
exclusions: []
last_scanned_commit:
last_snapshot:
```

If an existing target registration has different scope, exclusions, remote, or branch, preserve the
old values in a note and record the new values as a reviewable update.

## Raw Packet

Create:

```text
raw/project/YYYY-MM-DD-<target-id>-snapshot-<shortsha>-scan.md
```

Use `resources/raw-packet-template.md`.

The raw packet must include a scan scope contract:

```yaml
scan_scope:
  target_id:
  target_registry:
  target:
    path_or_url:
    remote:
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
    canonical_project_docs: []
    planned_direction: []
    generated_context: []
    compiled_synthesis: []
    human_reviewed_decisions: []
  assumptions: []
  unresolved_questions: []
commands_used: []
files_inspected: []
skipped:
  files: []
  dirs: []
  reasons: []
changed_since_last_scan: []
```

## Source Summary

Create:

```text
wiki/sources/YYYY-MM-DD-<target-id>-snapshot-<shortsha>-scan.md
```

Use `resources/source-summary-template.md`.

Every code-derived source summary should include an evidence chain:

```text
claim -> source summary -> raw scan packet -> repo commit + file path + symbol/line range
```

Use line ranges when they were actually inspected. Use symbol/path-level evidence when line ranges
were not captured. Do not invent line ranges.

## Project Profile

Create or update:

```text
wiki/concepts/<project-slug>-project-profile.md
```

Use `resources/project-profile-template.md`.

## Benchmark-Aware Wiki Surface

If the wiki purpose includes retrieval, coding assistance, evaluation, or benchmark tracking, create
or propose:

```text
wiki/experiments/YYYY-MM-DD-<target-id>-retrieval-benchmark.md
```

Use `resources/benchmark-report-template.md`.

Track at least the metrics that matter for the target:

- Recall@K;
- MRR;
- NDCG;
- citation precision;
- patch success;
- stale lag;
- latency;
- cost.

## Decision Records

For conclusions such as "code retrieval is the authority layer and wiki is the synthesis layer",
propose a decision record path such as:

```text
wiki/decisions/code-retrieval-is-authority-layer.md
```

Use `resources/decision-record-template.md`, but keep it `status: draft` until human review.

## Index And Log

- Update `wiki/index.md` with target registration, new source summary, and project profile links.
- Append a `wiki/log.md` entry.
- Keep status as `draft` unless the user explicitly approves.

## Retrieval-First Rule For Coding Questions

Add or preserve a wiki note that future code answers should follow this order:

1. Use `wiki/index.md` for navigation.
2. Use `wiki/sources/*` for context.
3. Verify against the registered target repo code at the referenced commit/current checkout.
4. Answer with clear labels: fact, inference, or hypothesis.

## Continue When

The wiki has a reviewable initial profile and a concrete deep scan proposal.

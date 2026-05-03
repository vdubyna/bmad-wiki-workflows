# Stage 4: Triage And Register

Convert clear candidates into source-registration handoffs.

## Triage

- `register`: source is relevant, permitted, bounded, and not already registered.
- `review`: source may matter but needs human confirmation.
- `ignore`: source is noise, generated output, cache, or explicitly excluded.
- `defer`: source is relevant but too large or broad for this pass.
- `fresh`: registered target has no relevant changed files.
- `mark-stale`: a changed target file maps to one or more wiki pages; mark pages
  `status: stale` or `needs-refresh: true` only if this was approved for the pass.
- `refresh-source-summary`: source summary should be regenerated from a new snapshot packet.
- `run-code-project-scan`: target repo needs a new `bmad-wiki-code-project-init` or focused scan
  pass.

## Registration

- For one or a few clear approved candidates, follow `bmad-wiki-source-registration` behavior
  directly: create raw source record, source summary, index/log updates.
- For many candidates, do not bulk-register by default. Create a prioritized handoff list.
- Keep generated context and working notes in lower authority layers.

## Target Refresh

- Check registered target repos.
- Compare the wiki `last_scanned_commit` with the current target repo commit.
- List changed files between those commits.
- Map changed files to wiki pages through `target_id`, `verified_commit`, `depends_on_paths`,
  source summary links, raw packet links, and evidence trace tables.
- Propose refresh tasks before rewriting pages.
- Do not rewrite code-derived wiki pages automatically without human review.
- Do not promote decisions to valid/approved without human review.

## Continue When

Every candidate has an action and clear candidates are either registered, queued for registration,
marked stale with approval, or queued for target refresh.

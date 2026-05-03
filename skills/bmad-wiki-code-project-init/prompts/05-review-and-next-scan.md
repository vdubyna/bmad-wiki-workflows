# Stage 5: Review And Next Scan

Close with a human review gate and a proposed deep scan plan.

## Present

Summarize:

- files created or updated;
- target registration path and status;
- target commit/worktree state;
- authority layers;
- snapshot packet path;
- stale/refresh baseline: last scanned commit and current commit;
- assumptions;
- open questions;
- recommended deep scan slices.

## Ask

Ask only the next decision needed:

- Is the project profile acceptable as `draft`?
- Which deep scan slice should run first?
- Should generated/planned artifacts remain included with lower-authority markers?
- Are there extra privacy exclusions before deep scan?
- Should target registration changes be accepted as the wiki baseline?
- Should any draft decisions be promoted to reviewed decision records?

## Do Not

- Do not commit without explicit approval.
- Do not mark pages `approved` without user review.
- Do not mark decision records valid without human review.
- Do not begin exhaustive scanning unless the user asks for it.

## Suggested Deep Scan Slice Format

```text
slice:
  name:
  folders:
  tests:
  questions:
  expected_outputs:
  risks:
```

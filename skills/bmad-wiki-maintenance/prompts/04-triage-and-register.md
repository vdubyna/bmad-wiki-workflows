# Stage 4: Triage And Register

Convert clear candidates into source-registration handoffs.

## Triage

- `register`: source is relevant, permitted, bounded, and not already registered.
- `review`: source may matter but needs human confirmation.
- `ignore`: source is noise, generated output, cache, or explicitly excluded.
- `defer`: source is relevant but too large or broad for this pass.

## Registration

- For one or a few clear approved candidates, follow `bmad-wiki-source-registration` behavior
  directly: create raw source record, source summary, index/log updates.
- For many candidates, do not bulk-register by default. Create a prioritized handoff list.
- Keep generated context and working notes in lower authority layers.

## Continue When

Every candidate has an action and clear candidates are either registered or queued for registration.

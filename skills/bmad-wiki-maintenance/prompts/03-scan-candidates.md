# Stage 3: Scan Candidates

Scan bounded roots for source candidates.

## Rules

- Use `rg --files` for local inventories when available.
- Keep scans shallow first; deepen only when the user asked for it or a root is clearly bounded.
- Exclude secrets, caches, dependency folders, build output, binaries, dumps, and editor noise.
- For URLs or external systems, inspect only explicitly approved locations.

## Candidate Metadata

Capture:

- path or URL;
- likely source type;
- reason it appears relevant;
- whether already registered;
- last modified date if available;
- size/scope;
- recommended action: `register`, `review`, `ignore`, or `defer`.

## Continue When

You have a concise candidate list with registration recommendations.

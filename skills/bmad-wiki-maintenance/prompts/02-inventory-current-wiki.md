# Stage 2: Inventory Current Wiki

Understand what the wiki already knows before looking for new sources.

## Read

- `wiki/index.md` if present;
- `wiki/log.md` if present;
- `wiki/targets/` registered target repos;
- `wiki/sources/` summaries;
- source registry sections if present;
- recent raw inbox/project records when relevant.

## Capture

- registered source locators;
- registered target repos with `target_id`, repo path, remote, branch, last scanned commit, scan
  scope, and exclusions;
- active/draft/superseded statuses;
- known source roots;
- code-derived page dependencies: `target_id`, `verified_commit`, `depends_on_paths`, raw packet
  links, source summary links;
- recent maintenance entries;
- obvious gaps or stale records.

## Continue When

You have a baseline list of known sources, registered targets, candidate scan roots, and
code-derived pages that can be checked for staleness.

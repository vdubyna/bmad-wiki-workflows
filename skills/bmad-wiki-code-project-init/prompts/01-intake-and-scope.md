# Stage 1: Intake, Scope, And Target Registration

Establish intent, verify the target code repo, and prepare a target registration before scanning.

## Steps

1. Check the current wiki repo status with `git status --short`.
2. Identify the target code repo path or URL only from the user message or explicit saved workflow
   context.
3. If the target repo path or URL is missing, stop and ask for the minimum missing intake:
   - project name or short project description;
   - local repo path or remote URL for analysis;
   - whether read-only commands may run in that repo;
   - branch/tag/commit if a specific source of truth is required;
   - scan purpose and must-include/must-exclude items if known.
4. Do not infer or auto-discover the target repo location from the current directory, wiki repo name,
   sibling folders, recent context, git remotes, package names, or common project layouts.
5. Run a target repo verification gate before any scan:
   - For a local path, expand exactly the supplied path, verify it exists and is readable, then
     determine whether it is a Git repo.
   - For a Git repo, capture branch, commit, remotes, and worktree status with read-only commands.
   - For a non-Git directory, record that fact and verify a filesystem inventory can run.
   - For a remote URL, verify that the URL was explicitly supplied. Do not clone or fetch it unless
     the user asked for that or approves it; otherwise ask for a local checkout path.
   - If the supplied target appears to be the wiki repo itself, ask for confirmation unless the user
     explicitly requested self-documentation.
   - If canonical docs, manifests, configs, source folders, or tests are not visible, ask for the
     missing project description/scope instead of inventing it.
6. Derive a stable `target_id` from explicit user input or the verified repository name. Keep it
   short, lowercase, and filesystem-safe, for example `codeman`.
7. Prepare a target registration contract before scan/ingest. It must include:
   - `target_id`;
   - `repo_path` or explicitly supplied remote URL;
   - `remote`;
   - `branch`;
   - `commit`;
   - `worktree_state`: `clean`, `dirty`, `non-git`, or `unknown`;
   - `scan_scope`;
   - `exclusions`;
   - dirty-change handling;
   - last scan status, if an existing `wiki/targets/<target_id>.md` is present.
8. Ask only additional questions that change the scan result:
   - Which branch/tag/commit is the source of truth?
   - Should dirty changes be included, ignored, or only inventoried?
   - What is the wiki purpose: onboarding, architecture, search/retrieval, benchmark, audit,
     migration, debugging?
   - Which folders/files are must-include?
   - Which folders/files/data are must-exclude?
   - Which stack/languages are expected?
   - What first output matters most?
9. If the user says to proceed autonomously, infer conservative read-only answers for scan options
   only after the target repo location and identity have passed verification.
10. Record assumptions and verification results for the target registration and raw packet.

## Default Decisions

- Scan mode: `quick`.
- Target repo: no default. Require a user-supplied or explicitly saved path/URL.
- Dirty changes: `ignore` unless explicitly requested.
- Include: docs, manifests, configs, source/test inventory.
- Exclude: secrets, dependencies, caches, build output, binaries, dumps.
- First output: raw packet, source summary, project profile, deep scan plan.

## Continue When

You can state:

- target repo;
- target repo source: user-supplied path/URL or explicit saved workflow context;
- target repo verification result;
- target registration contract;
- wiki repo;
- scan purpose;
- include/exclude assumptions;
- dirty-change handling;
- first output.

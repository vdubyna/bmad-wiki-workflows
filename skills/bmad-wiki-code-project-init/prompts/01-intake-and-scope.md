# Stage 1: Intake And Scope

Establish intent before scanning.

## Steps

1. Check the current wiki repo status with `git status --short`.
2. Identify the target code repo path or URL from the user message.
3. If missing, ask for the target repo path or URL.
4. Ask only questions that change the scan result:
   - Which branch/tag/commit is the source of truth?
   - Should dirty changes be included, ignored, or only inventoried?
   - What is the wiki purpose: onboarding, architecture, search/retrieval, benchmark, audit,
     migration, debugging?
   - Which folders/files are must-include?
   - Which folders/files/data are must-exclude?
   - Which stack/languages are expected?
   - What first output matters most?
5. If the user says to proceed autonomously, infer conservative read-only answers.
6. Record assumptions for the raw packet.

## Default Decisions

- Scan mode: `quick`.
- Dirty changes: `ignore` unless explicitly requested.
- Include: docs, manifests, configs, source/test inventory.
- Exclude: secrets, dependencies, caches, build output, binaries, dumps.
- First output: raw packet, source summary, project profile, deep scan plan.

## Continue When

You can state:

- target repo;
- wiki repo;
- scan purpose;
- include/exclude assumptions;
- dirty-change handling;
- first output.

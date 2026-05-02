# Stage 1: Intake And Project Shape

Establish project identity, purpose, source locations, and privacy boundaries before reading docs.

## Steps

1. Check the current wiki repo status with `git status --short`.
2. Identify the project name and source locations only from the user message or explicit saved
   workflow context.
3. If source locations are missing, ask for:
   - project name or short project description;
   - local folder paths, document paths, or URLs to use as source material;
   - whether read-only inspection may run;
   - must-include and must-exclude areas;
   - wiki purpose: onboarding, reference, retrieval, audit, migration, research, or operations.
4. Verify supplied local paths exist and are readable before scanning.
5. For URLs or external systems, do not fetch or connect unless the user explicitly supplied the URL
   and approved access.
6. Record assumptions, exclusions, and authority layers for the raw intake packet.

## Continue When

You can state:

- project identity;
- source locations and access status;
- wiki repo;
- scan purpose;
- include/exclude assumptions;
- first output.

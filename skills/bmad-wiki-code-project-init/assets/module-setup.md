# Module Setup

Use this when the user asks for `setup`, `configure`, or help registration.

1. Resolve `{project-root}` as the current project root.
2. Resolve `{skill-root}` as the folder containing this `SKILL.md`.
3. If `{project-root}/_bmad/` does not exist, explain that BMAD is not installed in this project and
   skip registration.
4. Run:

   ```sh
   python3 {skill-root}/scripts/merge-help-csv.py --project-root {project-root} --module-help {skill-root}/assets/module-help.csv
   ```

5. Run:

   ```sh
   python3 {skill-root}/scripts/merge-config.py --project-root {project-root} --module-yaml {skill-root}/assets/module.yaml
   ```

6. Summarize the registration result. Do not commit.

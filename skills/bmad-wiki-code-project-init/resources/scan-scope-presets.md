# Scan Scope Presets

Use these as starter presets when the user does not provide precise scope.

## Always Include Candidates

- Canonical docs: `README*`, `docs/**`, `AGENTS.md`, `CHANGELOG*`, `CONTRIBUTING*`.
- Manifests/config: `composer.json`, `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`,
  `Makefile`, `Dockerfile`, `.github/workflows/**`.
- Tests: `tests/**`, `test/**`, `spec/**`, `__tests__/**`.
- Architecture artifacts: `docs/architecture/**`, `adr/**`, `decisions/**`.

## Minimal Codebase Scope

Use this when the user asks for a conservative code wiki baseline and does not provide a custom
scope:

- Dirs: `src/**`, `tests/**`, `docs/**`.
- Exclusions: `.git/**`, `vendor/**`, `node_modules/**`.
- Capture only metadata, summaries, bounded excerpts, command output, and benchmark output in
  `raw/`; keep source code in the target repo.

## PHP/Symfony

- Dirs: `src/**`, `config/**`, `templates/**`, `tests/**`, `migrations/**`.
- Files: `composer.json`, `composer.lock` for dependency overview only, `symfony.lock`,
  `.env.example`, `phpunit.xml*`.
- Extensions: `.php`, `.twig`, `.yaml`, `.yml`, `.xml`, `.neon`.

## JS/TS

- Dirs: `src/**`, `app/**`, `lib/**`, `packages/**`, `components/**`, `tests/**`,
  `__tests__/**`.
- Files: `package.json`, lockfiles for dependency overview only, `tsconfig*.json`,
  `vite.config.*`, `next.config.*`, `jest.config.*`, `playwright.config.*`.
- Extensions: `.js`, `.jsx`, `.ts`, `.tsx`, `.mjs`, `.cjs`, `.html`, `.css`, `.scss`.

## Python

- Dirs: `src/**`, package folders, `tests/**`, `docs/**`, `scripts/**`.
- Files: `pyproject.toml`, `setup.cfg`, `setup.py`, `requirements*.txt`, `tox.ini`,
  `pytest.ini`, `ruff.toml`.
- Extensions: `.py`, `.toml`, `.ini`, `.cfg`, `.yaml`, `.yml`.

## Docs/Config

- Dirs: `docs/**`, `.github/workflows/**`, `config/**`, `deploy/**`, `infra/**`.
- Files: `README*`, `AGENTS.md`, `CHANGELOG*`, `CONTRIBUTING*`, `Makefile`, `Dockerfile`.
- Extensions: `.md`, `.mdx`, `.rst`, `.txt`, `.json`, `.yaml`, `.yml`, `.toml`, `.xml`.

## Default Excludes

- Secrets: `.env`, `.env.*`, private keys, credentials.
- VCS/runtime/cache: `.git/**`, `.codeman/**`, `.local/**`, `.cache/**`, `.pytest_cache/**`,
  `.ruff_cache/**`, `.mypy_cache/**`.
- Dependencies: `vendor/**`, `node_modules/**`, `.venv/**`, `venv/**`.
- Build output: `dist/**`, `build/**`, `coverage/**`, `target/**`, `var/cache/**`.
- Binaries/media unless requested: images, videos, archives, DB dumps.
- Generated bundles unless requested: `.min.js`, `.map`.

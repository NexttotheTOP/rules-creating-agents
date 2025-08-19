# Coding Standards

This document outlines the coding conventions and best practices for the project.

## Linting & Formatting

- Frontend: ESLint with `eslint-config-next` and Prettier
  - Lint: `pnpm --filter frontend lint`
  - Format: `pnpm --filter frontend format`
- Backend: Ruff and Black
  - Lint: `ruff apps/backend`
  - Format: `black --check apps/backend`

## Commit Messages

Adopt Conventional Commits:

```
<type>(<scope>): <subject>
```

Types:

- feat: A new feature
- fix: A bug fix
- docs: Documentation changes
- style: Code style changes (formatting)
- refactor: Code refactoring
- test: Adding or updating tests
- chore: Maintenance and tooling

Example:

```
feat(api): add /generate endpoint
```

## Branch Naming

- feature/<feature-name>
- fix/<bug-description>
- chore/<task-name>

## Pull Requests

- Title should follow Conventional Commits format
- Describe the purpose and context of changes
- Include related issue numbers
- Ensure all CI checks pass

## Code Reviews

- Provide constructive feedback
- Check for code quality, readability, and test coverage

## Logging

- Backend: Use Python `logging` module
- Frontend: Use `console` for logs or integrate external logger
- Use appropriate log levels: DEBUG, INFO, WARNING, ERROR

## Documentation

- Update `Docs/Implementation.md` and `Docs/project_structure.md` when changing architecture or structure
- Keep documentation up to date with code changes

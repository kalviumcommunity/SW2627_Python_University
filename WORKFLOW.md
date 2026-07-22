# Team GitHub Workflow

## Branching Strategy

- main contains production-ready code.
- Every new feature is developed in a feature branch.
- Branch names follow:
  - feature/<description>
  - fix/<description>
  - docs/<description>
  - refactor/<description>
  - chore/<description>
- Branches are deleted after merging.

---

## Commit Convention

Format

[type]: description

Types

- feat
- fix
- docs
- refactor
- chore

Examples

feat: add data validation

docs: update project documentation

fix: resolve upload bug

Reason

Using consistent commit messages makes project history easier to understand and supports automated changelog generation.

---

## Pull Request Process

Every Pull Request should:

- Explain what changed
- Explain why it changed
- Link related GitHub issues
- Receive at least one approval before merging

Reviews focus on:

- Correctness
- Readability
- Data integrity
- Test coverage

---

## GitHub Issue Workflow

Every feature or bug starts with an issue.

Issues include:

- Title
- Description
- Label
- Assignee

Issues are closed automatically after the Pull Request is merged.

## Branch Naming Examples

feature/data-cleaning

feature/model-training

fix/csv-validation

## Code Review Checklist

- Code readability
- Tests passed
- Documentation updated
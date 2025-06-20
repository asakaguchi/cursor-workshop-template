# CLAUDE.md

This file provides guidance for Claude Code (claude.ai/code) when working with code in this repository.

## Language Processing Instructions

**IMPORTANT**: Even when receiving instructions in Japanese, always think and process in English internally. However, respond to the user in Japanese when they communicate in Japanese.

**Note**: When using the Cursor editor, also refer to the rule files in the `.cursor/rules/` directory. The following are particularly important:

- `python-structure.mdc`: Modern Python project structure (src layout)
- `code-quality-enforcement.mdc`: Code quality and development guidelines
- `development-workflow.mdc`: Development flow and GitHub integration
- `pep8-enforcement.mdc`: Python coding standards

## References

This project is built based on the following resources:

- **Article**: [Building a Modern Python Development Environment with Docker](https://zenn.dev/mjun0812/articles/0ae2325d40ed20)
- **Template**: [mjun0812/python-project-template](
  https://github.com/mjun0812/python-project-template)
  - Particularly referencing the structure of [CLAUDE.md](
    https://github.com/mjun0812/python-project-template/blob/main/CLAUDE.md)

Many elements including Docker configuration, uv usage, and project structure are based on the above resources.

## Project Overview

This is a Cursor workshop template for building a **Product Management API** using Python and FastAPI. It implements a simple REST API for product management using in-memory storage.

## Key Requirements

The API must implement:

- Create product (POST /items)
- Get product (GET /items/{id})
- Health check (GET /health)
- TDD approach using pytest
- FastAPI framework with automatic Swagger UI generation

### Product Data Structure

- id: Integer (auto-generated)
- name: String (required, at least 1 character)
- price: Float (required, greater than 0)
- created_at: Datetime (auto-set)

## Development Commands

### Package Management

**Important**: Always use uv, never use pip

```bash
# Sync project (recommended - automatically recognizes from pyproject.toml)
uv sync

# Only when adding new dependencies as needed
# uv add package_name
# uv add --dev dev_package_name
```

### Running the Application

```bash
# Start FastAPI server
uvicorn src.product_api.main:app --reload

# Access Swagger UI: http://localhost:8000/docs
```

### Testing

```bash
# Run all tests
uv run --frozen pytest

# Run specific test file
uv run --frozen pytest tests/test_filename.py

# Run tests with verbose output
uv run --frozen pytest -v

# If there are anyio plugin issues
PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest
```

### Code Quality Checks

```bash
# Code formatting
uv run --frozen ruff format .

# Lint check
uv run --frozen ruff check .

# Fix lint issues
uv run --frozen ruff check . --fix

# Type checking
uv run --frozen pyright

# Check Markdown files (required)
markdownlint *.md

# Install pre-commit hooks (first time only)
uv run --frozen pre-commit install

# Run pre-commit manually
uv run --frozen pre-commit run --all-files
```

## Architecture Notes

- **In-memory storage**: No database - data persists only during application runtime
- **Test context**: Use `tests/context.py` to import `product_api` without installation
- **Project structure**: Main API code in `src/product_api/`, tests in `tests/` (src layout adopted)
- **Error handling**: Proper validation and HTTP status code implementation
- **No authentication**: Out of scope for this workshop

## Development Flow

### Issue-Driven Development

This project adopts issue-driven development:

1. **Requirements review**: Review requirements in docs/requirements.md etc.
2. **Task breakdown**: Break down requirements into tasks completable in 15-30 minutes
3. **Issue registration**: Register each task as an issue using GitHub CLI
4. **Development**: Create a branch for each issue and implement with TDD approach
5. **PR creation**: Create PR after confirming tests pass and request review

#### Branch Naming Convention

- `feature/task-{issue-number}-{brief-description}`
- Example: `feature/task-1-project-setup`

#### GitHub CLI Usage Examples

```bash
# Create issue (use $'...' syntax for line breaks)
gh issue create -t "Title" -b $'## Summary\nImplementation description\n\n## Implementation\n- [ ] Item 1\n- [ ] Item 2'

# Create PR
gh pr create \
  --title "feat: feature name" \
  --body $'## Summary\nDescription of changes\n\n## Related Issue\nFixes #1'
```

## Development Guidelines

### Code Quality Requirements

- **Type hints**: Required for all code
- **Documentation**: Required for public APIs
- **Function design**: Small, focused functions
- **Line length limit**: Maximum 88 characters
- **Tests**: Required for new features and bug fixes
- **Markdown**: Always check with markdownlint after editing files and ensure zero errors

### Package Management Rules

- **Required**: Use only uv, pip is prohibited
- **Basic operation**: First `uv sync` to sync project (auto-recognizes from pyproject.toml)
- **Add new**: Only when needed `uv add package` / `uv add --dev package`
- **Run tools**: `uv run tool`
- **Prohibited**: `uv pip install`, duplicate addition of existing dependencies, `@latest` syntax

**Important**: If dependencies are already defined in pyproject.toml,
do not duplicate with `uv add`, use only `uv sync`

### Testing Requirements

- **Framework**: `uv run --frozen pytest`
- **Async tests**: Use anyio, asyncio prohibited
- **Coverage**: Edge cases and error cases

## Technical Constraints

- Python 3.12 or higher required
- No external database
- No authentication/authorization
- No update/delete operations (create and read only)
- FastAPI for REST API with auto-generated documentation

## Git Commit Guidelines

- When bug fixes or features are based on user reports:

  ```bash
  git commit --trailer "Reported-by:<name>"
  ```

- When related to GitHub issues:

  ```bash
  git commit --trailer "Github-Issue:#<number>"
  ```

- **Prohibited**: Absolutely avoid mentioning `co-authored-by` or tool usage

## Pull Requests

- Include detailed description of changes
- Focus on the problem being solved and how it's solved
- **Prohibited**: Absolutely avoid mentioning `co-authored-by` or tool usage

## Error Resolution

### CI Failure Resolution Order

1. Fix formatting
2. Fix type errors
3. Fix lint errors

### Common Issues

- **Line length limit**: Split strings with parentheses, multi-line function calls, split imports
- **Type errors**: Check Optional, type narrowing, verify function signatures
- **pytest execution failure**: First run `uv sync`, don't duplicate existing dependencies
- **Coverage measurement failure**: Already configured in pyproject.toml, no additional config files needed
- **Pytest**: If anyio pytest mark not found, add `PYTEST_DISABLE_PLUGIN_AUTOLOAD=""`

### Best Practices

- Check git status before committing
- Run formatter before type checking
- Always run markdownlint after editing Markdown files
- Keep changes minimal
- Follow existing patterns
- Always document public APIs

## Important Instruction Reminders

Do what has been asked; nothing more, nothing less.

NEVER create files unless they're absolutely necessary for achieving your goal.

ALWAYS prefer editing an existing file to creating a new one.

NEVER proactively create documentation files (*.md) or README files.
Only create documentation files if explicitly requested by the User.

## important-instruction-reminders

Do what has been asked; nothing more, nothing less.
NEVER create files unless they're absolutely necessary for achieving your goal.
ALWAYS prefer editing an existing file to creating a new one.
NEVER proactively create documentation files (*.md) or README files.
Only create documentation files if explicitly requested by the User.

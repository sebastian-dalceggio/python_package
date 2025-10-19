# Python Development Guide

This guide covers workflows, best practices, and conventions for developing Python projects. Use this as a reference during active development.

## Table of Contents

- [Git Workflow](#git-workflow)
- [Code Style Guidelines](#code-style-guidelines)
- [Testing Requirements](#testing-requirements)
- [Development Workflow](#development-workflow)
- [AI Assistant Guidelines](#ai-assistant-guidelines)

---

## Git Workflow

### Branch Strategy

**Main Branches:**
- `main` - Production-ready code only. Protected branch, never commit directly.
- `dev` - Development branch. Base for all feature branches.

**Feature Branches:**
- Create a new branch for each feature/fix from `dev`
- Naming conventions:
  - `feature/description` - New features
  - `fix/bug-name` - Bug fixes
  - `refactor/component-name` - Code refactoring
  - `docs/description` - Documentation updates

### Daily Workflow

```bash
# Morning: Start work
git checkout dev
git pull origin dev
git checkout -b feature/new-feature

# During day: Work with AI, commit frequently
# ... make changes with Claude Code ...
git add .
git commit -m "feat: implement X"
# ... make more changes ...
git add .
git commit -m "test: add tests for X"

# End of day or when feature complete
uv run pytest  # Ensure all tests pass
git push -u origin feature/new-feature
# Create PR on GitHub: feature/new-feature → dev

# After PR merged
git checkout dev
git pull origin dev
git branch -d feature/new-feature  # Delete local branch
```

### Commit Message Convention

Use **Conventional Commits** format:

```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, no logic change)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks (dependencies, config)
- `perf`: Performance improvements

**Examples:**
```bash
git commit -m "feat(auth): add JWT token validation"
git commit -m "fix(api): handle null response in user endpoint"
git commit -m "test(user): add edge cases for user creation"
git commit -m "docs(readme): update installation instructions"
git commit -m "refactor(database): simplify query builder logic"
```

### Commit Frequency

**DO commit after each logical unit:**
- ✅ After implementing a complete function + its tests
- ✅ After fixing a bug + adding regression test
- ✅ After refactoring a module (if all tests pass)
- ✅ After adding documentation for a feature

**DON'T commit:**
- ❌ In the middle of implementing a function
- ❌ With failing tests (unless it's a WIP commit with clear message)
- ❌ With syntax errors or broken code

### Working with AI Assistants

**When using Claude Code, Cursor, or similar:**

```bash
# AI implements function
git add src/project_name/auth.py
git commit -m "feat(auth): implement login function"

# AI writes tests
git add tests/test_auth.py
git commit -m "test(auth): add login function tests"

# AI adds docstrings
git add src/project_name/auth.py
git commit -m "docs(auth): add comprehensive docstrings"
```

This creates a clear history of what was done step by step.

### Protected Branches Setup (GitHub)

Configure branch protection for `main`:

1. Go to **Settings** → **Branches** → **Add rule**
2. Branch name pattern: `main`
3. Enable:
   - ✅ Require a pull request before merging
   - ✅ Require status checks to pass (CI must pass)
   - ✅ Require branches to be up to date
   - ✅ Require conversation resolution
   - ✅ Do not allow bypassing the above settings

### Useful Git Commands

```bash
# See what changed
git status
git diff

# Review changes before committing
git diff --staged

# Amend last commit (before pushing)
git commit --amend -m "new message"

# Undo last commit (keep changes)
git reset --soft HEAD~1

# Discard all local changes
git reset --hard HEAD

# Update feature branch with latest dev
git checkout feature/my-feature
git merge dev

# Squash commits before merging (clean history)
git rebase -i dev
```

---

## Code Style Guidelines

### Type Hints

**REQUIRED**: All functions must have complete type hints.

```python
# ✅ CORRECT
def process_user(user_id: int, name: str) -> dict[str, str | int]:
    """Process user information."""
    return {"id": user_id, "name": name}

# ❌ INCORRECT - Missing type hints
def process_user(user_id, name):
    return {"id": user_id, "name": name}
```

**Use modern Python 3.10+ syntax:**
- Use `|` instead of `Union`: `str | int` not `Union[str, int]`
- Use `list[str]` instead of `List[str]`
- Use `dict[str, int]` instead of `Dict[str, int]`
- Use `str | None` instead of `Optional[str]`

### Docstrings

**REQUIRED**: All functions, classes, and modules must have complete Google-style docstrings.

**All functions must include Args, Returns, and Raises sections (when applicable):**

```python
def add(a: int, b: int) -> int:
    """Add two numbers together.

    Args:
        a: The first number to add.
        b: The second number to add.

    Returns:
        The sum of a and b.
    """
    return a + b
```

**Complex function with all sections:**
```python
def fetch_user_data(
    user_id: int,
    include_posts: bool = False,
    max_posts: int = 10
) -> dict[str, str | list[dict[str, str]]]:
    """Fetch user data from the database.

    Args:
        user_id: The unique identifier for the user.
        include_posts: Whether to include the user's posts. Defaults to False.
        max_posts: Maximum number of posts to fetch. Defaults to 10.

    Returns:
        Dictionary containing user information with keys:
        - "name": User's full name
        - "email": User's email address
        - "posts": List of post dictionaries (if include_posts is True)

    Raises:
        ValueError: If user_id is negative.
        DatabaseError: If database connection fails.

    Example:
        >>> fetch_user_data(123, include_posts=True, max_posts=5)
        {"name": "John Doe", "email": "john@example.com", "posts": [...]}
    """
    if user_id < 0:
        raise ValueError("user_id must be non-negative")
    # Implementation...
```

**Class:**
```python
class UserManager:
    """Manage user operations and data access.

    This class provides methods for creating, updating, and retrieving
    user information from the database.

    Attributes:
        db_connection: Active database connection.
        cache_enabled: Whether to use caching for queries.
    """

    def __init__(self, db_connection: Connection, cache_enabled: bool = True) -> None:
        """Initialize the UserManager.

        Args:
            db_connection: Active database connection.
            cache_enabled: Enable query caching. Defaults to True.
        """
        self.db_connection = db_connection
        self.cache_enabled = cache_enabled
```

### Code Organization

**File structure:**
```python
"""Module description goes here.

This module provides functionality for...
"""

# Standard library imports
import os
import sys
from pathlib import Path

# Third-party imports
import requests
from pydantic import BaseModel

# Local imports
from project_name.core import utils
from project_name.models import User

# Constants
MAX_RETRIES = 3
DEFAULT_TIMEOUT = 30

# Code follows...
```

### Common Patterns

**Error Handling:**
```python
def divide(a: float, b: float) -> float:
    """Divide two numbers.

    Args:
        a: The numerator.
        b: The denominator.

    Returns:
        The result of a divided by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

**Using Path instead of os.path:**
```python
from pathlib import Path

# ✅ CORRECT
def read_config(config_path: Path) -> dict[str, str]:
    """Read configuration from a file.

    Args:
        config_path: Path to the configuration file.

    Returns:
        Dictionary containing configuration key-value pairs.
    """
    return json.loads(config_path.read_text())

# ❌ INCORRECT
def read_config(config_path: str) -> dict:
    with open(config_path) as f:
        return json.load(f)
```

**Context Managers:**
```python
def process_file(filepath: Path) -> list[str]:
    """Process a file and return its lines.

    Args:
        filepath: Path to the file to process.

    Returns:
        List of non-empty lines from the file.
    """
    with filepath.open() as f:
        return [line.strip() for line in f if line.strip()]
```

---

## Testing Requirements

### Test Coverage

**REQUIRED**: Write tests for every new function and class.

**Test file naming:**
- Test files: `test_<module_name>.py`
- Test functions: `test_<function_name>_<scenario>`
- Test classes: `Test<ClassName>`

### Test Structure

**Every test must have a docstring:**

```python
def test_add_positive_numbers():
    """Test that add() correctly sums two positive integers.

    Args:
        None

    Returns:
        None
    """
    result = add(2, 3)
    assert result == 5


def test_add_negative_numbers():
    """Test that add() handles negative numbers correctly.

    Args:
        None

    Returns:
        None
    """
    result = add(-2, -3)
    assert result == -5


def test_fetch_user_data_with_invalid_id():
    """Test that fetch_user_data raises ValueError for negative user_id.

    This is a regression test for issue #123 where negative IDs
    caused database corruption.

    Args:
        None

    Returns:
        None
    """
    with pytest.raises(ValueError, match="user_id must be non-negative"):
        fetch_user_data(-1)
```

### Test Organization

**Arrange-Act-Assert pattern:**

```python
def test_user_creation():
    """Test that User.create() properly initializes a user object.

    Args:
        None

    Returns:
        None
    """
    # Arrange
    user_data = {"name": "John Doe", "email": "john@example.com"}

    # Act
    user = User.create(**user_data)

    # Assert
    assert user.name == "John Doe"
    assert user.email == "john@example.com"
    assert user.created_at is not None
```

### Fixtures

Use pytest fixtures for reusable test data:

```python
@pytest.fixture
def sample_user() -> User:
    """Create a sample user for testing.

    Returns:
        A User instance with standard test data.
    """
    return User(name="Test User", email="test@example.com")


def test_user_validation(sample_user: User):
    """Test that user validation works correctly.

    Args:
        sample_user: A sample user fixture.

    Returns:
        None
    """
    assert sample_user.is_valid()
```

---

## Development Workflow

### When Adding New Features

1. **Create feature branch:**
   ```bash
   git checkout dev
   git pull origin dev
   git checkout -b feature/add-user-authentication
   ```

2. **Write the function signature with type hints first**
3. **Write the docstring** explaining what it does
4. **Implement the function**
5. **Write tests** covering:
   - Happy path (normal usage)
   - Edge cases (empty inputs, boundary values)
   - Error cases (invalid inputs, exceptions)

6. **Run quality checks:**
   ```bash
   uv run pytest
   uv run mypy src/
   uv run ruff check .
   ```

7. **Commit changes:**
   ```bash
   git add .
   git commit -m "feat(auth): add user authentication"
   git add tests/
   git commit -m "test(auth): add authentication tests"
   ```

8. **Push and create PR:**
   ```bash
   git push -u origin feature/add-user-authentication
   ```

### When Modifying Existing Code

1. **Read existing tests** to understand expected behavior
2. **Update implementation**
3. **Update tests** if behavior changed
4. **Add new tests** for new edge cases
5. **Update docstrings** if function signature or behavior changed
6. **Run full test suite**: `uv run pytest`

---

## AI Assistant Guidelines

### When Working with Claude Code, Cursor, etc.

**Workflow:**

1. **Start a new feature:**
   ```bash
   git checkout dev
   git pull origin dev
   git checkout -b feature/add-user-authentication
   ```

2. **Make changes with AI assistant:**
   - Let AI make changes
   - Review the changes carefully
   - Test the changes (`uv run pytest`)

3. **Commit frequently with descriptive messages:**
   ```bash
   # After AI implements one logical unit of work
   git add .
   git commit -m "feat: add User model with validation"

   # After AI adds tests
   git add tests/
   git commit -m "test: add tests for User model"

   # After AI adds documentation
   git add docs/
   git commit -m "docs: add User model documentation"
   ```

4. **When feature is complete:**
   ```bash
   # Make sure all tests pass
   uv run pytest
   uv run mypy src/
   uv run ruff check .

   # Push feature branch
   git push -u origin feature/add-user-authentication
   ```

5. **Create Pull Request:**
   - On GitHub: `feature/add-user-authentication` → `dev`
   - Wait for CI to pass
   - Review changes one more time
   - Merge to `dev`

### Code Quality Checklist

Before considering any code complete, verify:

- [ ] All functions have type hints (parameters and return type)
- [ ] All functions have complete Google-style docstrings with Args/Returns/Raises
- [ ] All public classes have docstrings
- [ ] Tests exist for all new/modified code
- [ ] All tests have docstrings
- [ ] Tests cover happy path, edge cases, and error cases
- [ ] No debug statements (`print()`, `breakpoint()`, etc.)
- [ ] Imports are organized (stdlib, third-party, local)
- [ ] No unused imports or variables
- [ ] Type hints use modern syntax (`|` not `Union`, `list` not `List`)
- [ ] `uv run pytest` passes
- [ ] `uv run mypy src/` passes
- [ ] `uv run ruff check .` passes

---

## Tools Reference

```bash
# Run tests
uv run pytest

# Run tests with coverage
uv run pytest --cov

# Type check
uv run mypy src/

# Lint
uv run ruff check .

# Format
uv run ruff format .

# Run all pre-commit hooks
uv run pre-commit run --all-files

# Add dependency
uv add package-name

# Add dev dependency
uv add --dev package-name
```

---

## Environment Configuration

### Working with .env Files

```bash
# Create example env file (commit this)
cat > .env.example << 'EOF'
DATABASE_URL=postgresql://localhost/mydb
SECRET_KEY=your-secret-key-here
DEBUG=false
EOF

# Create actual env file (DO NOT commit)
cp .env.example .env
# Edit .env with real values

# Ensure .env is in .gitignore
echo ".env" >> .gitignore
```

### Using pydantic-settings for Configuration

```python
# src/project_name/config.py
"""Application configuration."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables.

    Attributes:
        app_name: Name of the application.
        debug: Whether debug mode is enabled.
        log_level: Logging level for the application.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    app_name: str = "MyApp"
    debug: bool = False
    log_level: str = "INFO"


settings = Settings()
```

---

## Questions?

When in doubt:
1. Look at existing code for patterns
2. Check the test files for examples
3. Run `uv run ruff check .` to see if changes are acceptable
4. Run `uv run mypy src/` to verify type correctness
5. Reference this guide for workflows and conventions

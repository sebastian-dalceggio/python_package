# Python Project Setup Blueprint

A comprehensive template for initializing Python projects using modern tooling: `uv`, `pytest`, `mypy`, `ruff`, and `pre-commit`.

## Directory Structure

```
project_name/
├── .git/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   └── project_name/
│       ├── __init__.py
│       ├── main.py
│       └── py.typed
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── .gitignore
├── .pre-commit-config.yaml
├── pyproject.toml
├── README.md
├── .python-version
├── AI_DEVELOPMENT_GUIDE.md
└── uv.lock
```

## Setup Instructions

### 1. Initialize the Project

```bash
# Create project directory (use underscores, not hyphens)
mkdir project_name && cd project_name

# Initialize git
git init

# Set Python version (e.g., 3.12)
echo "3.12" > .python-version

# Initialize uv project
uv init

# Create source directory structure
mkdir -p src/project_name tests
touch src/project_name/__init__.py
touch src/project_name/main.py
touch src/project_name/py.typed
touch tests/__init__.py
touch tests/test_main.py
```

### 2. Configuration Files

#### `pyproject.toml`

```toml
[project]
name = "project_name"
version = "0.1.0"
description = "Project description"
readme = "README.md"
requires-python = ">=3.12"
dependencies = []

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "pytest-cov>=4.1.0",
    "mypy>=1.8.0",
    "ruff>=0.2.0",
    "pre-commit>=3.6.0",
]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/project_name"]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = [
    "--strict-markers",
    "--strict-config",
    "--cov=src/project_name",
    "--cov-report=term-missing",
    "--cov-report=html",
]

[tool.mypy]
python_version = "3.12"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true
disallow_incomplete_defs = true
check_untyped_defs = true
no_implicit_optional = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_no_return = true
strict_equality = true
strict_concatenate = true

[[tool.mypy.overrides]]
module = "tests.*"
disallow_untyped_defs = false

[tool.ruff]
target-version = "py312"
line-length = 100

[tool.ruff.lint]
select = [
    "E",      # pycodestyle errors
    "W",      # pycodestyle warnings
    "F",      # pyflakes
    "I",      # isort
    "B",      # flake8-bugbear
    "C4",     # flake8-comprehensions
    "UP",     # pyupgrade
    "ARG",    # flake8-unused-arguments
    "SIM",    # flake8-simplify
    "TCH",    # flake8-type-checking
    "PTH",    # flake8-use-pathlib
    "D",      # pydocstyle (docstrings)
    "RUF",    # ruff-specific rules
]
ignore = [
    "E501",   # line too long (handled by formatter)
    "D203",   # 1 blank line required before class docstring (conflicts with D211)
    "D213",   # multi-line docstring summary should start at second line (conflicts with D212)
]

[tool.ruff.lint.pydocstyle]
convention = "google"

[tool.ruff.lint.per-file-ignores]
"tests/**/*.py" = ["ARG", "S101"]
"__init__.py" = ["D104"]

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
```

#### `.pre-commit-config.yaml`

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
      - id: check-merge-conflict
      - id: check-toml
      - id: debug-statements

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.2.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
        additional_dependencies: []
        args: [--strict, --ignore-missing-imports]
```

#### `.gitignore`

```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/
.venv

# uv
.uv/
uv.lock

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/
coverage.xml

# Type checking
.mypy_cache/
.dmypy.json
dmypy.json

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Environment
.env
```

#### `README.md`

```markdown
# project_name

Project description goes here.

## Setup

```bash
# Clone the repository
git clone <repository-url>
cd project_name

# Install dependencies with uv
uv sync --all-extras

# Install pre-commit hooks
uv run pre-commit install
```

## Development

See [AI_DEVELOPMENT_GUIDE.md](AI_DEVELOPMENT_GUIDE.md) for detailed development guidelines and workflows.

```bash
# Run tests
uv run pytest

# Run type checking
uv run mypy src/

# Run linting
uv run ruff check .

# Format code
uv run ruff format .

# Run all pre-commit hooks
uv run pre-commit run --all-files
```

## Usage

```python
from project_name import main

# Your usage examples here
```
```

### 3. Install Dependencies and Setup

```bash
# Sync all dependencies including dev dependencies
uv sync --all-extras

# Install pre-commit hooks
uv run pre-commit install
```

### 4. Setup GitHub Actions CI/CD

```bash
# Create GitHub workflows directory
mkdir -p .github/workflows

# Create CI workflow file
cat > .github/workflows/ci.yml << 'EOF'
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: ["3.11", "3.12"]

    steps:
      - uses: actions/checkout@v4

      - name: Install uv
        uses: astral-sh/setup-uv@v2

      - name: Set up Python ${{ matrix.python-version }}
        run: uv python install ${{ matrix.python-version }}

      - name: Install dependencies
        run: uv sync --all-extras

      - name: Run pre-commit
        run: uv run pre-commit run --all-files

      - name: Run tests with coverage
        run: uv run pytest --cov-report=xml
EOF
```

### 5. Create Initial Commit

```bash
git add .
git commit -m "Initial project setup"
```

### 6. Setup Git Workflow

```bash
# Create and switch to dev branch
git checkout -b dev

# Push both branches to remote (if repository exists)
git push -u origin main
git push -u origin dev

# Set dev as your default working branch
git checkout dev
```

## Common Commands

```bash
# Add a new dependency
uv add package-name

# Add a dev dependency
uv add --dev package-name

# Run tests with coverage
uv run pytest

# Type check
uv run mypy src/

# Lint
uv run ruff check .

# Format
uv run ruff format .

# Run pre-commit on all files
uv run pre-commit run --all-files

# Update pre-commit hooks
uv run pre-commit autoupdate
```

## Next Steps

After initial setup is complete:

1. Review and update `AI_DEVELOPMENT_GUIDE.md` with project-specific guidelines
2. Configure branch protection on GitHub for `main` branch
3. Start development on `dev` branch
4. Create feature branches for new work

See the development guide for detailed workflows and best practices.

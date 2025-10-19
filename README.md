# python-package

Add your description here.

## Setup

```bash
# Clone the repository
git clone https://github.com/sebastian-dalceggio/python_package.git
cd python_package

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
from python_package import main

# Your usage examples here
```

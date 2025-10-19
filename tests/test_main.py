"""Tests for the main module."""

from python_package.main import hello


def test_hello() -> None:
    """Test the hello function."""
    assert hello() == "Hello from python_package!"

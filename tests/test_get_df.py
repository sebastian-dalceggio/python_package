"""Test module."""

import pandas as pd

from python_package.main import get_df


def test_get_df_correct_shape():
    """Tests if the DataFrame created by get_df has the correct shape (rows, columns)."""
    numbers_df = get_df(5)
    assert numbers_df.shape == (5, 2)


def test_get_df_correct_values():
    """Tests if the DataFrame created by get_df contains the correct values."""
    numbers_df = get_df(3)
    expected_data = [[0, 0], [1, 1], [2, 2]]
    expected_df = pd.DataFrame(expected_data, columns=["A", "B"])
    pd.testing.assert_frame_equal(numbers_df, expected_df)


def test_get_df_empty():
    """Tests if get_df returns an empty DataFrame when rows is 0."""
    numbers_df = get_df(0)
    assert numbers_df.empty


def test_get_df_correct_columns():
    """Tests if the DataFrame created by get_df has the correct column names."""
    numbers_df = get_df(1)
    assert list(numbers_df.columns) == ["A", "B"]

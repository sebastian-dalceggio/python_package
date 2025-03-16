"""Main Module."""

import pandas as pd


def get_df(rows: int) -> pd.DataFrame:
    """Create a pandas DataFrame with two columns, 'A' and 'B', where each column contains
    integers from 0 up to (but not including) the specified number of rows.

    Args:
      rows (int): The number of rows for the DataFrame.

    Returns:
      pd.DataFrame: A pandas DataFrame with the specified number of rows and columns 'A' and 'B'.

    """
    data_list = [(i, i) for i in range(rows)]
    print(data_list)
    return pd.DataFrame(data_list, columns=["A", "B"])


def main():
    """Run the process."""
    numbers_df: pd.DataFrame
    numbers_df = get_df(10)
    print(numbers_df.columns)
    print(numbers_df.info())
    print(numbers_df)


if __name__ == "__main__":
    main()

"Main Module"

import pandas as pd

def get_df(rows: int) -> pd.DataFrame:
    """Creates a pandas DataFrame with two columns, 'A' and 'B', where each column contains
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
    """Runs the process."""
    df: pd.DataFrame
    df = get_df(10)
    print(df.columns)
    print(df.info())
    print(df)

if __name__ == "__main__":
    main()

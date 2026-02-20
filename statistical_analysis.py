"""Statistical analysis utilities for the SME Sales Data Analytics project.

This module loads the cleaned sales dataset, selects numeric columns, and prints:
1. Correlation matrix
2. Variance for each numeric column

Only pandas is used for computations, as requested.
"""

from pathlib import Path
import pandas as pd

DATA_PATH = Path("data/processed/sales_dataset_cleaned_with_profit.csv")


def run_statistical_analysis(data_path: Path = DATA_PATH) -> None:
    """Compute and print correlation matrix and variance for numeric columns."""
    df = pd.read_csv(data_path)

    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        print("No numeric columns found in the dataset.")
        return

    print("=== Correlation Matrix (Numeric Columns) ===")
    print(numeric_df.corr())

    print("\n=== Variance (Numeric Columns) ===")
    print(numeric_df.var())


if __name__ == "__main__":
    run_statistical_analysis()

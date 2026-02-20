"""Statistical analysis module using pandas only."""

from pathlib import Path
import pandas as pd
from src.data_utils import DEFAULT_DATA_PATH, load_dataset


def statistical_summary(data_path: Path = DEFAULT_DATA_PATH) -> tuple[pd.DataFrame, pd.Series]:
    """Return correlation matrix and variance for numeric columns."""
    df = load_dataset(data_path)
    numeric_df = df.select_dtypes(include="number")
    if numeric_df.empty:
        raise ValueError("No numeric columns found in dataset.")
    return numeric_df.corr(), numeric_df.var()


def print_statistical_summary(data_path: Path = DEFAULT_DATA_PATH) -> None:
    """Print correlation matrix and variance outputs."""
    corr_matrix, variance = statistical_summary(data_path)
    print("=== Correlation Matrix (Numeric Columns) ===")
    print(corr_matrix)
    print("\n=== Variance (Numeric Columns) ===")
    print(variance)

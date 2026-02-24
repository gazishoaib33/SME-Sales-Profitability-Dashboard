"""Statistical analysis module using pandas only."""

from pathlib import Path
import pandas as pd
from src.data_utils import DEFAULT_DATA_PATH, load_dataset


def statistical_summary(data_path: Path = DEFAULT_DATA_PATH) -> tuple[pd.DataFrame, pd.Series]:
    """Return correlation matrix and variance for numeric columns."""
    # Load cleaned data and keep only numeric columns for statistical computation.
    df = load_dataset(data_path)
    numeric_df = df.select_dtypes(include="number")

    if numeric_df.empty:
        raise ValueError("No numeric columns found in dataset.")

    # Correlation explains relationships; variance captures spread per feature.
    return numeric_df.corr(), numeric_df.var()


def print_statistical_summary(data_path: Path = DEFAULT_DATA_PATH) -> None:
    """Print correlation matrix and variance outputs."""
    corr_matrix, variance = statistical_summary(data_path)

    print("=== Statistical Analysis: Correlation Matrix (Numeric Columns) ===")
    print(corr_matrix.round(4).to_string())

    print("\n=== Statistical Analysis: Variance (Numeric Columns) ===")
    print(variance.round(4).to_string())

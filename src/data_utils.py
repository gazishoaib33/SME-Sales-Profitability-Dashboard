"""Shared data loading and feature preparation utilities."""

from pathlib import Path
import pandas as pd

PRIMARY_DATA_PATH = Path("data/sales_dataset_cleaned_with_profit.csv")
FALLBACK_DATA_PATH = Path("data/processed/sales_dataset_cleaned_with_profit.csv")
DEFAULT_DATA_PATH = PRIMARY_DATA_PATH
FEATURE_COLUMNS = ["Quantity", "Selling_Price", "Cost_Price"]
TARGET_COLUMN = "Profit"


def _is_placeholder_file(df: pd.DataFrame) -> bool:
    """Detect placeholder CSV files that do not contain the expected dataset."""
    return len(df.columns) == 1 and str(df.columns[0]).startswith("# Placeholder")


def load_dataset(data_path: Path = DEFAULT_DATA_PATH) -> pd.DataFrame:
    """Load the cleaned sales dataset, with fallback to processed data when needed."""
    df = pd.read_csv(data_path)
    if _is_placeholder_file(df):
        df = pd.read_csv(FALLBACK_DATA_PATH)
    return df


def get_model_data(df: pd.DataFrame):
    """Prepare feature matrix X and target vector y for predictive models."""
    missing = [col for col in FEATURE_COLUMNS + [TARGET_COLUMN] if col not in df.columns]
    if missing:
        raise ValueError(f"Dataset is missing required modeling columns: {missing}")
    return df[FEATURE_COLUMNS], df[TARGET_COLUMN]

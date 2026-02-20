"""Shared data loading and feature preparation utilities."""

from pathlib import Path
import pandas as pd

DEFAULT_DATA_PATH = Path("data/processed/sales_dataset_cleaned_with_profit.csv")
FEATURE_COLUMNS = ["Quantity", "Discount", "Revenue"]
TARGET_COLUMN = "Profit"


def load_dataset(data_path: Path = DEFAULT_DATA_PATH) -> pd.DataFrame:
    """Load the cleaned sales dataset."""
    return pd.read_csv(data_path)


def ensure_discount_column(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy of the dataframe with a Discount column available."""
    prepared_df = df.copy()
    if "Discount" not in prepared_df.columns:
        required_columns = {"Selling_Price", "Cost_Price"}
        if not required_columns.issubset(prepared_df.columns):
            raise ValueError(
                "Missing 'Discount'. To derive it, dataset must include 'Selling_Price' and 'Cost_Price'."
            )
        prepared_df["Discount"] = (
            (prepared_df["Cost_Price"] - prepared_df["Selling_Price"]) / prepared_df["Cost_Price"]
        ).fillna(0)
    return prepared_df


def get_model_data(df: pd.DataFrame):
    """Prepare feature matrix X and target vector y for predictive models."""
    prepared_df = ensure_discount_column(df)
    missing = [col for col in FEATURE_COLUMNS + [TARGET_COLUMN] if col not in prepared_df.columns]
    if missing:
        raise ValueError(f"Dataset is missing required modeling columns: {missing}")
    return prepared_df[FEATURE_COLUMNS], prepared_df[TARGET_COLUMN]

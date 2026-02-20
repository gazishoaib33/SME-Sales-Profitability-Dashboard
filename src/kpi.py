"""KPI computations for sales profitability analysis."""

from pathlib import Path
from src.data_utils import DEFAULT_DATA_PATH, load_dataset


def calculate_kpis(data_path: Path = DEFAULT_DATA_PATH) -> dict:
    """Calculate core KPIs from the cleaned sales dataset."""
    df = load_dataset(data_path)
    return {
        "Total Revenue": float(df["Revenue"].sum()),
        "Total Profit": float(df["Profit"].sum()),
        "Average Order Value": float(df["Revenue"].mean()),
    }


def print_kpis(data_path: Path = DEFAULT_DATA_PATH) -> None:
    """Print KPI summary in a readable format."""
    kpis = calculate_kpis(data_path)
    print("=== KPI Summary ===")
    print(f"Total Revenue: {kpis['Total Revenue']:.2f}")
    print(f"Total Profit: {kpis['Total Profit']:.2f}")
    print(f"Average Order Value: {kpis['Average Order Value']:.2f}")

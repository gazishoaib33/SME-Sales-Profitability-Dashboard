"""Entry point for running the SME Sales Profitability analysis workflow."""

from src.kpi import print_kpis
from src.ml_model import print_ml_model_results
from src.regression_analysis import print_regression_analysis
from src.statistical_analysis import print_statistical_summary


def run_pipeline() -> None:
    """Run KPI, statistical, regression, and ML analyses in sequence."""
    print_kpis()
    print()
    print_statistical_summary()
    print()

    try:
        print_regression_analysis()
    except ImportError as exc:
        print(f"Regression analysis skipped: {exc}")

    print()

    try:
        print_ml_model_results()
    except ImportError as exc:
        print(f"ML model analysis skipped: {exc}")


if __name__ == "__main__":
    run_pipeline()

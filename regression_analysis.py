"""Backward-compatible entry point for regression analysis."""

from src.regression_analysis import print_regression_analysis


if __name__ == "__main__":
    print_regression_analysis()
    try:
        print_regression_analysis()
    except ImportError as exc:
        print(f"Regression analysis skipped: {exc}")

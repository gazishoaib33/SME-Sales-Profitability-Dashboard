"""Backward-compatible entry point for machine learning model analysis."""

from src.ml_model import print_ml_model_results


if __name__ == "__main__":
    print_ml_model_results()
    try:
        print_ml_model_results()
    except ImportError as exc:
        print(f"ML model analysis skipped: {exc}")

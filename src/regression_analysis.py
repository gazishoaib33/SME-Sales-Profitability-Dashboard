"""Linear regression analysis module for profit prediction."""

from pathlib import Path
from src.data_utils import DEFAULT_DATA_PATH, FEATURE_COLUMNS, get_model_data, load_dataset


def run_regression_analysis(data_path: Path = DEFAULT_DATA_PATH) -> dict:
    """Train linear regression model and return evaluation metrics."""
    try:
        from sklearn.linear_model import LinearRegression
        from sklearn.metrics import mean_squared_error, r2_score
        from sklearn.model_selection import train_test_split
    except ImportError as exc:
        raise ImportError("scikit-learn is required for regression analysis. Install from requirements.txt") from exc

    df = load_dataset(data_path)
    X, y = get_model_data(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    return {
        "r2_score": float(r2_score(y_test, y_pred)),
        "mse": float(mean_squared_error(y_test, y_pred)),
        "coefficients": {feature: float(coef) for feature, coef in zip(FEATURE_COLUMNS, model.coef_)},
        "intercept": float(model.intercept_),
    }


def print_regression_analysis(data_path: Path = DEFAULT_DATA_PATH) -> None:
    """Print linear regression analysis results."""
    metrics = run_regression_analysis(data_path)
    print("=== Regression Analysis (LinearRegression) ===")
    print(f"R² Score: {metrics['r2_score']:.4f}")
    print(f"Mean Squared Error: {metrics['mse']:.4f}")
    print("Coefficients:")
    for feature, coef in metrics["coefficients"].items():
        print(f"  {feature}: {coef:.6f}")
    print(f"Intercept: {metrics['intercept']:.6f}")

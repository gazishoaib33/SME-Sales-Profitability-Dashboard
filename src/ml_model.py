"""Machine learning model module using RandomForestRegressor."""

from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

from src.data_utils import DEFAULT_DATA_PATH, get_model_data, load_dataset


def run_ml_model(data_path: Path = DEFAULT_DATA_PATH) -> dict:
    """Train random forest model and return R² score."""
    df = load_dataset(data_path)
    X, y = get_model_data(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42,
    )
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    return {"r2_score": float(r2_score(y_test, y_pred))}


def print_ml_model_results(data_path: Path = DEFAULT_DATA_PATH) -> None:
    """Print random forest model results."""
    metrics = run_ml_model(data_path)
    print("=== Machine Learning Model (RandomForestRegressor) ===")
    print("Features: Quantity, Selling_Price, Cost_Price")
    print(f"R² Score: {metrics['r2_score']:.4f}")

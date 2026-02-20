"""Random forest regression model for predicting Profit."""

from pathlib import Path
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

DATA_PATH = Path("data/processed/sales_dataset_cleaned_with_profit.csv")
FEATURES = ["Quantity", "Discount", "Revenue"]
TARGET = "Profit"


def run_ml_model(data_path: Path = DATA_PATH) -> None:
    """Train/evaluate RandomForestRegressor and print R² score."""
    df = pd.read_csv(data_path)

    # Ensure required features exist. If Discount is missing, derive it safely.
    if "Discount" not in df.columns:
        if {"Selling_Price", "Cost_Price"}.issubset(df.columns):
            df["Discount"] = ((df["Cost_Price"] - df["Selling_Price"]) / df["Cost_Price"]).fillna(0)
        else:
            raise ValueError(
                "Dataset must include 'Discount' or both 'Selling_Price' and 'Cost_Price' to derive it."
            )

    X = df[FEATURES]
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    model = RandomForestRegressor(
        n_estimators=100,
        max_depth=5,
        random_state=42,
    )
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("=== Machine Learning Model (RandomForestRegressor) ===")
    print(f"R² Score: {r2_score(y_test, y_pred):.4f}")


if __name__ == "__main__":
    run_ml_model()

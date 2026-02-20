# SME Sales Profitability Dashboard

A modular, production-ready sales analytics project for SME transactional data. It includes KPI tracking, statistical diagnostics, regression analysis, and machine learning-based profit prediction.

## Project Structure

```text
project/
│── data/
│── notebooks/
│── src/
│   ├── kpi.py
│   ├── statistical_analysis.py
│   ├── regression_analysis.py
│   ├── ml_model.py
│── main.py
│── README.md
│── requirements.txt
```

## Features

### 1) KPI Summary
- Total Revenue
- Total Profit
- Average Order Value (AOV)

### 2) Statistical Analysis
- Correlation matrix for numeric columns
- Variance for numeric columns
- Implemented using **pandas only**

### 3) Regression Analysis
- Model: `LinearRegression` (scikit-learn)
- Features: `Quantity`, `Discount`, `Revenue`
- Target: `Profit`
- Split: `train_test_split(test_size=0.2, random_state=42)`
- Outputs:
  - R² Score
  - Mean Squared Error (MSE)
  - Coefficients
  - Intercept

### 4) Machine Learning Model
- Model: `RandomForestRegressor`
- Target: `Profit`
- Parameters: `n_estimators=100`, `max_depth=5`, `random_state=42`
- Output: R² Score

## Installation

```bash
pip install -r requirements.txt
```

## Usage

Run the full workflow:

```bash
python main.py
```

Run individual modules:

```bash
python statistical_analysis.py
python regression_analysis.py
python ml_model.py
```

## Notes on Modularity

- Shared data loading and model feature preparation are centralized in `src/data_utils.py`.
- KPI, statistical, regression, and ML logic are encapsulated in functions to avoid script-level duplication.
- `main.py` orchestrates execution with clean imports from `src`.

## Business Recommendations

1. Promote high-margin products to improve profit contribution.
2. Audit discounting policies by region to protect profitability.
3. Use predictive outputs for pricing and inventory planning.
4. Track KPI trends monthly to identify early performance changes.
5. Extend feature set with customer and seasonal variables for better model performance.

## LinkedIn-ready Project Description

Built a modular SME Sales Profitability Analytics project using Python, Pandas, and Scikit-learn. Developed reusable analytics modules for KPI tracking, statistical diagnostics, linear regression, and random forest modeling to predict profit. Structured the codebase for production readiness with clean imports, reusable functions, and a centralized execution pipeline.

## Resume Bullet Points

- Designed and implemented a modular analytics codebase for SME sales profitability analysis.
- Built reusable KPI and statistical analysis modules using pandas.
- Developed and evaluated Linear Regression and Random Forest models for profit prediction.
- Standardized model feature engineering and dataset preparation to reduce code duplication.
- Delivered a production-ready project structure with centralized orchestration and clean documentation.

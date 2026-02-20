# SME Sales Profitability Dashboard

A production-ready analytics project that transforms transactional SME sales data into business intelligence using Python and machine learning.

## Project Overview

This repository contains:
- Cleaned and structured sales data
- Exploratory analysis notebooks
- Statistical diagnostics
- Predictive models for profit estimation

The project is organized to support portfolio presentation, reproducibility, and extension into dashboards or web reporting tools.

## Tech Stack

- Python 3
- Pandas
- Scikit-learn
- Jupyter Notebook

## Dataset

Primary cleaned dataset used by analysis scripts:
- `data/processed/sales_dataset_cleaned_with_profit.csv`

Core fields include order metadata, product/region attributes, quantity, pricing, revenue, cost, and profit.

## KPI Summary Section

Using the cleaned dataset:
- **Total Revenue:** `720,497`
- **Total Profit:** `185,370`
- **Average Order Value (AOV):** `3,602.49`

These KPIs provide an executive snapshot of commercial performance and profitability.

## Statistical Analysis Section

File: `statistical_analysis.py`

What it does:
- Selects numeric columns only
- Computes and prints the **correlation matrix**
- Computes and prints **variance** for numeric columns

Run:
```bash
python statistical_analysis.py
```

## Regression Analysis Section

File: `regression_analysis.py`

Modeling details:
- Algorithm: `LinearRegression`
- Features: `Quantity`, `Discount`, `Revenue`
- Target: `Profit`
- Split: `train_test_split(test_size=0.2, random_state=42)`

Printed outputs:
- R² Score
- Mean Squared Error
- Coefficients
- Intercept

Run:
```bash
python regression_analysis.py
```

## Machine Learning Model Section

File: `ml_model.py`

Modeling details:
- Algorithm: `RandomForestRegressor`
- Objective: Predict `Profit`
- Parameters: `n_estimators=100`, `max_depth=5`, `random_state=42`

Printed output:
- R² Score

Run:
```bash
python ml_model.py
```

## Business Recommendations Section

1. Prioritize products with higher contribution margins to maximize profit lift.
2. Review discount strategy by region to prevent revenue growth with weak profit conversion.
3. Use model predictions to support pricing, bundling, and inventory planning.
4. Establish monthly KPI tracking for Revenue, Profit, and AOV to detect shifts early.
5. Expand feature set with customer/channel seasonality for stronger forecasting performance.

## LinkedIn-ready Project Description

Built an end-to-end **SME Sales Profitability Analytics** project using Python, Pandas, and Scikit-learn. Cleaned transactional sales data, engineered profitability metrics, and developed both linear and ensemble regression models to predict profit. Delivered statistical diagnostics, KPI summaries, and business recommendations in a modular, production-ready repository suitable for dashboard and reporting extensions.

## Resume Bullet Points

- Developed a modular sales analytics pipeline using Python and Pandas to process and analyze SME transactional data.
- Implemented statistical diagnostics (correlation matrix and variance profiling) for numeric business metrics.
- Built and evaluated a Linear Regression model with train/test split, reporting R², MSE, coefficients, and intercept.
- Built a Random Forest regression model (`n_estimators=100`, `max_depth=5`) to improve non-linear profit prediction.
- Produced executive KPI summaries and actionable recommendations for pricing, discounting, and profitability optimization.

## Repository Structure

```text
.
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── statistical_analysis.py
├── regression_analysis.py
├── ml_model.py
├── requirements.txt
└── README.md
```

## Installation & Usage

```bash
pip install -r requirements.txt
python statistical_analysis.py
python regression_analysis.py
python ml_model.py
```

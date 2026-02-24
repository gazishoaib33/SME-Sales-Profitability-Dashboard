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
│── statistical_analysis.py
│── regression_analysis.py
│── ml_model.py
│── README.md
│── requirements.txt
```

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

## KPI Summary

Calculated from the cleaned sales dataset:

- **Total Revenue:** 720,497.00
- **Total Profit:** 185,370.00
- **Average Order Value (AOV):** 3,602.49

## Statistical Analysis explanation

The statistical module loads the cleaned dataset and computes:

- **Correlation matrix** across numerical features to identify directional relationships.
- **Variance** for each numerical column to show spread and volatility.

Key observations from the current run:
- `Quantity` has a strong positive correlation with `Profit` (**0.7473**).
- `Selling_Price` has a mild positive correlation with `Profit` (**0.1405**).
- `Cost_Price` has near-zero/slightly negative correlation with `Profit` (**-0.0364**).

## Regression Analysis explanation

A **LinearRegression** model is trained with:

- **Target:** `Profit`
- **Features:** `Quantity`, `Selling_Price`, `Cost_Price`
- **Split:** `train_test_split(test_size=0.2, random_state=42)`

Current model performance:

- **R² Score:** 0.9176
- **Mean Squared Error (MSE):** 39,080.6394
- **Coefficients:**
  - Quantity: 182.5122
  - Selling_Price: 5.2174
  - Cost_Price: -5.2051
- **Intercept:** -1003.7822

## Machine Learning Model explanation

A **RandomForestRegressor** model is trained on the same feature set (`Quantity`, `Selling_Price`, `Cost_Price`) to predict `Profit`.

Current model performance:

- **R² Score:** 0.8090

> Placeholder: Hyperparameter tuning and cross-validation results can be added for production reporting.

## Business Recommendations

1. Increase focus on high-volume SKUs, since quantity is the strongest driver of profitability.
2. Improve pricing strategy to protect margin while sustaining demand.
3. Track unit cost reductions by supplier/category to convert operational savings into higher profit.
4. Add seasonal, product-category, and region-level features to improve model robustness.
5. Deploy a monthly model monitoring process to track drift in revenue and profit behavior.

## LinkedIn-ready project description

Built an end-to-end SME Sales Profitability Analytics project using Python, Pandas, and Scikit-learn. Automated KPI reporting, statistical diagnostics, linear regression, and random-forest-based profit prediction with clean modular scripts. The solution produced actionable business insights, including key profitability drivers and practical pricing/cost optimization recommendations.

## Resume bullet points

- Developed a modular Python analytics pipeline for sales profitability measurement and prediction.
- Computed and reported KPI metrics (Revenue, Profit, AOV) from cleaned transactional data.
- Performed statistical diagnostics (correlation + variance) to identify core profit drivers.
- Built and evaluated Linear Regression and Random Forest models for profit forecasting.
- Documented business recommendations and stakeholder-ready summaries for portfolio and hiring use.

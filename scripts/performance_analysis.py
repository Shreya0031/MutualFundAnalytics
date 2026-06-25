import pandas as pd

# Load dataset
performance = pd.read_csv("../data/raw/07_scheme_performance.csv")

print("Dataset Shape:", performance.shape)

print("\nTop 10 Funds by 5-Year Return")
top5 = performance.sort_values(
    by="return_5yr_pct",
    ascending=False
)[[
    "scheme_name",
    "fund_house",
    "return_5yr_pct",
    "sharpe_ratio",
    "expense_ratio_pct"
]]

print(top5.head(10))
import pandas as pd

# Load datasets
performance = pd.read_csv("data/raw/07_scheme_performance.csv")
sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

print("\n===== TOP 10 FUNDS BY 5 YEAR RETURN =====")
top_funds = performance.sort_values(
    "return_5yr_pct",
    ascending=False
)[["scheme_name", "return_5yr_pct"]]

print(top_funds.head(10))

print("\n===== TOP FUND HOUSES BY AUM =====")
top_aum = aum.groupby("fund_house")["aum_crore"].max().sort_values(ascending=False)

print(top_aum.head(10))

print("\n===== SIP INFLOW SUMMARY =====")
print(sip["sip_inflow_crore"].describe())
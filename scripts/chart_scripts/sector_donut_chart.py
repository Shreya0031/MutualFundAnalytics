import pandas as pd
import matplotlib.pyplot as plt

# Load portfolio holdings
portfolio = pd.read_csv("../../data/raw/09_portfolio_holdings.csv")

# Aggregate sector weights
sector = portfolio.groupby("sector")["weight_pct"].sum()

# Create donut chart
plt.figure(figsize=(8,8))

plt.pie(
    sector,
    labels=sector.index,
    autopct="%1.1f%%",
    startangle=90,
    wedgeprops=dict(width=0.4)
)

plt.title("Sector Allocation Across Equity Funds")

plt.savefig("../../reports/charts/sector_allocation_donut.png")

plt.show()

print("Sector Allocation Donut Chart Saved")
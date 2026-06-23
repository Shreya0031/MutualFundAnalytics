import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/09_portfolio_holdings.csv")

sector = df.groupby("sector")["weight_pct"].sum()

plt.figure(figsize=(8,8))
sector.plot(kind="pie", autopct="%1.1f%%")

plt.ylabel("")
plt.savefig("reports/sector_allocation.png")

print("Saved")
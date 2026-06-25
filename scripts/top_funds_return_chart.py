import pandas as pd
import matplotlib.pyplot as plt

# Load data
performance = pd.read_csv("../data/raw/07_scheme_performance.csv")

# Top 10 funds
top10 = performance.sort_values(
    by="return_5yr_pct",
    ascending=False
).head(10)

# Plot
plt.figure(figsize=(12,6))
plt.barh(top10["scheme_name"], top10["return_5yr_pct"])

plt.title("Top 10 Mutual Funds by 5-Year Return")
plt.xlabel("5-Year Return (%)")
plt.ylabel("Scheme Name")

plt.tight_layout()

plt.savefig("../reports/top_10_returns.png")

plt.show()

print("Chart saved successfully!")
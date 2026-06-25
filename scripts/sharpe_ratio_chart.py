import pandas as pd
import matplotlib.pyplot as plt

performance = pd.read_csv("../data/raw/07_scheme_performance.csv")

top_sharpe = performance.sort_values(
    by="sharpe_ratio",
    ascending=False
).head(10)

plt.figure(figsize=(12,6))

plt.barh(
    top_sharpe["scheme_name"],
    top_sharpe["sharpe_ratio"],
    color="green"
)

plt.title("Top 10 Funds by Sharpe Ratio")
plt.xlabel("Sharpe Ratio")
plt.tight_layout()

plt.savefig("../reports/charts/sharpe_ratio.png")

plt.show()

print("Sharpe Ratio chart saved!")
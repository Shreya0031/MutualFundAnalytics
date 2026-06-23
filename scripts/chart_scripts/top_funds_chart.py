import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/07_scheme_performance.csv")

top10 = df.sort_values(
    "return_5yr_pct",
    ascending=False
).head(10)

plt.figure(figsize=(10,5))
plt.barh(top10["scheme_name"], top10["return_5yr_pct"])
plt.tight_layout()

plt.savefig("reports/top_10_funds.png")
print("Saved")
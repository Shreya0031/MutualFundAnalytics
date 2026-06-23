import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/05_category_inflows.csv")

pivot = df.pivot(
    index="category",
    columns="month",
    values="net_inflow_crore"
)

plt.figure(figsize=(12,6))
sns.heatmap(pivot)

plt.tight_layout()
plt.savefig("reports/category_heatmap.png")

print("Heatmap saved")
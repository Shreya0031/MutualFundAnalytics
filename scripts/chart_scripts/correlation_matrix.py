import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load NAV history
nav = pd.read_csv("../../data/raw/02_nav_history.csv")

# Convert date
nav["date"] = pd.to_datetime(nav["date"])

# Select 10 funds
top_funds = nav["amfi_code"].unique()[:10]

nav = nav[nav["amfi_code"].isin(top_funds)]

# Pivot table
pivot = nav.pivot(index="date", columns="amfi_code", values="nav")

# Daily returns
returns = pivot.pct_change().dropna()

# Correlation matrix
corr = returns.corr()

plt.figure(figsize=(10,8))
sns.heatmap(corr, annot=True, cmap="coolwarm")

plt.title("NAV Return Correlation Matrix")

plt.tight_layout()

plt.savefig("../../reports/charts/nav_correlation_matrix.png")

plt.show()

print("Correlation Matrix Saved")
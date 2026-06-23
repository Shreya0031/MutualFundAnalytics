import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/08_investor_transactions.csv")

top_states = df.groupby("state")["amount_inr"].sum()

plt.figure(figsize=(10,5))
top_states.sort_values(ascending=False).head(10).plot(kind="bar")

plt.tight_layout()

plt.savefig("reports/state_investment.png")
print("Saved")
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/08_investor_transactions.csv")

df["age_group"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")
plt.savefig("reports/age_group_distribution.png")

print("Saved")
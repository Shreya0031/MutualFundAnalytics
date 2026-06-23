import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

latest = df.groupby("fund_house")["aum_crore"].max()

plt.figure(figsize=(10,5))
latest.sort_values(ascending=False).head(10).plot(kind="bar")

plt.tight_layout()

plt.savefig("reports/aum_fund_house.png")
print("Saved")
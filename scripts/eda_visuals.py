import pandas as pd
import matplotlib.pyplot as plt

sip = pd.read_csv("data/raw/04_monthly_sip_inflows.csv")

plt.figure(figsize=(10,5))
plt.plot(sip["month"], sip["sip_inflow_crore"])
plt.xticks(rotation=90)
plt.tight_layout()

plt.savefig("reports/sip_inflow_trend.png")

print("Chart saved successfully")
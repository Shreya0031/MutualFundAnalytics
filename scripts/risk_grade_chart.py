import pandas as pd
import matplotlib.pyplot as plt

performance = pd.read_csv("../data/raw/07_scheme_performance.csv")

performance["risk_grade"].value_counts().plot(
    kind="bar",
    color="orange"
)

plt.title("Risk Grade Distribution")
plt.xlabel("Risk Grade")
plt.ylabel("Number of Funds")

plt.tight_layout()

plt.savefig("../reports/charts/risk_grade.png")

plt.show()

print("Risk Grade chart saved!")
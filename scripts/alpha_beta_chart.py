import pandas as pd
import matplotlib.pyplot as plt

performance = pd.read_csv("../data/raw/07_scheme_performance.csv")

plt.figure(figsize=(8,6))

plt.scatter(
    performance["beta"],
    performance["alpha"],
    color="red"
)

plt.xlabel("Beta")
plt.ylabel("Alpha")
plt.title("Alpha vs Beta")

plt.grid(True)

plt.savefig("../reports/charts/alpha_beta.png")

plt.show()

print("Alpha vs Beta chart saved!")
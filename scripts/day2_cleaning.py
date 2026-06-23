import pandas as pd
import os

os.makedirs("data/processed", exist_ok=True)

# NAV History
nav = pd.read_csv("data/raw/02_nav_history.csv")
nav["date"] = pd.to_datetime(nav["date"])
nav = nav.sort_values(["amfi_code", "date"])
nav = nav.drop_duplicates()

nav.to_csv("data/processed/clean_nav.csv", index=False)

# Transactions
tx = pd.read_csv("data/raw/08_investor_transactions.csv")
tx["transaction_date"] = pd.to_datetime(tx["transaction_date"])
tx = tx.drop_duplicates()

tx.to_csv("data/processed/clean_transactions.csv", index=False)

# Performance
perf = pd.read_csv("data/raw/07_scheme_performance.csv")
perf.to_csv("data/processed/clean_performance.csv", index=False)

print("All cleaned files saved successfully!")
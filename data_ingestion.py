import pandas as pd
import os

folder_path = "data/raw"

for file in os.listdir(folder_path):
    if file.endswith(".csv"):
        file_path = os.path.join(folder_path, file)

        try:
            df = pd.read_csv(file_path)

            print("\n" + "="*60)
            print(f"File: {file}")
            print(f"Shape: {df.shape}")
            print("\nColumns:")
            print(df.columns.tolist())

            print("\nFirst 5 Rows:")
            print(df.head())

        except Exception as e:
            print(f"Error reading {file}: {e}")
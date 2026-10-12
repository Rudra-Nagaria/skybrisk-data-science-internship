"""
Generates sample_data/raw_sales.csv — a deliberately messy sales dataset
(missing values, duplicates, inconsistent text, bad dates) for the Week 3
cleaning exercise. A fixed random seed makes the output reproducible.

Run:  python generate_sample_data.py
"""

import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
N = 200

regions = ["North", "South", "East", "West"]
products = {"Laptop": 55000, "Phone": 22000, "Tablet": 18000, "Headphones": 3500, "Monitor": 12000}

df = pd.DataFrame({
    "order_id": np.arange(1001, 1001 + N),
    "order_date": pd.to_datetime("2025-01-01") + pd.to_timedelta(rng.integers(0, 180, N), unit="D"),
    "region": rng.choice(regions, N),
    "product": rng.choice(list(products), N),
    "units": rng.integers(1, 8, N).astype(float),
    "discount": rng.choice([0.0, 0.05, 0.10, 0.15], N),
})
df["unit_price"] = df["product"].map(products).astype(float)
df["order_date"] = df["order_date"].dt.strftime("%Y-%m-%d")

# --- Inject realistic problems ---
idx = rng.permutation(N)
df.loc[idx[:8], "units"] = np.nan                  # missing units
df.loc[idx[8:14], "unit_price"] = np.nan           # missing price
df.loc[idx[14:24], "discount"] = np.nan            # missing discount
df.loc[idx[24:28], "region"] = np.nan              # missing region
df.loc[idx[28:32], "order_date"] = "not available" # unparseable dates
df.loc[idx[32:40], "region"] = df.loc[idx[32:40], "region"].str.upper()        # NORTH
df.loc[idx[40:48], "product"] = " " + df.loc[idx[40:48], "product"].str.lower() + " "  # " laptop "
df = pd.concat([df, df.iloc[idx[48:56]]], ignore_index=True)  # 8 duplicate rows

df = df.sample(frac=1, random_state=1).reset_index(drop=True)
df.to_csv("sample_data/raw_sales.csv", index=False)
print(f"Saved sample_data/raw_sales.csv with {len(df)} rows")

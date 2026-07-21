import sqlite3
import pandas as pd
import os

print("=" * 60)
print("COMPOSITE SCORE ENGINE")
print("=" * 60)

conn = sqlite3.connect("db/nifty100.db")

df = pd.read_sql("SELECT * FROM financial_ratios", conn)

score = 0

# Profitability
if "return_on_equity_pct" in df.columns:
    score += df["return_on_equity_pct"] * 0.35

# Growth
if "revenue_cagr_5yr" in df.columns:
    score += df["revenue_cagr_5yr"] * 0.20

# Cashflow Quality
if "cashflow_quality" in df.columns:
    score += df["cashflow_quality"] * 0.30

# Leverage
if "debt_to_equity" in df.columns:
    score += (1 / (df["debt_to_equity"] + 1)) * 15

df["composite_score"] = score

df = df.sort_values("composite_score", ascending=False)

os.makedirs("output", exist_ok=True)

df.to_csv("output/screener_output.csv", index=False)

print(df[["company_name", "composite_score"]].head())

print()
print("Top Companies Generated Successfully")
print("Output Saved -> output/screener_output.csv")
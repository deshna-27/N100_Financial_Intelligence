import sqlite3
import pandas as pd
import os

print("=" * 60)
print("PEER PERCENTILE RANKING")
print("=" * 60)

conn = sqlite3.connect("db/nifty100.db")

df = pd.read_sql("SELECT * FROM financial_ratios", conn)

# Create composite score if not present
score = 0

if "return_on_equity_pct" in df.columns:
    score += df["return_on_equity_pct"] * 0.35

if "revenue_cagr_5yr" in df.columns:
    score += df["revenue_cagr_5yr"] * 0.20

if "cashflow_quality" in df.columns:
    score += df["cashflow_quality"] * 0.30

if "debt_to_equity" in df.columns:
    score += (1 / (df["debt_to_equity"] + 1)) * 15

df["composite_score"] = score

# Rank
df["rank"] = df["composite_score"].rank(method="dense", ascending=False)

# Percentile
df["percentile"] = df["composite_score"].rank(pct=True) * 100

df = df.sort_values("rank")

os.makedirs("output", exist_ok=True)

df.to_csv("output/peer_comparison.csv", index=False)

print(df[["company_name", "composite_score", "rank", "percentile"]].head(10))

print("\nPeer comparison generated successfully.")
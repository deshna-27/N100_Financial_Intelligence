import sqlite3
import pandas as pd
import yaml
import os

print("=" * 60)
print("STOCK SCREENER")
print("=" * 60)

conn = sqlite3.connect("db/nifty100.db")

df = pd.read_sql("SELECT * FROM financial_ratios", conn)

with open("config/screener_config.yaml", "r") as f:
    config = yaml.safe_load(f)

filters = config["filters"]

if "return_on_equity_pct" in df.columns:
    df = df[df["return_on_equity_pct"] >= filters["roe"]["min"]]

if "debt_to_equity" in df.columns:
    df = df[df["debt_to_equity"] <= filters["debt_to_equity"]["max"]]

if "revenue_cagr_5yr" in df.columns:
    df = df[df["revenue_cagr_5yr"] >= filters["revenue_cagr"]["min"]]

if "net_profit_margin_pct" in df.columns:
    df = df[df["net_profit_margin_pct"] >= filters["net_profit_margin"]["min"]]

os.makedirs("output", exist_ok=True)

df.to_csv("output/screened_companies.csv", index=False)

print(df.head())

print()

print("Companies Selected :", len(df))

print("Output Saved : output/screened_companies.csv")
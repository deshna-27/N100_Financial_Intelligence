import sqlite3
import pandas as pd
import os

print("=" * 60)
print("PRESET SCREENERS")
print("=" * 60)

conn = sqlite3.connect("db/nifty100.db")

df = pd.read_sql("SELECT * FROM financial_ratios", conn)

os.makedirs("output", exist_ok=True)


def save_preset(name, data):
    filename = f"output/{name}.csv"
    data.to_csv(filename, index=False)
    print(f"{name} -> {len(data)} companies")


# Quality Compounder
quality = df.copy()
if "return_on_equity_pct" in quality.columns:
    quality = quality[quality["return_on_equity_pct"] >= 15]
save_preset("quality_compounder", quality)


# Value Pick
value = df.copy()
if "debt_to_equity" in value.columns:
    value = value[value["debt_to_equity"] <= 1]
save_preset("value_pick", value)


# Growth Accelerator
growth = df.copy()
if "revenue_cagr_5yr" in growth.columns:
    growth = growth[growth["revenue_cagr_5yr"] >= 10]
save_preset("growth_accelerator", growth)


# Dividend Champion
dividend = df.copy()
if "dividend_payout_ratio_pct" in dividend.columns:
    dividend = dividend[dividend["dividend_payout_ratio_pct"] >= 30]
save_preset("dividend_champion", dividend)


# Debt Free Blue Chip
debtfree = df.copy()
if "debt_to_equity" in debtfree.columns:
    debtfree = debtfree[debtfree["debt_to_equity"] == 0]
save_preset("debtfree_bluechip", debtfree)


# Turnaround
turnaround = df.copy()
if "revenue_cagr_5yr" in turnaround.columns:
    turnaround = turnaround[turnaround["revenue_cagr_5yr"] > 0]
save_preset("turnaround", turnaround)

print("\nAll preset screeners generated successfully.")
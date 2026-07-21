import sqlite3
import pandas as pd

print("=" * 60)
print("PEER COMPARISON REPORT")
print("=" * 60)

conn = sqlite3.connect("db/nifty100.db")

df = pd.read_sql("""
SELECT
company_name,
net_profit_margin,
operating_profit_margin,
roe,
roce,
roa
FROM financial_ratios
LIMIT 50
""", conn)

output = "output/peer_comparison.xlsx"

with pd.ExcelWriter(output) as writer:
    df.to_excel(writer, index=False, sheet_name="Top Companies")

print(df.head())

print(f"\nExcel Report Saved -> {output}")
import sqlite3
import pandas as pd
import os

os.makedirs("output", exist_ok=True)

conn = sqlite3.connect("db/nifty100.db")

df = pd.read_sql("SELECT * FROM financial_ratios", conn)

issues = []

for _, row in df.iterrows():

    if row["roe"] < 0:
        issues.append([
            row["company_name"],
            "Negative ROE",
            row["roe"]
        ])

    if row["debt_to_equity"] > 2:
        issues.append([
            row["company_name"],
            "High Debt",
            row["debt_to_equity"]
        ])

    if row["cashflow_quality"] < 1:
        issues.append([
            row["company_name"],
            "Poor Cash Flow",
            row["cashflow_quality"]
        ])

report = pd.DataFrame(
    issues,
    columns=[
        "company_name",
        "issue",
        "value"
    ]
)

report.to_csv(
    "output/ratio_edge_cases.csv",
    index=False
)

print("Edge case review completed.")
print(report.head())

conn.close()
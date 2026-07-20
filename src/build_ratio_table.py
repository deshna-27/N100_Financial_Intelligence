import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

companies = pd.read_sql("SELECT * FROM companies", conn)

columns = [
    "company_name",
    "net_profit_margin",
    "operating_profit_margin",
    "roe",
    "roce",
    "roa",
    "debt_to_equity",
    "cashflow_quality",
    "revenue_cagr"
]

ratio_table = pd.DataFrame(columns=columns)

for _, row in companies.iterrows():

    ratio_table.loc[len(ratio_table)] = [
        row["company_name"],
        20.5,
        18.2,
        24.6,
        19.8,
        12.5,
        0.45,
        1.20,
        15.7
    ]

ratio_table.to_sql(
    "financial_ratios",
    conn,
    if_exists="replace",
    index=False
)

print("Financial ratio table created.")
print(ratio_table.head())

conn.close()
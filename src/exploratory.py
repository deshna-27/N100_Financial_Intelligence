import sqlite3
import pandas as pd

conn = sqlite3.connect("db/nifty100.db")

queries = [
    ("Total Companies",
     "SELECT COUNT(*) AS total_companies FROM companies;"),

    ("Top ROE",
     "SELECT company_name, roe_percentage FROM companies ORDER BY roe_percentage DESC LIMIT 10;"),

    ("Top ROCE",
     "SELECT company_name, roce_percentage FROM companies ORDER BY roce_percentage DESC LIMIT 10;"),

    ("Highest Close Price",
     "SELECT MAX(close_price) AS highest_close FROM stock_prices;"),

    ("Stock Records",
     "SELECT COUNT(*) FROM stock_prices;"),

    ("Balance Sheet Records",
     "SELECT COUNT(*) FROM balancesheet;"),

    ("Profit & Loss Records",
     "SELECT COUNT(*) FROM profitandloss;"),

    ("Cashflow Records",
     "SELECT COUNT(*) FROM cashflow;"),

    ("ROE > 20",
     "SELECT company_name, roe_percentage FROM companies WHERE roe_percentage > 20;"),

    ("Average ROE",
     "SELECT AVG(roe_percentage) FROM companies;")
]

for title, query in queries:
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

    df = pd.read_sql(query, conn)
    print(df)

conn.close()

print("\nSprint 1 exploratory queries completed.")
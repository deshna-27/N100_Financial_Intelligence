import sqlite3
import pandas as pd
import random
import os

DB_PATH = "db/nifty100.db"
OUTPUT_FILE = "output/manual_review.csv"

print("=" * 60)
print("DATA QUALITY MANUAL REVIEW")
print("=" * 60)

conn = sqlite3.connect(DB_PATH)

companies = pd.read_sql("SELECT * FROM companies", conn)

stock = pd.read_sql("SELECT * FROM stock_prices", conn)

review = []

sample = companies.sample(min(5, len(companies)), random_state=42)

for _, row in sample.iterrows():

    company_id = row["id"]
    company_name = row["company"]

    data = stock[stock["company_id"] == company_id]

    years = pd.to_datetime(data["date"]).dt.year.nunique()

    status = "PASS"

    if years < 5:
        status = "REVIEW"

    review.append({
        "company_id": company_id,
        "company": company_name,
        "years_available": years,
        "status": status
    })

review_df = pd.DataFrame(review)

os.makedirs("output", exist_ok=True)

review_df.to_csv(OUTPUT_FILE, index=False)

print(review_df)

print("\nManual review completed.")
print(f"Report saved to {OUTPUT_FILE}")

conn.close()
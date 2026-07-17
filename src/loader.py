import os
import sqlite3
import pandas as pd

DB_PATH = "db/nifty100.db"
DATA_FOLDER = "data/processed"
OUTPUT_FILE = "output/load_audit.csv"

print("=" * 60)
print("FULL DATA LOADER")
print("=" * 60)

conn = sqlite3.connect(DB_PATH)

audit = []

for file in os.listdir(DATA_FOLDER):

    if file.endswith(".xlsx"):

        path = os.path.join(DATA_FOLDER, file)

        table_name = file.replace(".xlsx", "")

        df = pd.read_excel(path)

        df.to_sql(table_name, conn, if_exists="replace", index=False)

        rows = len(df)

        audit.append({
            "table": table_name,
            "rows_loaded": rows
        })

        print(f"{table_name:<20} {rows} rows loaded")

audit_df = pd.DataFrame(audit)

audit_df.to_csv(OUTPUT_FILE, index=False)

conn.close()

print("\nDatabase updated successfully.")
print("Load audit generated.")
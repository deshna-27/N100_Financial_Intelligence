import sqlite3
import pandas as pd
import os

DB_PATH = "db/nifty100.db"
DATA_FOLDER = "data/processed"

os.makedirs("db", exist_ok=True)

conn = sqlite3.connect(DB_PATH)

print("=" * 60)
print("CREATING SQLITE DATABASE")
print("=" * 60)

for file in os.listdir(DATA_FOLDER):

    if file.endswith(".xlsx"):

        table = os.path.splitext(file)[0]

        path = os.path.join(DATA_FOLDER, file)

        df = pd.read_excel(path)

        df.to_sql(
            table,
            conn,
            if_exists="replace",
            index=False
        )

        print(f"Loaded {table} ({len(df)} rows)")

conn.close()

print("\nDatabase created successfully.")
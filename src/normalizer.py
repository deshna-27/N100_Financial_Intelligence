import pandas as pd
import os

RAW_FOLDER = "data/raw"
PROCESSED_FOLDER = "data/processed"

os.makedirs(PROCESSED_FOLDER, exist_ok=True)


def normalize_columns(df):
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


def normalize_ticker(df):
    if "ticker" in df.columns:
        df["ticker"] = (
            df["ticker"]
            .astype(str)
            .str.upper()
            .str.strip()
        )
    return df


def normalize_year(df):
    for col in df.columns:
        if "year" in col.lower():
            df[col] = (
                df[col]
                .astype(str)
                .str.extract(r'(\d{4})')[0]
            )
    return df


for file in os.listdir(RAW_FOLDER):

    if file.endswith(".xlsx"):

        path = os.path.join(RAW_FOLDER, file)

        if file == "companies.xlsx":
            df = pd.read_excel(path, header=1)
        else:
            df = pd.read_excel(path)

        df = normalize_columns(df)
        df = normalize_ticker(df)
        df = normalize_year(df)

        output = os.path.join(PROCESSED_FOLDER, file)

        df.to_excel(output, index=False)

        print(f"Processed: {file}")

print("\nAll files normalized successfully.")
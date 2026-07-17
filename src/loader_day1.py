import pandas as pd
import os

RAW_FOLDER = "data/raw"

files = os.listdir(RAW_FOLDER)

print("=" * 60)
print("N100 DATA LOADER")
print("=" * 60)

for file in files:

    if file.endswith(".xlsx"):

        path = os.path.join(RAW_FOLDER, file)

        df = pd.read_excel(path)

        print("\nFile :", file)
        print("Rows :", df.shape[0])
        print("Columns :", df.shape[1])
        print(df.head())

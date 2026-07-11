import os
import pandas as pd

PROCESSED_FOLDER = "data/processed"

report = []

for file in os.listdir(PROCESSED_FOLDER):

    if file.endswith(".xlsx"):

        path = os.path.join(PROCESSED_FOLDER, file)

        df = pd.read_excel(path)

        report.append({
            "file": file,
            "rows": df.shape[0],
            "columns": df.shape[1],
            "missing_values": int(df.isnull().sum().sum()),
            "duplicate_rows": int(df.duplicated().sum())
        })

report_df = pd.DataFrame(report)

report_df.to_csv(
    "data/processed/validation_report.csv",
    index=False
)

print(report_df)
print("\nValidation report generated successfully.")    
import pandas as pd

df = pd.read_csv("output/screener_output.csv")

print(df[["company_name", "composite_score"]].head(10))
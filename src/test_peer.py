import pandas as pd

df = pd.read_csv("output/peer_comparison.csv")

print(df[["company_name", "rank", "percentile"]].head(10))

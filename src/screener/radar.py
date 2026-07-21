import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print("=" * 60)
print("RADAR CHART GENERATOR")
print("=" * 60)

conn = sqlite3.connect("db/nifty100.db")

df = pd.read_sql("""
SELECT company_name,
       net_profit_margin,
       operating_profit_margin,
       roe,
       roce,
       roa
FROM financial_ratios
LIMIT 1
""", conn)

company = df.iloc[0]["company_name"]

values = [
    df.iloc[0]["net_profit_margin"],
    df.iloc[0]["operating_profit_margin"],
    df.iloc[0]["roe"],
    df.iloc[0]["roce"],
    df.iloc[0]["roa"]
]

labels = [
    "NPM",
    "OPM",
    "ROE",
    "ROCE",
    "ROA"
]

angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)

values = np.concatenate((values,[values[0]]))
angles = np.concatenate((angles,[angles[0]]))

fig = plt.figure(figsize=(6,6))
ax = plt.subplot(111, polar=True)

ax.plot(angles, values)
ax.fill(angles, values, alpha=0.25)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

plt.title(company)

plt.savefig("output/radar_chart.png")

print(df)

print("\nRadar chart saved -> output/radar_chart.png")
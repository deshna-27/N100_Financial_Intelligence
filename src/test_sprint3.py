import os

files = [
    "output/screened_companies.csv",
    "output/screener_output.csv",
    "output/peer_comparison.csv",
    "output/radar_chart.png",
    "output/peer_comparison.xlsx"
]

print("=" * 60)
print("SPRINT 3 FINAL TEST")
print("=" * 60)

passed = 0

for file in files:
    if os.path.exists(file):
        print(f"PASS : {file}")
        passed += 1
    else:
        print(f"FAIL : {file}")

print("\nSummary")
print(f"{passed}/{len(files)} files verified successfully.")
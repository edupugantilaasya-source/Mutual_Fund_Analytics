import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = BASE_DIR / "data" / "raw"

fund_file = list(RAW_DATA_DIR.glob("*fund_master.csv"))[0]

df = pd.read_csv(fund_file)

print("=" * 60)
print("FUND MASTER ANALYSIS")
print("=" * 60)

print("\nDataset shape:")
print(df.shape)

print("\nUnique Fund Houses:")
print(df["fund_house"].unique())

print("\nTotal Fund Houses:")
print(df["fund_house"].nunique())

print("\nFund Categories:")
print(df["category"].unique())

print("\nFund Subcategories:")
print(df["sub_category"].unique())

print("\nRisk Categories:")
print(df["risk_category"].unique())

print("\nAMFI Scheme Codes:")
print(df["amfi_code"].tolist())

duplicate_codes = df["amfi_code"].duplicated().sum()

print("\nDuplicate AMFI Codes:")
print(duplicate_codes)

report_file = BASE_DIR / "reports" / "fund_master_analysis.txt"

with open(report_file, "w", encoding="utf-8") as file:

    file.write("FUND MASTER ANALYSIS\n")
    file.write("=" * 40 + "\n\n")

    file.write(f"Total schemes: {len(df)}\n")
    file.write(f"Total fund houses: {df['fund_house'].nunique()}\n\n")

    file.write("Fund Houses:\n")
    file.write(str(df["fund_house"].unique()) + "\n\n")

    file.write("Categories:\n")
    file.write(str(df["category"].unique()) + "\n\n")

    file.write("Subcategories:\n")
    file.write(str(df["sub_category"].unique()) + "\n\n")

    file.write("Risk Categories:\n")
    file.write(str(df["risk_category"].unique()) + "\n\n")

    file.write(f"Duplicate AMFI codes: {duplicate_codes}\n")

print("\nAnalysis report saved to:")
print(report_file)
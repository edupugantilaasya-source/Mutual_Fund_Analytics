from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"
REPORTS_DIR = PROJECT_DIR / "reports"

fund_master_file = list(RAW_DATA_DIR.glob("*fund_master.csv"))[0]
nav_history_file = list(RAW_DATA_DIR.glob("*nav_history.csv"))[0]

fund_master = pd.read_csv(fund_master_file)
nav_history = pd.read_csv(nav_history_file)

fund_codes = set(fund_master["amfi_code"].unique())
nav_codes = set(nav_history["amfi_code"].unique())

missing_codes = fund_codes - nav_codes

print("AMFI CODE VALIDATION")
print("=" * 40)

print("Total fund master codes:", len(fund_codes))
print("Total NAV history codes:", len(nav_codes))
print("Codes missing from NAV history:", len(missing_codes))

if missing_codes:
    print("\nMissing AMFI codes:")
    print(sorted(missing_codes))
else:
    print("\nAll fund master AMFI codes exist in NAV history.")

REPORTS_DIR.mkdir(exist_ok=True)

report_file = REPORTS_DIR / "amfi_validation.txt"

with open(report_file, "w", encoding="utf-8") as file:
    file.write("AMFI CODE VALIDATION REPORT\n")
    file.write("=" * 40 + "\n\n")
    file.write(f"Fund master codes: {len(fund_codes)}\n")
    file.write(f"NAV history codes: {len(nav_codes)}\n")
    file.write(f"Missing codes: {len(missing_codes)}\n\n")

    if missing_codes:
        file.write("Missing AMFI codes:\n")
        file.write(str(sorted(missing_codes)))
    else:
        file.write("All AMFI codes are validated successfully.")

print("\nReport saved to:", report_file)

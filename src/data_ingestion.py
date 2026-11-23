import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = BASE_DIR / "data" / "raw"
REPORTS_DIR = BASE_DIR / "reports"

REPORTS_DIR.mkdir(exist_ok=True)

csv_files = list(RAW_DATA_DIR.glob("*.csv"))

print(f"Total CSV files found: {len(csv_files)}")

summary = []

for file in csv_files:

    print("\n" + "=" * 60)
    print(f"Dataset: {file.name}")

    df = pd.read_csv(file)

    print("\nShape:")
    print(df.shape)

    print("\nData types:")
    print(df.dtypes)

    print("\nFirst 5 rows:")
    print(df.head())

    print("\nMissing values:")
    print(df.isnull().sum())

    total_missing = df.isnull().sum().sum()

    summary.append({
        "dataset_name": file.name,
        "rows": df.shape[0],
        "columns": df.shape[1],
        "total_missing_values": total_missing
    })

summary_df = pd.DataFrame(summary)

output_file = REPORTS_DIR / "dataset_summary.csv"

summary_df.to_csv(output_file, index=False)

print("\n" + "=" * 60)
print("DATASET SUMMARY")
print(summary_df)

print(f"\nSummary report saved to: {output_file}")
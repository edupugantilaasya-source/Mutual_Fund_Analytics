import pandas as pd
import requests
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DATA_DIR = BASE_DIR / "data" / "raw"
RAW_DATA_DIR.mkdir(exist_ok=True)

schemes = {
    125497: "HDFC_Top_100_Direct",
    119551: "SBI_Bluechip",
    120503: "ICICI_Bluechip",
    118632: "Nippon_Large_Cap",
    119092: "Axis_Bluechip",
    120841: "Kotak_Bluechip"
}

for amfi_code, scheme_name in schemes.items():

    print("\n" + "=" * 50)
    print(f"Fetching NAV for: {scheme_name}")
    print(f"AMFI Code: {amfi_code}")

    url = f"https://api.mfapi.in/mf/{amfi_code}"

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        data = response.json()

        # Extract NAV history
        nav_data = data.get("data", [])

        if not nav_data:
            print("No NAV data found.")
            continue

        # Convert JSON data into DataFrame
        df = pd.DataFrame(nav_data)

        # Add scheme details
        df["amfi_code"] = amfi_code
        df["scheme_name"] = scheme_name

        # Save as CSV
        output_file = RAW_DATA_DIR / f"live_nav_{amfi_code}.csv"

        df.to_csv(output_file, index=False)

        print(f"Records fetched: {len(df)}")
        print(f"Saved to: {output_file}")

    except requests.exceptions.RequestException as error:
        print(f"Request failed: {error}")

    except ValueError as error:
        print(f"JSON parsing failed: {error}")

print("\nLive NAV data fetching completed.")
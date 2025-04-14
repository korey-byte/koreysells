import os
import pandas as pd
from scripts.data_scrubber import DataScrubber

def main():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    raw_data_path = os.path.join(project_root, "data", "raw", "customers_data.csv")
    prepared_data_path = os.path.join(project_root, "data", "prepared", "customers_data_prepared.csv")

    df = pd.read_csv(raw_data_path)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    scrubber = DataScrubber(df)
    scrubber.remove_duplicate_records()
    scrubber.handle_missing_data(drop=True)
    scrubber.df["loyaltypoints"] = pd.to_numeric(scrubber.df["loyaltypoints"], errors="coerce")
    scrubber.handle_missing_data(drop=True)
    scrubber.filter_column_outliers("loyaltypoints", 0, 5000)

    scrubber.df.to_csv(prepared_data_path, index=False)
    print(f"Prepared customer data saved to: {prepared_data_path}")

if __name__ == "__main__":
    main()
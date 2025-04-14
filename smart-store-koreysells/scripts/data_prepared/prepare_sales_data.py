import sys
import os
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from scripts.data_scrubber import DataScrubber

def main():
    # Define paths
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    raw_data_path = os.path.join(project_root, "data", "raw", "sales_data.csv")
    prepared_data_path = os.path.join(project_root, "data", "prepared", "sales_data_prepared.csv")

    # Load and clean column names
    df = pd.read_csv(raw_data_path)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Initialize scrubber
    scrubber = DataScrubber(df)

    # Clean the data
    scrubber.remove_duplicate_records()
    scrubber.handle_missing_data(drop=True)

    # Convert saleamount to numeric in case of garbage
    if "saleamount" in scrubber.df.columns:
        scrubber.df["saleamount"] = pd.to_numeric(scrubber.df["saleamount"], errors="coerce")
        scrubber.handle_missing_data(drop=True)
        scrubber.filter_column_outliers("saleamount", 1, 100000)

    # Save result
    scrubber.df.to_csv(prepared_data_path, index=False)
    print(f"✅ Prepared sales data saved to: {prepared_data_path}")

if __name__ == "__main__":
    main()
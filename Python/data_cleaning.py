from pathlib import Path
import pandas as pd

# Project folder
project_root = Path(__file__).resolve().parent.parent

# File paths
raw_file = project_root / "data" / "raw" / "retail_transactions.csv"
cleaned_file = project_root / "data" / "cleaned" / "retail_cleaned.csv"

# Load raw data
df = pd.read_csv(raw_file)

# Convert Order_Date to date format
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing important values
df = df.dropna(subset=["Order_ID", "Customer_ID", "Product_Name", "Sales", "Profit"])

# Save cleaned data
df.to_csv(cleaned_file, index=False)

print("Data cleaning completed!")
print("Rows after cleaning:", len(df))
print("Cleaned file saved to:", cleaned_file)
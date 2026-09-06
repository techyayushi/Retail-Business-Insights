import pandas as pd

# Load the retail dataset
df = pd.read_csv("retail_transactions.csv")

# 1. Display first 5 rows
print("\nFIRST 5 ROWS")
print(df.head())

# 2. Number of rows and columns
print("\nDATASET SHAPE")
print(df.shape)

# 3. Column names
print("\nCOLUMN NAMES")
print(df.columns.tolist())

# 4. Data types and non-null values
print("\nDATA TYPES AND INFORMATION")
print(df.info())

# 5. Statistical summary
print("\nSTATISTICAL SUMMARY")
print(df.describe())

# 6. Missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# 7. Duplicate rows
print("\nDUPLICATE ROWS")
print(df.duplicated().sum())

# 8. Unique values in important columns
print("\nUNIQUE CUSTOMER COUNT")
print(df["Customer_ID"].nunique())

print("\nUNIQUE PRODUCTS")
print(df["Product_Name"].nunique())

print("\nUNIQUE CATEGORIES")
print(df["Category"].nunique())

print("\nREGIONS")
print(df["Region"].unique())
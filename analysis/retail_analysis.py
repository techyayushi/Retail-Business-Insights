from pathlib import Path
import pandas as pd

# Project folder
project_root = Path(__file__).resolve().parent.parent

# Load cleaned data
cleaned_file = project_root / "data" / "cleaned" / "retail_cleaned.csv"
df = pd.read_csv(cleaned_file)

# Basic business metrics
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
total_customers = df["Customer_ID"].nunique()

print("===== RETAIL BUSINESS ANALYSIS =====")
print("Total Sales:", total_sales)
print("Total Profit:", total_profit)
print("Total Quantity Sold:", total_quantity)
print("Total Customers:", total_customers)

# Category performance
category_analysis = (
    df.groupby("Category")
      .agg(
          Sales=("Sales", "sum"),
          Profit=("Profit", "sum"),
          Quantity=("Quantity", "sum")
      )
      .sort_values("Sales", ascending=False)
)

print("\n===== CATEGORY PERFORMANCE =====")
print(category_analysis)

# Region performance
region_analysis = (
    df.groupby("Region")
      .agg(
          Sales=("Sales", "sum"),
          Profit=("Profit", "sum"),
          Quantity=("Quantity", "sum")
      )
      .sort_values("Sales", ascending=False)
)

print("\n===== REGION PERFORMANCE =====")
print(region_analysis)

# Customer segment performance
customer_analysis = (
    df.groupby("Customer_Segment")
      .agg(
          Customers=("Customer_ID", "nunique"),
          Sales=("Sales", "sum"),
          Profit=("Profit", "sum"),
          Quantity=("Quantity", "sum")
      )
      .sort_values("Sales", ascending=False)
)

print("\n===== CUSTOMER SEGMENT PERFORMANCE =====")
print(customer_analysis)

# Product performance
product_analysis = (
    df.groupby("Product_Name")
      .agg(
          Sales=("Sales", "sum"),
          Profit=("Profit", "sum"),
          Quantity=("Quantity", "sum")
      )
      .sort_values("Sales", ascending=False)
)

print("\n===== PRODUCT PERFORMANCE =====")
print(product_analysis)

# Monthly performance
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

monthly_analysis = (
    df.groupby(df["Order_Date"].dt.to_period("M"))
      .agg(
          Sales=("Sales", "sum"),
          Profit=("Profit", "sum"),
          Quantity=("Quantity", "sum")
      )
)

print("\n===== MONTHLY PERFORMANCE =====")
print(monthly_analysis)


# Discount impact analysis
discount_analysis = (
    df.groupby("Discount")
      .agg(
          Sales=("Sales", "sum"),
          Profit=("Profit", "sum"),
          Quantity=("Quantity", "sum"),
          Transactions=("Order_ID", "count")
      )
      .sort_index()
)

print("\n===== DISCOUNT IMPACT =====")
print(discount_analysis)


# Top customers by sales
customer_sales = (
    df.groupby("Customer_ID")
      .agg(
          Sales=("Sales", "sum"),
          Profit=("Profit", "sum"),
          Orders=("Order_ID", "count"),
          Quantity=("Quantity", "sum")
      )
      .sort_values("Sales", ascending=False)
)

print("\n===== TOP 10 CUSTOMERS BY SALES =====")
print(customer_sales.head(10))

# Pareto analysis
customer_sales = customer_sales.sort_values("Sales", ascending=False)

customer_sales["Cumulative_Sales"] = customer_sales["Sales"].cumsum()

total_sales = customer_sales["Sales"].sum()

customer_sales["Cumulative_Percentage"] = (
    customer_sales["Cumulative_Sales"] / total_sales * 100
)

customers_for_80_percent = (
    customer_sales["Cumulative_Percentage"] <= 80
).sum()

percentage_customers = (
    customers_for_80_percent / len(customer_sales) * 100
)

print("\n===== PARETO ANALYSIS =====")
print("Customers contributing to first 80% of sales:",
      customers_for_80_percent)

print("Percentage of customers:",
      round(percentage_customers, 2), "%")


# Profit Margin Analysis
df["Profit_Margin"] = (df["Profit"] / df["Sales"]) * 100

margin_analysis = (
    df.groupby("Category")
      .agg(
          Sales=("Sales", "sum"),
          Profit=("Profit", "sum"),
          Average_Margin=("Profit_Margin", "mean")
      )
      .sort_values("Average_Margin", ascending=False)
)

print("\n===== PROFIT MARGIN ANALYSIS =====")
print(margin_analysis)

# Discount vs Profit Margin
discount_margin = (
    df.groupby("Discount")
      .agg(
          Sales=("Sales", "sum"),
          Profit=("Profit", "sum"),
          Transactions=("Order_ID", "count")
      )
)

discount_margin["Profit_Margin"] = (
    discount_margin["Profit"] / discount_margin["Sales"] * 100
)

print("\n===== DISCOUNT VS PROFIT MARGIN =====")
print(discount_margin)

# Product Profit Margin Analysis
product_margin = (
    df.groupby("Product_Name")
      .agg(
          Sales=("Sales", "sum"),
          Profit=("Profit", "sum"),
          Quantity=("Quantity", "sum")
      )
)

product_margin["Profit_Margin"] = (
    product_margin["Profit"] / product_margin["Sales"] * 100
)

product_margin = product_margin.sort_values(
    "Profit_Margin", ascending=False
)

print("\n===== PRODUCT PROFIT MARGIN =====")
print(product_margin)
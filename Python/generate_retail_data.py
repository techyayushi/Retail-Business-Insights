import pandas as pd
import numpy as np

# Make results reproducible
np.random.seed(42)

# Number of transactions
num_transactions = 10000

# -----------------------------
# Product information
# -----------------------------

products = {
    "Electronics": [
        "Laptop",
        "Smartphone",
        "Tablet",
        "Monitor",
        "Headphones",
        "Keyboard",
        "Mouse"
    ],
    "Furniture": [
        "Office Chair",
        "Desk",
        "Bookshelf",
        "Sofa",
        "Coffee Table"
    ],
    "Office Supplies": [
        "Notebook",
        "Pen Set",
        "Printer Paper",
        "Stapler",
        "File Folder"
    ],
    "Accessories": [
        "Backpack",
        "Wallet",
        "Watch",
        "Sunglasses",
        "Travel Bag"
    ]
}

# -----------------------------
# Location information
# -----------------------------

locations = {
    "North": ["Delhi", "Jaipur", "Chandigarh", "Lucknow"],
    "South": ["Bengaluru", "Chennai", "Hyderabad", "Kochi"],
    "East": ["Kolkata", "Bhubaneswar", "Patna", "Guwahati"],
    "West": ["Mumbai", "Pune", "Ahmedabad", "Surat"]
}

# -----------------------------
# Create product lists
# -----------------------------

product_names = []
categories = []

for category, product_list in products.items():
    for product in product_list:
        product_names.append(product)
        categories.append(category)

# -----------------------------
# Generate transaction data
# -----------------------------

data = []

for i in range(num_transactions):

    order_id = f"ORD{i + 1:05d}"

    customer_id = f"CUST{np.random.randint(1, 2001):04d}"

    order_date = pd.Timestamp("2025-01-01") + pd.to_timedelta(
        np.random.randint(0, 365),
        unit="D"
    )

    product_index = np.random.randint(len(product_names))

    product_name = product_names[product_index]
    category = categories[product_index]

    region = np.random.choice(
        list(locations.keys()),
        p=[0.30, 0.25, 0.20, 0.25]
    )

    city = np.random.choice(locations[region])

    quantity = np.random.randint(1, 6)

    unit_price = round(
        np.random.uniform(100, 60000),
        2
    )

    discount = np.random.choice(
        [0, 0.05, 0.10, 0.15, 0.20],
        p=[0.20, 0.25, 0.30, 0.15, 0.10]
    )

    sales = round(
        quantity * unit_price * (1 - discount),
        2
    )

    cost = round(
        sales * np.random.uniform(0.55, 0.80),
        2
    )

    profit = round(
        sales - cost,
        2
    )

    customer_segment = np.random.choice(
        ["Consumer", "Corporate", "Small Business"],
        p=[0.55, 0.25, 0.20]
    )

    data.append([
        order_id,
        order_date,
        customer_id,
        customer_segment,
        product_name,
        category,
        region,
        city,
        quantity,
        unit_price,
        discount,
        sales,
        cost,
        profit
    ])

# -----------------------------
# Create DataFrame
# -----------------------------

columns = [
    "Order_ID",
    "Order_Date",
    "Customer_ID",
    "Customer_Segment",
    "Product_Name",
    "Category",
    "Region",
    "City",
    "Quantity",
    "Unit_Price",
    "Discount",
    "Sales",
    "Cost",
    "Profit"
]

df = pd.DataFrame(data, columns=columns)

# -----------------------------
# Save dataset
# -----------------------------

df.to_csv(
    "retail_transactions.csv",
    index=False
)

print("Dataset created successfully!")
print(f"Total transactions: {len(df)}")
print("\nFirst 5 rows:")
print(df.head())

print("\nDataset information:")
print(df.info())
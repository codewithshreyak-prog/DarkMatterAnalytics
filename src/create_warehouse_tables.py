import pandas as pd

df = pd.read_csv("data/processed/cleaned_retail.csv")

# Customers table - one row per customer
customers = (
    df.groupby("CustomerID")
    .agg({"Country": "first"})
    .reset_index()
)

# Products table
products = df[["StockCode", "Description", "UnitPrice"]].drop_duplicates()

# Orders table - one row per invoice
orders = (
    df.groupby("InvoiceNo")
    .agg({
        "CustomerID": "first",
        "InvoiceDate": "first"
    })
    .reset_index()
)

# Order items table
order_items = df[[
    "InvoiceNo",
    "StockCode",
    "Quantity",
    "UnitPrice",
    "Revenue"
]]

customers.to_csv("data/processed/customers.csv", index=False)
products.to_csv("data/processed/products.csv", index=False)
orders.to_csv("data/processed/orders.csv", index=False)
order_items.to_csv("data/processed/order_items.csv", index=False)

print("Warehouse tables created successfully!")
print("Customers:", customers.shape)
print("Products:", products.shape)
print("Orders:", orders.shape)
print("Order Items:", order_items.shape)
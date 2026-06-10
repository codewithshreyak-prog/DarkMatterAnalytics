import pandas as pd

df = pd.read_excel("data/raw/Online Retail.xlsx")

print("Original Shape:", df.shape)
print("\nOriginal Data Types:")
print(df.dtypes)

# Remove rows without CustomerID
df = df.dropna(subset=["CustomerID"])

# Convert CustomerID from float to int
df["CustomerID"] = df["CustomerID"].astype(int)

# Make sure InvoiceDate is datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Remove rows without product description
df = df.dropna(subset=["Description"])

# Remove cancelled orders
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]

# Remove invalid quantity and price
df = df[df["Quantity"] > 0]
df = df[df["UnitPrice"] > 0]

# Create revenue column
df["Revenue"] = df["Quantity"] * df["UnitPrice"]

print("\nCleaned Shape:", df.shape)
print("\nCleaned Data Types:")
print(df.dtypes)

df.to_csv("data/processed/cleaned_retail.csv", index=False)

print("\nCleaned dataset saved to data/processed/cleaned_retail.csv")
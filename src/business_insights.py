import pandas as pd

df = pd.read_csv("data/processed/cleaned_retail.csv")

# Top 10 customers by revenue
top_customers = (
    df.groupby("CustomerID")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 CUSTOMERS")
print(top_customers)

# Top 10 products by revenue
top_products = (
    df.groupby("Description")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP 10 PRODUCTS")
print(top_products)

# Revenue by country
country_revenue = (
    df.groupby("Country")["Revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTOP COUNTRIES")
print(country_revenue)
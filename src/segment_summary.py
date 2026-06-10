import pandas as pd

rfm = pd.read_csv("data/processed/rfm_customers.csv")

summary = rfm.groupby("Segment").agg({
    "CustomerID": "count",
    "Recency": "mean",
    "Frequency": "mean",
    "Monetary": "mean"
}).round(2)

summary.columns = [
    "Customer_Count",
    "Avg_Recency",
    "Avg_Frequency",
    "Avg_Monetary"
]

print(summary)

summary.to_csv("data/processed/segment_summary.csv")

print("\nSegment summary saved!")
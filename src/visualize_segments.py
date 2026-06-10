import pandas as pd
import matplotlib.pyplot as plt

summary = pd.read_csv("data/processed/segment_summary.csv")

# Chart 1: Customer count by segment
plt.figure(figsize=(8, 5))
plt.bar(summary["Segment"], summary["Customer_Count"])
plt.title("Customer Count by Segment")
plt.xlabel("Segment")
plt.ylabel("Number of Customers")
plt.tight_layout()
plt.savefig("screenshots/customer_count_by_segment.png")
plt.show()

# Chart 2: Average monetary value by segment
plt.figure(figsize=(8, 5))
plt.bar(summary["Segment"], summary["Avg_Monetary"])
plt.title("Average Monetary Value by Segment")
plt.xlabel("Segment")
plt.ylabel("Average Revenue")
plt.tight_layout()
plt.savefig("screenshots/avg_monetary_by_segment.png")
plt.show()

# Chart 3: Average recency by segment
plt.figure(figsize=(8, 5))
plt.bar(summary["Segment"], summary["Avg_Recency"])
plt.title("Average Recency by Segment")
plt.xlabel("Segment")
plt.ylabel("Average Days Since Last Purchase")
plt.tight_layout()
plt.savefig("screenshots/avg_recency_by_segment.png")
plt.show()

print("Segment charts saved in screenshots folder!")
import os
import pandas as pd
import matplotlib.pyplot as plt

revenue_data = {
    "Month": [
        "2010-12","2011-01","2011-02","2011-03",
        "2011-04","2011-05","2011-06","2011-07",
        "2011-08","2011-09","2011-10","2011-11","2011-12"
    ],
    "Revenue": [
        572713.89,569445.04,447137.35,595500.76,
        469200.36,678594.56,661213.69,600091.01,
        645343.90,952838.38,1039318.79,1161817.38,
        518192.79
    ]
}

df = pd.DataFrame(revenue_data)

os.makedirs("screenshots", exist_ok=True)

plt.figure(figsize=(10, 5))
plt.plot(df["Month"], df["Revenue"], marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue (£)")
plt.xticks(rotation=45)
plt.tight_layout()

output_path = "screenshots/monthly_revenue_trend.png"
plt.savefig(output_path, dpi=300)
plt.close()

print(f"Revenue trend chart saved at: {output_path}")
import pandas as pd
import sqlite3

conn = sqlite3.connect(r"C:\portfolio_python\sales_decline_analysis\data\retail.db")

df = pd.read_sql("SELECT * FROM monthly_sales", conn)

df["sales"] = df["order_cnt"] * df["avg_order_value"]

df["order_change"] = df["order_cnt"].pct_change()
df["aov_change"] = df["avg_order_value"].pct_change()

print(df)

import matplotlib.pyplot as plt

plt.figure(figsize=(8,4))
plt.plot(df["year_month"], df["sales"])
plt.xticks(rotation=45)
plt.title("monthly sales trend")
plt.tight_layout()
plt.savefig(r"C:\portfolio_python\sales_decline_analysis\result\monthly_sales_trend.png")

country_sales = pd.read_sql("""
SELECT
Country,
SUM(Quantity * UnitPrice) AS sales
FROM clean_orders
GROUP BY Country
ORDER BY sales DESC
LIMIT 10
""", conn)

print(country_sales)

plt.figure(figsize=(8,4))
plt.bar(country_sales["Country"], country_sales["sales"])
plt.xticks(rotation=45)
plt.title("Top Country by Sales")
plt.tight_layout()
plt.savefig(r"C:\portfolio_python\sales_decline_analysis\result\country_sales.png")


top_customers = pd.read_sql("""
SELECT
CustomerID,
SUM(Quantity * UnitPrice) as total_sales
FROM clean_orders
GROUP BY CustomerID
ORDER BY total_sales DESC
LIMIT 10
""", conn)

print(top_customers)

plt.figure(figsize=(8,4))
plt.bar(top_customers["CustomerID"].astype(str), top_customers["total_sales"])
plt.xticks(rotation=45)
plt.title("Top Customers by Sales")
plt.tight_layout()
plt.savefig(r"C:\portfolio_python\sales_decline_analysis\result\top_customers.png")

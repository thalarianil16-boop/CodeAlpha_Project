import pandas as pd
import matplotlib.pyplot as plt

print("Task 3: Data Visualization")

# Load dataset

df = pd.read_csv("Online_Retail.csv")

print("Dataset loaded successfully")
print(df.head())

# Create sales column

df["Sales"] = df["Quantity"] * df["UnitPrice"]

print("\nSales column created successfully")
print(df[["Quantity", "UnitPrice", "Sales"]].head())

# Convert InvoiceDate to datetime

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# Create Month column

df["Month"] =  df["InvoiceDate"].dt.to_period("M")

# Calculate monthly sales
monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# Monthly Sales Trend
plt.figure(figsize=(12, 6))

monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Top 10 Products by Sales

top_products = (
    df.groupby("Description")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Products by Sales:")
print(top_products)

# Create a bar chart
plt.figure(figsize=(12, 6))

top_products.plot(kind = "bar")

plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.xticks(rotation = 45)

plt.tight_layout()
plt.show()

# Top 10 Countries by Sales

top_countries = (
    df.groupby("Country")["Sales"]
    .sum()
    .sort_values(ascending = False)
    .head(10)
)

print("\nTop 10 Countries by Sales:")
print(top_countries)

# Create bar chart
plt.figure(figsize = (12, 6))

top_countries.plot(kind = "bar")

plt.title("Top 10 Countries by Sales")
plt.xlabel("Country")
plt.ylabel("Total Sales")

plt.xticks(rotation = 45)

plt.tight_layout()
plt.show()

# Quantity Sold Distribution

plt.figure(figsize=(10, 6))

plt.hist(df["Quantity"], bins=30)

plt.title("Quantity Sold Distribution")
plt.xlabel("Quantity")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

# Sales Distribution

plt.figure(figsize=(10, 6))

plt.hist(df["Sales"], bins=30)

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

# Sales vs Quantity

plt.figure(figsize=(10, 6))

plt.scatter(df["Quantity"], df["Sales"], alpha=0.5)

plt.title("Sales vs Quantity")
plt.xlabel("Quantity")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()

# Top 10 Products - Horizontal Bar Chart

plt.figure(figsize=(10, 6))

top_products.sort_values().plot(kind="barh")

plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product")

plt.tight_layout()
plt.show()

# Top 10 Countries - Horizontal Bar Chart

plt.figure(figsize=(10, 6))

top_countries.sort_values().plot(kind="barh")

plt.title("Top 10 Countries by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Country")

plt.tight_layout()
plt.show()
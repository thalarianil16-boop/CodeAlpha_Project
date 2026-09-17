
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# EDA Questions

# 1. Which countries generate the highest sales?
# 2. Which products generate the highest sales?
# 3. How do sales change from month to month?
# 4. Which products are sold in the highest quantities?
# 5. How many transactions are cancelled?
# 6. Are there missing values and duplicate records?
# 7. Are there unusual values such as negative quantities or prices?
# 8. Did sales increase during the later months of 2011?
print("CodeAlpha EDA Project")

#  Load Dataset
# utf-8-sig removes the BOM from the first column name
df = pd.read_csv("Online_Retail.csv", encoding="utf-8-sig")

print("Project started successfully")

#  Display first rows
print(df.head())

#  Dataset Shape
print("\nDataset Shape:")
print(df.shape)

#  Column Names
print("\nColumn Names:")
print(df.columns)

#  Data Types
print("\nData Types:")
print(df.dtypes)

#  Dataset Information
print("\nDataset Information:")
df.info()

#  Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

#  Data Quality Checks

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nNegative Quantity:")
print((df["Quantity"] < 0).sum())

print("\nZero Unit Price:")
print((df["UnitPrice"] == 0).sum())

print("\nNegative Unit Price:")
print((df["UnitPrice"] < 0).sum())

# Cancelled Transactions
cancelled = df["InvoiceNo"].astype(str).str.startswith("C")

print("\nCancelled Transactions:")
print(cancelled.sum())

print("\nSample Cancelled Transactions:")
print(df[cancelled].head())

#  Remove Duplicates
df = df.drop_duplicates()

print("\nShape after removing duplicates:")
print(df.shape)

# Convert InvoiceDate
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

print("\nInvoiceDate Data Type:")
print(df["InvoiceDate"].dtype)

# Remove Missing Description
print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

df = df.dropna(subset=["Description"])

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nDataset Shape After Cleaning:")
print(df.shape)

# Calculate Sales
df["Sales"] = df["Quantity"] * df["UnitPrice"]

print("\nSales Column Created:")
print(df[["Quantity", "UnitPrice", "Sales"]].head())

# Basic Sales Analysis

print("\nTotal Sales:")
print(df["Sales"].sum())

print("\nAverage Sales:")
print(df["Sales"].mean())

print("\nMaximum Sales:")
print(df["Sales"].max())

print("\nMinimum Sales:")
print(df["Sales"].min())

# Sales by Country
country_sales = df.groupby("Country")["Sales"].sum()

print("\nTop 10 Countries by Sales:")
print(country_sales.sort_values(ascending=False).head(10))

#  Country Chart
top_countries = country_sales.sort_values(
    ascending=False
).head(10)

plt.figure(figsize=(10, 6))

top_countries.plot(kind="bar")

plt.title("Top 10 Countries by Sales")
plt.xlabel("Country")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Top 10 Products
product_sales = df.groupby("Description")["Sales"].sum()

top_products = product_sales.sort_values(
    ascending=False
).head(10)

print("\nTop 10 Products by Sales:")
print(top_products)

# Product Chart
plt.figure(figsize=(12, 6))

top_products.plot(kind="bar")

plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.xticks(rotation=75)

plt.tight_layout()
plt.show()

#  Monthly Sales
df["Month"] = df["InvoiceDate"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

#  Monthly Sales Chart
plt.figure(figsize=(12, 6))

monthly_sales.plot(kind="line", marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

print("\nEDA Analysis Completed Successfully!")

#  Hypothesis Testing
# Hypothesis: Sales increased during the later months of 2011.

first_half_sales = monthly_sales[
    monthly_sales.index <= "2011-06"
].sum()

second_half_sales = monthly_sales[
    monthly_sales.index >= "2011-07"
].sum()

print("\nHypothesis Testing:")
print("First half sales (Dec 2010 - Jun 2011):", first_half_sales)
print("Second half sales (Jul 2011 - Dec 2011):", second_half_sales)

if second_half_sales > first_half_sales:
    print("Result: Sales were higher during the later months.")
else:
    print("Result: Sales were not higher during the later months.")
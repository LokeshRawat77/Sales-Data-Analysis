import pandas as pd

# Load sales dataset
df = pd.read_csv("sales_data.csv")

# Show basic information
print("📊 SALES DATA ANALYSIS REPORT")
print("-" * 40)

print("\nFirst 100 Rows:")
print(df.head())

print("\nDataset Shape:")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print("\nMissing Values:")
print(df.isnull().sum())

# Handle missing values
df["Quantity"] = df["Quantity"].fillna(0)
df["Price"] = df["Price"].fillna(0)
df["Total_Sales"] = df["Total_Sales"].fillna(df["Quantity"] * df["Price"])

# Remove duplicate records
df = df.drop_duplicates()

# Calculate metrics
total_revenue = df["Total_Sales"].sum()
total_quantity = df["Quantity"].sum()
average_sale = df["Total_Sales"].mean()

best_selling_product = df.groupby("Product")["Quantity"].sum().idxmax()
best_revenue_product = df.groupby("Product")["Total_Sales"].sum().idxmax()
top_region = df.groupby("Region")["Total_Sales"].sum().idxmax()

# Print clean report
print("\n📌 FINAL REPORT")
print("-" * 40)
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Total Quantity Sold: {total_quantity}")
print(f"Average Sale Value: ₹{average_sale:,.2f}")
print(f"Best-Selling Product: {best_selling_product}")
print(f"Highest Revenue Product: {best_revenue_product}")
print(f"Top Performing Region: {top_region}")

print("\n✅ Analysis completed successfully!")
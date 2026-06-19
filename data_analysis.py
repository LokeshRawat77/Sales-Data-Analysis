import pandas as pd

# Load CSV file
df = pd.read_csv("sales_data.csv")

# Display first 5 rows
print(" First 5 Rows:")
print(df.head())

# Dataset information
print("\n Dataset Information:")
print(df.info())

# Shape of dataset
print("\n Number of Rows and Columns:")
print(df.shape)

# Missing values
print("\n Missing Values:")
print(df.isnull().sum())

# Statistics
print("\n  Average Values:")
print(df[["Quantity", "Price", "Total_Sales"]].mean())

print("\n Maximum Values:")
print(df[["Quantity", "Price", "Total_Sales"]].max())

print("\n  Minimum Values:")
print(df[["Quantity", "Price", "Total_Sales"]].min())
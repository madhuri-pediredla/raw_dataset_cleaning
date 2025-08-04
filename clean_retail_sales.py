import pandas as pd
from datetime import datetime

df = pd.read_csv("retail_sales_sample.csv")

df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce', dayfirst=True)
df['Order Date'].fillna(pd.Timestamp.today(), inplace=True)  

df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Quantity'].fillna(0, inplace=True)  
df['Quantity'] = df['Quantity'].astype(int)

df['Unit Price'] = pd.to_numeric(df['Unit Price'], errors='coerce').fillna(0.0)
df['Total'] = pd.to_numeric(df['Total'], errors='coerce').fillna(0.0)


df['Country'] = df['Country'].astype(str).str.strip().str.title()
df['Category'] = df['Category'].astype(str).str.strip().str.title()


print(" Cleaned Data Preview (with filled values):")
print(df.head())

df.to_csv("retail_sales_cleaned.csv", index=False)
print("\n Cleaned data saved to 'retail_sales_cleaned.csv'")
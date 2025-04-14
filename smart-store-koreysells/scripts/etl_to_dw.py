import pandas as pd
import sqlite3
import os

# Set paths
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
prepared_dir = os.path.join(project_root, "data", "prepared")
dw_dir = os.path.join(project_root, "data", "dw")
os.makedirs(dw_dir, exist_ok=True)
db_path = os.path.join(dw_dir, "smart_sales.db")

# Connect to SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id TEXT PRIMARY KEY,
    name TEXT,
    region TEXT,
    join_date TEXT,
    miles_from_depot REAL,
    preferredcontactmethod TEXT,
    loyaltypoints REAL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id TEXT PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    unit_price REAL,
    weight REAL,
    supplier TEXT,
    stockquantity INTEGER
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    transaction_id INTEGER PRIMARY KEY,
    date TEXT,
    store_id TEXT,
    customer_id TEXT,
    product_id TEXT,
    quantity INTEGER,
    sales_amount REAL,
    shipping_cost REAL,
    promotion_code TEXT,
    campaignid TEXT,
    discountpercent REAL,
    paymenttype TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
""")

# Load data from cleaned CSVs
customers_df = pd.read_csv(os.path.join(prepared_dir, "customers_data_prepared.csv"))
products_df = pd.read_csv(os.path.join(prepared_dir, "products_data_prepared.csv"))
sales_df = pd.read_csv(os.path.join(prepared_dir, "sales_data_prepared.csv"))

# Clean column names
customers_df.columns = customers_df.columns.str.lower().str.strip().str.replace(" ", "_")
products_df.columns = products_df.columns.str.lower().str.strip().str.replace(" ", "_")
sales_df.columns = sales_df.columns.str.lower().str.strip().str.replace(" ", "_")

# Rename columns to match schema
customers_df = customers_df.rename(columns={
    "customerid": "customer_id",
    "joindate": "join_date",
    "preferredcontactmethod": "preferredcontactmethod",
    "loyaltypoints": "loyaltypoints"
})

products_df = products_df.rename(columns={
    "productid": "product_id",
    "productname": "product_name",
    "unitprice": "unit_price",
    "stock": "stockquantity"
})

sales_df = sales_df.rename(columns={
    "transactionid": "transaction_id",
    "saledate": "date",
    "saleamount": "sales_amount",
    "storeid": "store_id",
    "customerid": "customer_id",
    "productid": "product_id",
    "campaignid": "campaignid",
    "discountpercent": "discountpercent",
    "paymenttype": "paymenttype"
})

# Optional: Delete existing records before loading
cursor.execute("DELETE FROM customers")
cursor.execute("DELETE FROM products")
cursor.execute("DELETE FROM sales")

# Load data into tables
customers_df.to_sql("customers", conn, if_exists="append", index=False)
products_df.to_sql("products", conn, if_exists="append", index=False)
sales_df.to_sql("sales", conn, if_exists="append", index=False)

conn.commit()
conn.close()

print(f"✅ Data warehouse created at: {db_path}")
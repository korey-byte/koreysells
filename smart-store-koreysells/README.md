# 🧠 Smart Store Project - KoreySells

A business intelligence project to clean and prepare smart store sales data using Python, pandas, and sheer entrepreneurial spite.

---

## 📁 Structure

```
smart-store-koreysells/
├── data/
│   ├── raw/
│   │   ├── customers_data.csv
│   │   ├── products_data.csv
│   │   └── sales_data.csv
│   ├── prepared/
│   │   ├── customers_data_prepared.csv
│   │   ├── products_data_prepared.csv
│   │   └── sales_data_prepared.csv
│   └── dw/
│       └── smart_sales.db
├── logs/
├── scripts/
│   ├── data_scrubber.py
│   ├── data_prep.py
│   ├── etl_to_dw.py
│   └── data_prepared/
│       ├── prepare_customers_data.py
│       ├── prepare_products_data.py
│       └── prepare_sales_data.py
├── tests/
│   └── test_data_scrubber.py
├── utils/
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ⚙️ Setup

1. Clone the repo:  
   `git clone https://github.com/korey-byte/koreysells.git`

2. Create & activate a virtual environment (macOS):  
   `python3 -m venv .venv && source .venv/bin/activate`

3. Install dependencies:  
   `pip install -r requirements.txt`

---

## 🧪 Workflow & Highlights

### ✅ P2 - Initial Setup & Scripting

- Initialized a Python project with `venv`, Git, and external packages.
- Created `scripts/data_prep.py` and `utils/logger.py`.
- Verified structure: `README.md`, `.gitignore`, `requirements.txt`, and raw data files.

### ✅ P3 - Data Cleaning & ETL Prep

- Built a reusable `DataScrubber` class for cleaning:
  - Removed duplicates
  - Handled missing values
  - Converted data types
  - Filtered outliers
- Verified `DataScrubber` works using unit tests in `tests/test_data_scrubber.py`.
- Cleaned all three datasets:
  - `customers_data.csv`: Fixed casing, date formats, and numeric fields.
  - `products_data.csv`: Standardized types, filtered pricing errors.
  - `sales_data.csv`: Cleaned amounts, standardized fields.
- Saved outputs in `data/prepared/`.

### ✅ P4 - Data Warehouse Design & Population

	•	Designed a Star Schema:
	  •	Fact Table: sales
	  •	Dimension Tables: customers, products
	•	Created the database smart_sales.db in data/dw/ using SQLite.
	•	Built and loaded the tables using the ETL script scripts/etl_to_dw.py.
	•	Added critical fields to support deeper analytics, such as:
	  •	loyaltypoints, preferredcontactmethod, store_id, stockquantity
	•	Handled ETL errors by matching CSV column names to database schemas exactly.
	•	Verified table structure and data population using VS Code SQLite Viewer.

---

### ✅ P5 -  Final Assignment: Cross-Platform Reporting (MacOS)

- Connected to SQLite database (smart_sales.db) using PySpark.
- Loaded sales, customers, and products data into Spark DataFrames.
- Queried total revenue per customer using Spark SQL.
- Created drilldown aggregations by Year, Quarter, and Month.
- Built Top Customers bar chart and Sales Trend line chart using Seaborn/Matplotlib.
- Documented final analysis work in `final_p5_work.ipynb`.
  
### ✅ P6 - OLAP Analysis & Insights (MacOS)

- Connected to the SQLite database (smart_sales.db) directly using Python.
- Performed OLAP analysis by joining the sales and products tables.
- Aggregated total sales_amount by product category.
- Created a bar chart visualizing Total Sales by Product Category.
- Saved output graph (p6_sales_by_category.png) inside scripts/OLAP/.
- Challenges: 
  - Initial SQL query failed due to incorrect column name (sale_amount vs sales_amount).
  - Solved by manually checking table columns inside the database.
- Suggested Business Action:
  - Focus marketing efforts on Electronics, which dominated total sales.


### ✅ P7 - Custom BI Project
  - Loaded sales_data_prepared.csv into Jupyter Notebook.
	- Aggregated and analyzed:
  	- Total Sales Amount by Product
  	- Average Sale Amount by Store
  	- Total Sales Amount by Campaign
  	- Average Discount Percent by Payment Type
  	- Total Sales Amount by Payment Type
	- Created and saved bar charts:
  	- p7c_total_sales_by_product.png
  	- p7c_avg_sale_by_store.png
  	- p7c_total_sales_by_campaign.png
  	- p7c_avg_discount_by_payment.png
  	- p7c_total_sales_by_payment.png
	- Suggested Business Actions:
  	- Focus inventory on Product ID 101.
  	- Prioritize Store ID 401 operations.
  	- Maximize Campaign ID 0 performance.
  	- Encourage Cash and PayPal payments.
---

## 🔁 Key Commands

```bash
# Activate virtual environment
source .venv/bin/activate

# Run tests
python3 tests/test_data_scrubber.py

# Run individual scripts
PYTHONPATH=. python3 scripts/data_prepared/prepare_customers_data.py
PYTHONPATH=. python3 scripts/data_prepared/prepare_products_data.py
PYTHONPATH=. python3 scripts/data_prepared/prepare_sales_data.py

# Git workflow
git pull origin main
git add .
git commit -m "Cleaned and loaded data into DW"
git push origin main
```

---

Built with caffeine, chaos, and no tolerance for messy data.  
💼 – KoreySells
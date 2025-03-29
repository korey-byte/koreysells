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
│   └── prepared/
│       ├── customers_data_prepared.csv
│       ├── products_data_prepared.csv
│       └── sales_data_prepared.csv
├── logs/
├── scripts/
│   ├── data_scrubber.py
│   ├── data_prep.py
│   ├── autofill_sales_columns.py
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
git commit -m "Cleaned and prepared smart store data with DataScrubber"
git push origin main
```

---

Built with caffeine, chaos, and no tolerance for messy data.  
💼 – KoreySells
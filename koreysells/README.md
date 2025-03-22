# 🛍️ Smart Store: KoreySells

A Business Intelligence project for processing and analyzing retail sales data using Python.

This repo is part of a course assignment to build real-world analytics workflows using tools like virtual environments, Git, Python scripts, and logging.

---

## 📁 Project Structure

```
koreysells/
│
├── data/
│   └── raw/
│       ├── customers_data.csv
│       ├── products_data.csv
│       └── sales_data.csv
│
├── scripts/
│   └── data_prep.py
│
├── utils/
│   └── logger.py
│
├── logs/
│   └── project_log.log
│
├── .gitignore
├── requirements.txt
├── README.md
└── venv_checker.log
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/korey-byte/koreysells.git
cd koreysells
```

### 2. Create and activate virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate  # Mac/Linux
```

### 3. Install required packages

```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

### 4. (Optional) Verify setup

```bash
python3 -m datafun_venv_checker.venv_checker
```

---

## 🚀 Running Scripts

### Run the data preparation script

```bash
python3 scripts/data_prep.py
```

### Output Example:

```
INFO: Loading raw data files...
INFO: Customers: (11, 4)
INFO: Products: (8, 4)
INFO: Sales: (94, 7)
```

All logs also saved to `logs/project_log.log`.

---

## 🔁 Git Workflow

Use the following commands when updating the repo:

```bash
git pull origin main
git add .
git commit -m "Describe what you changed"
git push -u origin main
```

---

## 🧠 Project Purpose

This project simulates a real-world analytics workflow. It emphasizes:
- Clean repo setup
- Logging with `logger.py`
- Structured folders for scaling
- Proper Git hygiene and documentation

It’s meant to help build foundational habits for working on a data team.

---

## 🧼 Repo Status

- [x] All folders structured and organized ✅  
- [x] Virtual environment working ✅  
- [x] Logging configured and verified ✅  
- [x] Scripts run successfully ✅  
- [x] README polished ✅  

---

## 💬 Author

**Korey Sansone**  
[GitHub Profile](https://github.com/korey-byte)  
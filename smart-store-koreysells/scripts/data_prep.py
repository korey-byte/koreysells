import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utils.logger import logger

logger.info("Loading raw data files...")

customers = pd.read_csv("data/raw/customers_data.csv")
products = pd.read_csv("data/raw/products_data.csv")
sales = pd.read_csv("data/raw/sales_data.csv")

logger.info(f"Customers: {customers.shape}")
logger.info(f"Products: {products.shape}")
logger.info(f"Sales: {sales.shape}")
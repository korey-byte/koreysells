import logging
import os

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

# Set up logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create file handler
file_handler = logging.FileHandler("logs/project_log.log")
file_handler.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.info("Logging to file: logs/project_log.log")

def get_logger(name: str) -> logging.Logger:
    return logger
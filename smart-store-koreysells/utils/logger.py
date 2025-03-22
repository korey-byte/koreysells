import logging

# Create a logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create a console handler
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Create formatter and add it to the handler
formatter = logging.Formatter('%(levelname)s: %(message)s')
ch.setFormatter(formatter)

# Add handler to the logger
logger.addHandler(ch)
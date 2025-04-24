import logging

logging.basicConfig(filename="app.log", level=logging.WARNING)

try:
    1 / 0
except Exception:
    logging.warning("An error occurred, please check internal logs.")

import logging
import os
from dotenv import load_dotenv

load_dotenv()
ENV = os.getenv("ENV", "dev")

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)


class UppercaseFilter(logging.Filter):
    def filter(self, record):
        record.name = record.name.upper()
        return True
    

def get_logger(name: str, log_file: str, level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevention: handler not connecting 2-3 times each time the logger is called
    if logger.hasHandlers():
        return logger

    # Formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # File handler
    file_path = os.path.join(LOG_DIR, log_file)
    file_handler = logging.FileHandler(file_path)
    file_handler.setLevel(level)
    file_handler.setFormatter(formatter)
    file_handler.addFilter(UppercaseFilter())
    logger.addHandler(file_handler)

    # In "dev" mode logs are printed into console
    if ENV != "prod":
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        console_handler.addFilter(UppercaseFilter())
        logger.addHandler(console_handler)

    logger.propagate = False
    return logger

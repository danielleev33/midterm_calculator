import logging

from app.calculator_config import CalculatorConfig, ensure_directories


def get_logger():
    ensure_directories()

    logger = logging.getLogger("calculator")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(
            CalculatorConfig.LOG_FILE,
            encoding=CalculatorConfig.DEFAULT_ENCODING
        )
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
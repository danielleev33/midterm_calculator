import os
from dotenv import load_dotenv

load_dotenv()


class CalculatorConfig:
    LOG_DIR = os.getenv("CALCULATOR_LOG_DIR", "logs")
    HISTORY_DIR = os.getenv("CALCULATOR_HISTORY_DIR", "data")
    MAX_HISTORY_SIZE = int(os.getenv("CALCULATOR_MAX_HISTORY_SIZE", 100))
    AUTO_SAVE = os.getenv("CALCULATOR_AUTO_SAVE", "true").lower() == "true"
    PRECISION = int(os.getenv("CALCULATOR_PRECISION", 2))
    MAX_INPUT_VALUE = float(os.getenv("CALCULATOR_MAX_INPUT_VALUE", 1000000))
    DEFAULT_ENCODING = os.getenv("CALCULATOR_DEFAULT_ENCODING", "utf-8")
    LOG_FILE = os.getenv("CALCULATOR_LOG_FILE", "logs/calculator.log")
    HISTORY_FILE = os.getenv("CALCULATOR_HISTORY_FILE", "data/history.csv")


def ensure_directories() -> None:
    os.makedirs(CalculatorConfig.LOG_DIR, exist_ok=True)
    os.makedirs(CalculatorConfig.HISTORY_DIR, exist_ok=True)
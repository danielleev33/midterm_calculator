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


class LoggingObserver:
    def __init__(self):
        self.logger = get_logger()

    def update(self, calculation, history):
        self.logger.info(
            "Performed %s on %s and %s -> %s",
            calculation.operation,
            calculation.operand1,
            calculation.operand2,
            calculation.result,
        )


class AutoSaveObserver:
    def update(self, calculation, history):
        if CalculatorConfig.AUTO_SAVE:
            history.save_to_csv()
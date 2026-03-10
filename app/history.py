import os
import pandas as pd

from app.calculation import Calculation
from app.calculator_config import CalculatorConfig, ensure_directories
from app.exceptions import HistoryError


class History:
    def __init__(self):
        self.history = []
        ensure_directories()

    def add_calculation(self, calculation):
        if len(self.history) >= CalculatorConfig.MAX_HISTORY_SIZE:
            self.history.pop(0)
        self.history.append(calculation)

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history = []

    def save_to_csv(self, file_path=None):
        file_path = file_path or CalculatorConfig.HISTORY_FILE

        try:
            data = [calc.to_dict() for calc in self.history]
            df = pd.DataFrame(data)
            df.to_csv(file_path, index=False, encoding=CalculatorConfig.DEFAULT_ENCODING)
        except Exception as exc:
            raise HistoryError(f"Failed to save history to CSV: {exc}") from exc

    def load_from_csv(self, file_path=None):
        file_path = file_path or CalculatorConfig.HISTORY_FILE

        if not os.path.exists(file_path):
            raise HistoryError(f"History file does not exist: {file_path}")

        try:
            df = pd.read_csv(file_path, encoding=CalculatorConfig.DEFAULT_ENCODING)

            required_columns = {"operation", "operand1", "operand2", "result", "timestamp"}
            if not required_columns.issubset(df.columns):
                raise HistoryError("CSV file is missing required columns.")

            self.history = [
                Calculation(
                    row["operation"],
                    row["operand1"],
                    row["operand2"],
                    row["result"],
                    row["timestamp"],
                )
                for _, row in df.iterrows()
            ]
        except HistoryError:
            raise
        except Exception as exc:
            raise HistoryError(f"Failed to load history from CSV: {exc}") from exc
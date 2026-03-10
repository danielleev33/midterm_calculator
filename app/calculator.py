from app.calculation import Calculation
from app.calculator_config import CalculatorConfig
from app.calculator_memento import CalculatorMemento
from app.history import History
from app.input_validators import validate_number
from app.operations import OperationFactory
from app.logger import LoggingObserver, AutoSaveObserver


class Calculator:
    def __init__(self):
        self.history = History()
        self.undo_stack = []
        self.redo_stack = []
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, calculation):
        for observer in self.observers:
            observer.update(calculation, self.history)

    def _save_state(self):
        memento = CalculatorMemento(self.history.get_history())
        self.undo_stack.append(memento)

    def calculate(self, operation_name, a, b):
        a = validate_number(a)
        b = validate_number(b)

        self._save_state()
        self.redo_stack.clear()

        operation = OperationFactory.create_operation(operation_name)
        result = operation.execute(a, b)
        result = round(result, CalculatorConfig.PRECISION)

        calculation = Calculation(operation_name, a, b, result)
        self.history.add_calculation(calculation)
        self.notify_observers(calculation)

        return result

    def get_history(self):
        return self.history.get_history()

    def clear_history(self):
        self._save_state()
        self.redo_stack.clear()
        self.history.clear_history()

    def undo(self):
        if not self.undo_stack:
            return False

        current_state = CalculatorMemento(self.history.get_history())
        self.redo_stack.append(current_state)

        previous_state = self.undo_stack.pop()
        self.history.history = previous_state.get_state()
        return True

    def redo(self):
        if not self.redo_stack:
            return False

        current_state = CalculatorMemento(self.history.get_history())
        self.undo_stack.append(current_state)

        next_state = self.redo_stack.pop()
        self.history.history = next_state.get_state()
        return True

    def save_history(self, file_path=None):
        self.history.save_to_csv(file_path)

    def load_history(self, file_path=None):
        self._save_state()
        self.redo_stack.clear()
        self.history.load_from_csv(file_path)


def run_repl():
    calculator = Calculator()
    calculator.add_observer(LoggingObserver())
    calculator.add_observer(AutoSaveObserver())

    commands = {
        "add",
        "subtract",
        "multiply",
        "divide",
        "power",
        "root",
        "modulus",
        "int_divide",
        "percent",
        "abs_diff",
    }

    print("Advanced Calculator REPL")
    print("Type 'help' for available commands.")

    while True:
        try:
            user_input = input(">>> ").strip()

            if not user_input:
                continue

            parts = user_input.split()
            command = parts[0].lower()

            if command == "exit":
                print("Exiting calculator. Goodbye!")
                break

            elif command == "help":
                print("Available commands:")
                print("  add a b")
                print("  subtract a b")
                print("  multiply a b")
                print("  divide a b")
                print("  power a b")
                print("  root a b")
                print("  modulus a b")
                print("  int_divide a b")
                print("  percent a b")
                print("  abs_diff a b")
                print("  history")
                print("  clear")
                print("  undo")
                print("  redo")
                print("  save")
                print("  load")
                print("  help")
                print("  exit")

            elif command in commands:
                if len(parts) != 3:
                    print(f"Usage: {command} <a> <b>")
                    continue

                result = calculator.calculate(command, parts[1], parts[2])
                print(f"Result: {result}")

            elif command == "history":
                history = calculator.get_history()
                if not history:
                    print("History is empty.")
                else:
                    for calc in history:
                        print(calc)

            elif command == "clear":
                calculator.clear_history()
                print("History cleared.")

            elif command == "undo":
                if calculator.undo():
                    print("Undo successful.")
                else:
                    print("Nothing to undo.")

            elif command == "redo":
                if calculator.redo():
                    print("Redo successful.")
                else:
                    print("Nothing to redo.")

            elif command == "save":
                calculator.save_history()
                print("History saved successfully.")

            elif command == "load":
                calculator.load_history()
                print("History loaded successfully.")

            else:
                print("Unknown command. Type 'help' for available commands.")

        except Exception as exc:
            print(f"Error: {exc}")


if __name__ == "__main__":  # pragma: no cover
    run_repl()
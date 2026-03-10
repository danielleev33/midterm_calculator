from app.calculation import Calculation
from app.calculator_config import CalculatorConfig
from app.calculator_memento import CalculatorMemento
from app.history import History
from app.input_validators import validate_number
from app.operations import OperationFactory


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
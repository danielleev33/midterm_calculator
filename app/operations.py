from abc import ABC, abstractmethod
from app.exceptions import OperationError

class Operation(ABC):
    @abstractmethod
    def execute(self, a, b):
        """Execute the operation on two numeric inputs."""
        pass  # pragma: no cover


class Add(Operation):
    def execute(self, a, b):
        return a + b


class Subtract(Operation):
    def execute(self, a, b):
        return a - b


class Multiply(Operation):
    def execute(self, a, b):
        return a * b


class Power(Operation):
    def execute(self, a, b):
        return a ** b


class AbsDiff(Operation):
    def execute(self, a, b):
        return abs(a - b)


class Divide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Cannot divide by zero.")
        return a / b


class Modulus(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Cannot take modulus by zero.")
        return a % b


class IntDivide(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Cannot perform integer division by zero.")
        return a // b


class Percent(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Cannot calculate percentage with zero denominator.")
        return (a / b) * 100


class Root(Operation):
    def execute(self, a, b):
        if b == 0:
            raise OperationError("Cannot calculate zeroth root.")

        if a < 0:
            if b % 2 == 0:
                raise OperationError("Cannot calculate an even root of a negative number.")
            return -((-a) ** (1 / b))

        return a ** (1 / b)


class OperationFactory:
    _operations = {
        "add": Add,
        "subtract": Subtract,
        "multiply": Multiply,
        "divide": Divide,
        "power": Power,
        "root": Root,
        "modulus": Modulus,
        "int_divide": IntDivide,
        "percent": Percent,
        "abs_diff": AbsDiff,
    }

    @classmethod
    def create_operation(cls, operation_name):
        operation_class = cls._operations.get(operation_name.lower())
        if not operation_class:
            raise OperationError(f"Unsupported operation: {operation_name}")
        return operation_class()
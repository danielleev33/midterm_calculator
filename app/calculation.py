from datetime import datetime


class Calculation:
    def __init__(self, operation, operand1, operand2, result, timestamp=None):
        self.operation = operation
        self.operand1 = operand1
        self.operand2 = operand2
        self.result = result
        self.timestamp = timestamp or datetime.now()

    def to_dict(self):
        return {
            "operation": self.operation,
            "operand1": self.operand1,
            "operand2": self.operand2,
            "result": self.result,
            "timestamp": self.timestamp,
        }

    def __str__(self):
        return f"{self.operation}({self.operand1}, {self.operand2}) = {self.result}"
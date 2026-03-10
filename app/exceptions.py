class CalculatorError(Exception):
    """Base calculator exception."""
    pass


class OperationError(CalculatorError):
    """Raised for invalid calculator operations."""
    pass


class ValidationError(CalculatorError):
    """Raised for invalid user input."""
    pass


class HistoryError(CalculatorError):
    """Raised for history/save/load issues."""
    pass
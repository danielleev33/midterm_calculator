from app.calculator import Calculator
import pytest
from app.exceptions import ValidationError, OperationError


def test_calculate_add():
    calculator = Calculator()
    result = calculator.calculate("add", 2, 3)

    assert result == 5
    assert len(calculator.get_history()) == 1


def test_calculate_divide():
    calculator = Calculator()
    result = calculator.calculate("divide", 10, 2)

    assert result == 5


def test_clear_history():
    calculator = Calculator()
    calculator.calculate("add", 2, 3)
    calculator.clear_history()

    assert calculator.get_history() == []


def test_undo():
    calculator = Calculator()
    calculator.calculate("add", 2, 3)
    calculator.calculate("multiply", 4, 5)

    assert len(calculator.get_history()) == 2

    success = calculator.undo()

    assert success is True
    assert len(calculator.get_history()) == 1
    assert calculator.get_history()[0].operation == "add"


def test_redo():
    calculator = Calculator()
    calculator.calculate("add", 2, 3)
    calculator.calculate("multiply", 4, 5)

    calculator.undo()
    success = calculator.redo()

    assert success is True
    assert len(calculator.get_history()) == 2
    assert calculator.get_history()[1].operation == "multiply"


def test_undo_empty():
    calculator = Calculator()
    assert calculator.undo() is False


def test_redo_empty():
    calculator = Calculator()
    assert calculator.redo() is False


def test_calculate_invalid_input():
    calculator = Calculator()
    with pytest.raises(ValidationError):
        calculator.calculate("add", "abc", 3)


def test_calculate_input_exceeds_max():
    calculator = Calculator()
    with pytest.raises(ValidationError):
        calculator.calculate("add", 1000000000, 1)


def test_calculate_divide_by_zero():
    calculator = Calculator()
    with pytest.raises(OperationError):
        calculator.calculate("divide", 10, 0)
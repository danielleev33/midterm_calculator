import pytest

from app.exceptions import OperationError
from app.operations import (
    Add,
    Subtract,
    Multiply,
    Divide,
    Power,
    Root,
    Modulus,
    IntDivide,
    Percent,
    AbsDiff,
    OperationFactory,
)


def test_add():
    assert Add().execute(2, 3) == 5


def test_subtract():
    assert Subtract().execute(10, 4) == 6


def test_multiply():
    assert Multiply().execute(3, 5) == 15


def test_divide():
    assert Divide().execute(10, 2) == 5


def test_power():
    assert Power().execute(2, 3) == 8


def test_root_square():
    assert Root().execute(16, 2) == 4


def test_root_cube():
    assert Root().execute(27, 3) == 3


def test_root_negative_odd():
    assert Root().execute(-8, 3) == -2


def test_modulus():
    assert Modulus().execute(10, 3) == 1


def test_int_divide():
    assert IntDivide().execute(10, 3) == 3


def test_percent():
    assert Percent().execute(25, 200) == 12.5


def test_abs_diff():
    assert AbsDiff().execute(3, 10) == 7


def test_divide_by_zero():
    with pytest.raises(OperationError):
        Divide().execute(10, 0)


def test_modulus_by_zero():
    with pytest.raises(OperationError):
        Modulus().execute(10, 0)


def test_int_divide_by_zero():
    with pytest.raises(OperationError):
        IntDivide().execute(10, 0)


def test_percent_zero_denominator():
    with pytest.raises(OperationError):
        Percent().execute(25, 0)


def test_root_zero_degree():
    with pytest.raises(OperationError):
        Root().execute(16, 0)


def test_root_negative_even():
    with pytest.raises(OperationError):
        Root().execute(-16, 2)


def test_factory_add():
    operation = OperationFactory.create_operation("add")
    assert isinstance(operation, Add)


def test_factory_divide():
    operation = OperationFactory.create_operation("divide")
    assert isinstance(operation, Divide)


def test_factory_abs_diff():
    operation = OperationFactory.create_operation("abs_diff")
    assert isinstance(operation, AbsDiff)


def test_factory_invalid_operation():
    with pytest.raises(OperationError):
        OperationFactory.create_operation("banana")
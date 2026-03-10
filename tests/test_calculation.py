from app.calculation import Calculation


def test_calculation_creation():
    calc = Calculation("add", 2, 3, 5)

    assert calc.operation == "add"
    assert calc.operand1 == 2
    assert calc.operand2 == 3
    assert calc.result == 5
    assert calc.timestamp is not None


def test_calculation_to_dict():
    calc = Calculation("multiply", 4, 5, 20)
    calc_dict = calc.to_dict()

    assert calc_dict["operation"] == "multiply"
    assert calc_dict["operand1"] == 4
    assert calc_dict["operand2"] == 5
    assert calc_dict["result"] == 20
    assert "timestamp" in calc_dict


def test_calculation_str():
    calc = Calculation("subtract", 10, 4, 6)
    assert str(calc) == "subtract(10, 4) = 6"
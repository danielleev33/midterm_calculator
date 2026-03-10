from app.calculation import Calculation
from app.calculator_memento import CalculatorMemento


def test_memento_stores_history_state():
    history_state = [Calculation("add", 2, 3, 5)]
    memento = CalculatorMemento(history_state)

    saved_state = memento.get_state()

    assert len(saved_state) == 1
    assert saved_state[0].operation == "add"
    assert saved_state[0].result == 5


def test_memento_returns_copy_of_state():
    history_state = [Calculation("add", 2, 3, 5)]
    memento = CalculatorMemento(history_state)

    saved_state = memento.get_state()
    saved_state.append(Calculation("multiply", 2, 4, 8))

    assert len(memento.get_state()) == 1
import os
import pytest

from app.calculation import Calculation
from app.exceptions import HistoryError
from app.history import History


def test_add_calculation():
    history = History()
    calc = Calculation("add", 2, 3, 5)

    history.add_calculation(calc)

    assert len(history.get_history()) == 1
    assert history.get_history()[0].operation == "add"


def test_clear_history():
    history = History()
    history.add_calculation(Calculation("add", 2, 3, 5))
    history.clear_history()

    assert history.get_history() == []


def test_save_to_csv(tmp_path):
    history = History()
    history.add_calculation(Calculation("multiply", 4, 5, 20))

    file_path = tmp_path / "history.csv"
    history.save_to_csv(file_path)

    assert os.path.exists(file_path)


def test_load_from_csv(tmp_path):
    history = History()
    history.add_calculation(Calculation("subtract", 10, 4, 6))

    file_path = tmp_path / "history.csv"
    history.save_to_csv(file_path)

    new_history = History()
    new_history.load_from_csv(file_path)

    loaded = new_history.get_history()
    assert len(loaded) == 1
    assert loaded[0].operation == "subtract"
    assert loaded[0].operand1 == 10
    assert loaded[0].operand2 == 4
    assert loaded[0].result == 6


def test_load_missing_file():
    history = History()

    with pytest.raises(HistoryError):
        history.load_from_csv("does_not_exist.csv")


def test_load_invalid_csv(tmp_path):
    file_path = tmp_path / "bad_history.csv"
    file_path.write_text("bad,column\n1,2\n", encoding="utf-8")

    history = History()

    with pytest.raises(HistoryError):
        history.load_from_csv(file_path)
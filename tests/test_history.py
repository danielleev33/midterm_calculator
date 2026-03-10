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


def test_history_respects_max_size(monkeypatch):
    from app.calculator_config import CalculatorConfig

    monkeypatch.setattr(CalculatorConfig, "MAX_HISTORY_SIZE", 2)

    history = History()
    history.add_calculation(Calculation("add", 1, 1, 2))
    history.add_calculation(Calculation("add", 2, 2, 4))
    history.add_calculation(Calculation("add", 3, 3, 6))

    saved = history.get_history()
    assert len(saved) == 2
    assert saved[0].operand1 == 2
    assert saved[1].operand1 == 3


def test_save_to_csv_raises_history_error(monkeypatch):
    history = History()
    history.add_calculation(Calculation("add", 2, 3, 5))

    def bad_to_csv(*args, **kwargs):
        raise Exception("save failed")

    monkeypatch.setattr("pandas.DataFrame.to_csv", bad_to_csv)

    with pytest.raises(HistoryError):
        history.save_to_csv("fake.csv")


def test_load_from_csv_raises_history_error_for_bad_read(monkeypatch):
    history = History()

    def bad_read_csv(*args, **kwargs):
        raise Exception("read failed")

    monkeypatch.setattr("pandas.read_csv", bad_read_csv)
    monkeypatch.setattr("os.path.exists", lambda path: True)

    with pytest.raises(HistoryError):
        history.load_from_csv("fake.csv")


def test_save_and_load_empty_history(tmp_path):
    history = History()
    file_path = tmp_path / "empty_history.csv"

    history.save_to_csv(file_path)

    new_history = History()
    new_history.load_from_csv(file_path)

    assert new_history.get_history() == []
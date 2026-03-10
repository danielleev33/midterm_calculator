from app.calculator import Calculator
from app.logger import LoggingObserver, AutoSaveObserver, get_logger


def test_get_logger_returns_logger():
    logger = get_logger()
    assert logger is not None


def test_logging_observer_is_registered_and_runs():
    calculator = Calculator()
    observer = LoggingObserver()
    calculator.add_observer(observer)

    result = calculator.calculate("add", 2, 3)

    assert result == 5
    assert len(calculator.get_history()) == 1


def test_autosave_observer_is_registered_and_runs(tmp_path):
    calculator = Calculator()
    calculator.history.save_to_csv = lambda file_path=None: None

    observer = AutoSaveObserver()
    calculator.add_observer(observer)

    result = calculator.calculate("multiply", 4, 5)

    assert result == 20
    assert len(calculator.get_history()) == 1
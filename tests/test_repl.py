import builtins

from app.calculator import run_repl


def test_repl_exit(monkeypatch, capsys):
    inputs = iter(["exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    run_repl()

    captured = capsys.readouterr()
    assert "Exiting calculator" in captured.out


def test_repl_help_then_exit(monkeypatch, capsys):
    inputs = iter(["help", "exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    run_repl()

    captured = capsys.readouterr()
    assert "Available commands:" in captured.out
    assert "add a b" in captured.out


def test_repl_add_then_exit(monkeypatch, capsys):
    inputs = iter(["add 2 3", "exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    run_repl()

    captured = capsys.readouterr()
    assert "Result:" in captured.out


def test_repl_history_then_exit(monkeypatch, capsys):
    inputs = iter(["add 2 3", "history", "exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    run_repl()

    captured = capsys.readouterr()
    assert "add(" in captured.out


def test_repl_unknown_command(monkeypatch, capsys):
    inputs = iter(["banana", "exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    run_repl()

    captured = capsys.readouterr()
    assert "Unknown command" in captured.out


def test_repl_bad_argument_count(monkeypatch, capsys):
    inputs = iter(["add 2", "exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    run_repl()

    captured = capsys.readouterr()
    assert "Usage: add <a> <b>" in captured.out


def test_repl_undo_redo_empty(monkeypatch, capsys):
    inputs = iter(["undo", "redo", "exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    run_repl()

    captured = capsys.readouterr()
    assert "Nothing to undo." in captured.out
    assert "Nothing to redo." in captured.out


def test_repl_clear_and_history(monkeypatch, capsys):
    inputs = iter(["add 2 3", "clear", "history", "exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    run_repl()

    captured = capsys.readouterr()
    assert "History cleared." in captured.out
    assert "History is empty." in captured.out


def test_repl_save_and_load(monkeypatch, capsys):
    inputs = iter(["save", "load", "exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    run_repl()

    captured = capsys.readouterr()
    assert "History saved successfully." in captured.out
    assert "History loaded successfully." in captured.out


def test_repl_exception_handling(monkeypatch, capsys):
    inputs = iter(["divide 10 0", "exit"])
    monkeypatch.setattr(builtins, "input", lambda _: next(inputs))

    run_repl()

    captured = capsys.readouterr()
    assert "Error:" in captured.out
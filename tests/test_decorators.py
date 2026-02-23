import pytest

from src.decorators import log


def test_log_success_console(capsys):
    @log()
    def add(x: int, y: int) -> int:
        return x + y

    result = add(1, 2)
    assert result == 3
    captured = capsys.readouterr()
    assert "add called" in captured.err
    assert "add ok" in captured.err


def test_log_error_console(capsys):
    @log()
    def divide(x: int, y: int) -> int:
        return x // y

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
    captured = capsys.readouterr()
    assert "divide called" in captured.err
    assert "divide error: ZeroDivisionError" in captured.err


def test_log_success_file(tmp_path):
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def multiply(x: int, y: int) -> int:
        return x * y

    result = multiply(3, 4)
    assert result == 12
    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()
    assert "multiply called" in content
    assert "multiply ok" in content


def test_log_error_file(tmp_path):
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def bad_func(x: str) -> int:
        raise ValueError("bad input")

    with pytest.raises(ValueError):
        bad_func("test")
    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()
    assert "bad_func called" in content
    assert "bad_func error: ValueError. Inputs: ('test',), {}" in content

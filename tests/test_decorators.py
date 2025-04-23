import os

import pytest

from src.decorators import log


@pytest.fixture
def log_file(tmp_path):
    filename = tmp_path / "test_log.txt"
    yield filename
    if os.path.exists(filename):
        os.remove(filename)


def test_log_to_console(capsys):
    @log()
    def add(a: int, b: int) -> int:
        return a + b

    add(2, 3)
    captured = capsys.readouterr()
    assert "add - Args: (2, 3), Kwargs: {} - Result: 5" in captured.out


def test_log_to_file(log_file):
    @log(filename=log_file)
    def multiply(a: int, b: int) -> int:
        return a * b

    multiply(3, 4)
    with open(log_file, "r", encoding="utf-8") as file:
        log_content = file.read()
    assert "multiply - Args: (3, 4), Kwargs: {} - Result: 12" in log_content


def test_log_error_to_console(capsys):
    @log()
    def divide(a: int, b: int) -> float:
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
    captured = capsys.readouterr()
    assert "divide - Args: (1, 0), Kwargs: {} - Error: division by zero" in captured.out


def test_log_error_to_file(log_file):
    @log(filename=log_file)
    def subtract(a: int, b: int) -> int:
        if a < b:
            raise ValueError("a must be greater than b")
        return a - b

    with pytest.raises(ValueError):
        subtract(1, 2)
    with open(log_file, "r", encoding="utf-8") as file:
        log_content = file.read()
    assert "subtract - Args: (1, 2), Kwargs: {} - Error: a must be greater than b" in log_content

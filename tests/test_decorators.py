import pytest

from src.decorators import log


def test_log_without_filename_success(capsys):
    @log()
    def simple_func(x, y):
        return x + y

    result = simple_func(2, 3)
    assert result == 5

    captured = capsys.readouterr()
    assert captured.out == "simple_func ok\n"
    assert captured.err == ""


def test_log_with_filename_success(tmp_path):
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def simple_func(x, y):
        return x + y

    result = simple_func(2, 3)
    assert result == 5

    with open(log_file, "r") as f:
        assert f.read() == "simple_func ok\n"


def test_log_without_filename_error(capsys):
    @log()
    def error_func(x):
        return x / 0

    with pytest.raises(ZeroDivisionError):
        error_func(5)

    captured = capsys.readouterr()
    assert "error_func error: ZeroDivisionError. Inputs: (5,), {}" in captured.out
    assert captured.err == ""


def test_log_with_filename_error(tmp_path):
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def error_func(x, y=10):
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        error_func(5, y=20)

    with open(log_file, "r") as f:
        log_content = f.read()
        assert "error_func error: ValueError. Inputs: (5,), {'y': 20}" in log_content


def test_log_multiple_calls(capsys):
    @log()
    def simple_func(x):
        return x * 2

    result1 = simple_func(3)
    result2 = simple_func(4)

    assert result1 == 6
    assert result2 == 8

    captured = capsys.readouterr()
    assert captured.out == "simple_func ok\nsimple_func ok\n"


def test_log_with_filename_multiple_calls(tmp_path):
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def simple_func(x):
        return x * 2

    simple_func(3)
    simple_func(4)

    with open(log_file, "r") as f:
        content = f.read().splitlines()
        assert len(content) == 2
        assert content[0] == "simple_func ok"
        assert content[1] == "simple_func ok"


def test_log_different_exceptions(tmp_path):
    log_file = tmp_path / "test.log"

    @log(filename=str(log_file))
    def error_func(x):
        if x > 0:
            raise ValueError("Positive")
        raise TypeError("Negative")

    with pytest.raises(ValueError):
        error_func(1)

    with pytest.raises(TypeError):
        error_func(-1)

    with open(log_file, "r") as f:
        content = f.read().splitlines()
        assert "error_func error: ValueError. Inputs: (1,), {}" in content[0]
        assert "error_func error: TypeError. Inputs: (-1,), {}" in content[1]

from unittest.mock import patch

from src.external_api import convert_to_rub
from src.file_reader import read_json_file


def test_read_json_file():
    result = read_json_file("data/operations.json")
    print(f"Result: {result}")
    assert isinstance(result, list)
    if result:
        assert result != []


@patch("requests.get")
def test_convert_currency(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": 75.0}

    transaction = {"amount": 1, "currency": "USD"}
    assert convert_to_rub(transaction) == 75.0

    transaction = {"amount": 1, "currency": "RUB"}
    assert convert_to_rub(transaction) == 1.0

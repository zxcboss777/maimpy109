import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
    ]


# Тест по USD
def test_filter_by_currency_usd(transactions):
    result = list(filter_by_currency(transactions, "USD"))
    assert len(result) == 2  # 2 транзакции в USD
    assert result[0]["id"] == 939719570
    assert result[1]["id"] == 142264268


# Тест по RUB
def test_filter_by_currency_rub(transactions):
    result = list(filter_by_currency(transactions, "RUB"))
    assert len(result) == 1  # 1 транзакция в RUB
    assert result[0]["id"] == 873106923


def test_card_number_generator_range():
    start = 1
    end = 5
    expected_output = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
    result = list(card_number_generator(start, end))
    assert result == expected_output


# Тест корректности форматирования
def test_card_number_generator_formatting():
    start = 9999999999999995
    end = 9999999999999999
    expected_output = [
        "9999 9999 9999 9995",
        "9999 9999 9999 9996",
        "9999 9999 9999 9997",
        "9999 9999 9999 9998",
        "9999 9999 9999 9999",
    ]
    result = list(card_number_generator(start, end))
    assert result == expected_output


# Тест обработки крайних значений диапазона
def test_card_number_generator_edge_cases():
    # Минимальное значение
    start = 0
    end = 1
    expected_output = ["0000 0000 0000 0000", "0000 0000 0000 0001"]
    result = list(card_number_generator(start, end))
    assert result == expected_output

    # Максимальное значение
    start = 9999999999999998
    end = 9999999999999999
    expected_output = ["9999 9999 9999 9998", "9999 9999 9999 9999"]
    result = list(card_number_generator(start, end))
    assert result == expected_output


def test_transaction_descriptions(transactions):
    descriptions = list(transaction_descriptions(transactions))
    expected_descriptions = ["Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет"]
    assert descriptions == expected_descriptions


# Тест работы с пустым списком
def test_transaction_descriptions_empty_list():
    descriptions = list(transaction_descriptions([]))
    assert descriptions == []  # Ожидаем пустой список


# Тест работы с одной транзакцией
def test_transaction_descriptions_single_transaction():
    single_transaction = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    ]
    descriptions = list(transaction_descriptions(single_transaction))
    assert descriptions == ["Перевод организации"]

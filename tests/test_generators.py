import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def sample_transactions() -> list[dict]:
    return [
        {
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Payment for services",
        },
        {
            "operationAmount": {"currency": {"code": "EUR"}},
            "description": "Grocery shopping",
        },
        {
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Online purchase",
        },
    ]


def test_filter_by_currency(sample_transactions: list[dict]) -> None:
    usd_transactions = filter_by_currency(sample_transactions, "USD")
    assert next(usd_transactions)["description"] == "Payment for services"
    assert next(usd_transactions)["description"] == "Online purchase"
    with pytest.raises(StopIteration):
        next(usd_transactions)


def test_transaction_descriptions(sample_transactions: list[dict]) -> None:
    descriptions = transaction_descriptions(sample_transactions)
    assert next(descriptions) == "Payment for services"
    assert next(descriptions) == "Grocery shopping"
    assert next(descriptions) == "Online purchase"
    with pytest.raises(StopIteration):
        next(descriptions)


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 2, ["0000 0000 0000 0001"]),
        (9999, 10001, ["0000 0000 0000 9999", "0000 0000 0001 0000"]),
    ],
)
def test_card_number_generator(start: int, stop: int, expected: list[str]) -> None:
    generator = card_number_generator(start, stop)
    for exp in expected:
        assert next(generator) == exp
    with pytest.raises(StopIteration):
        next(generator)

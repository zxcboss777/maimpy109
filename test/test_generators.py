import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def sample_transactions():
    return [
        {"currency": "USD", "amount": 100, "description": "Payment 1"},
        {"currency": "EUR", "amount": 200, "description": "Payment 2"},
        {"currency": "USD", "amount": 300, "description": "Payment 3"},
    ]


@pytest.mark.parametrize(
    "currency, expected_count",
    [("USD", 2), ("EUR", 1), ("GBP", 0)],
)
def test_filter_by_currency(sample_transactions, currency, expected_count):
    filtered = list(filter_by_currency(sample_transactions, currency))
    assert len(filtered) == expected_count
    for transaction in filtered:
        assert transaction["currency"] == currency


def test_transaction_descriptions(sample_transactions):
    descriptions = list(transaction_descriptions(sample_transactions))
    assert descriptions == ["Payment 1", "Payment 2", "Payment 3"]


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (1, 2, ["0000 0000 0000 0001"]),
        (9999, 10001, ["0000 0000 0000 9999", "0000 0000 0001 0000"]),
    ],
)
def test_card_number_generator(start, stop, expected):
    generated = list(card_number_generator(start, stop))
    assert generated == expected
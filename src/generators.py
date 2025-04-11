# generators.py

from typing import Dict, Iterator, List, Generator


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """
    Фильтрует транзакции по заданной валюте и возвращает итератор.

    Args:
        transactions: Список словарей с транзакциями.
        currency: Код валюты для фильтрации (например, "USD", "RUB").

    Yields:
        Словарь транзакции, если её валюта совпадает с заданной.
    """
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: List[Dict]) -> Generator[str, None, None]:
    """
    Генератор, который возвращает описания транзакций.

    Args:
        transactions: Список словарей с транзакциями.

    Yields:
        Описание каждой транзакции.
    """
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Generator[str, None, None]:
    """
    Генератор номеров банковских карт в формате "XXXX XXXX XXXX XXXX".

    Args:
        start: Начальное значение номера карты.
        stop: Конечное значение номера карты (не включается).

    Yields:
        Строка с номером карты.
    """
    for num in range(start, stop):
        card_num = f"{num:016d}"
        yield " ".join([card_num[i : i + 4] for i in range(0, 16, 4))


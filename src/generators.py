from typing import Dict, Iterable, Iterator


def filter_by_currency(transactions: Iterable[Dict], currency: str) -> Iterator[Dict]:
    """
    Фильтрует транзакции по заданной валюте и возвращает итератор.

    :param transactions: Список транзакций (словарей)
    :param currency: Код валюты для фильтрации (например, "USD")
    :return: Итератор по транзакциям с указанной валютой
    """
    for transaction in transactions:
        if transaction.get("currency") == currency:
            yield transaction


def transaction_descriptions(transactions: Iterable[Dict]) -> Iterator[str]:
    """
    Генератор, который возвращает описания транзакций.

    :param transactions: Список транзакций (словарей)
    :return: Итератор по описаниям транзакций
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генератор номеров банковских карт в формате "XXXX XXXX XXXX XXXX".

    :param start: Начальное значение диапазона (включительно)
    :param stop: Конечное значение диапазона (не включая)
    :return: Итератор по номерам карт
    """
    for number in range(start, stop):
        card_number = f"{number:016d}"
        yield " ".join([card_number[i : i + 4] for i in range(0, 16, 4)])

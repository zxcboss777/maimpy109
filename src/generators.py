# generators.py

from typing import Dict, List, Iterator, Generator
from typing import List, Dict, Iterator


def filter_by_currency(transactions: List[Dict], currency: str) -> Iterator[Dict]:
    """
    Фильтрует транзакции по заданной валюте.
    :param transactions: Список транзакций.
    :param currency: Код валюты для фильтрации.
    :return: Итератор, возвращающий транзакции с указанной валютой.
    Возвращает итератор по транзакциям, у которых валюта совпадает с переданной.
    :param transactions: Список словарей с информацией о транзакциях.
                         Каждый словарь предполагается в формате:
                             {
                                "amount": float,
                                "currency": str,
                                "description": str,
                                ...
                             }
    :param currency: Искомая валюта (например, 'USD').
    :return: Итератор словарей, соответствующих указанной валюте.
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction
    for tx in transactions:
        if tx.get("currency") == currency:
            yield tx

    """
    Генерирует описания транзакций.
    Генератор, возвращающий описание каждой транзакции.
    :param transactions: Список транзакций.
    :return: Генератор, возвращающий описания транзакций.
    :param transactions: Список словарей с информацией о транзакциях.
    :return: Итератор строк (описаний транзакций).
    """
    for transaction in transactions:
        yield transaction["description"]
    for tx in transactions:
        yield tx.get("description", "")


def card_number_generator(start: int, end: int) -> Generator[str, None, None]:
def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """
    Генерирует номера банковских карт в заданном диапазоне.
    Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.
    Числовые значения генерируются от 'start' до 'stop' включительно.
    :param start: Начальное значение диапазона.
    :param end: Конечное значение диапазона.
    :return: Генератор, возвращающий номера карт в формате XXXX XXXX XXXX XXXX.
    :param start: Начальное число для генерации (например, 1).
    :param stop: Конечное число для генерации (например, 9999999999999999).
    :return: Итератор строк в формате 'XXXX XXXX XXXX XXXX'.
    """
    for number in range(start, stop + 1):
        yield f"{number:016d}"[:4] + " " + f"{number:016d}"[4:8] + " " + f"{number:016d}"[
                                                                         8:12] + " " + f"{number:016d}"[12:16]
    for num in range(start, stop + 1):
        # Преобразуем число в 16-значную строку с ведущими нулями.
        card_str = str(num).zfill(16)
        # Форматируем в виде XXXX XXXX XXXX XXXX
        formatted = f"{card_str[:4]} {card_str[4:8]} {card_str[8:12]} {card_str[12:16]}"
        yield formatted








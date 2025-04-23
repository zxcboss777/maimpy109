import logging
from datetime import datetime

from src.masks import mask_account_number, mask_card_number


def mask_account_card(input_data: str) -> str:
    """Определяет тип данных (счёт/карта) и маскирует соответствующим образом."""
    card_list = input_data.split()
    number = card_list.pop()
    name = " ".join(card_list)
    if name == "Счет":
        return f"Счет {mask_account_number(number)}"
    else:
        return f"{name} {mask_card_number(number)}"


def get_date(date_str: str) -> str:
    """Парсит дату из формата ISO в DD.MM.YYYY."""
    try:
        dt = datetime.strptime(date_str.strip(), "%Y-%m-%dT%H:%M:%S")
        formatted_date = dt.strftime("%d.%m.%Y")
        return formatted_date
    except ValueError as e:
        raise ValueError(f"Invalid date format: {date_str}")

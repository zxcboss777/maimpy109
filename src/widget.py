import re
from src.masks import get_mask_card_number, get_mask_account
from datetime import datetime

    def mask_account_card(account_info: str) -> str:
    """
    Маскирует номер карты или счета.

    Args:
        account_info (str): Строка формата 'Visa Platinum 7000792289606361'
                            или 'Счет 73654108430135874305'.

    Returns:
        str: Строка с замаскированным номером.
    """
    # Разделяем строку на название и номер
    match = re.match(r"(.*?)(\d+)$", account_info)
    if not match:
        raise ValueError("Неверный формат входных данных")

    name, number = match.groups()

    # Применяем соответствующую маскировку
if name.strip().startswith("Счет"):
    return f"{name} {get_mask_account(number)}"
else:
    return f"{name} {get_mask_card_number(number)}"

    









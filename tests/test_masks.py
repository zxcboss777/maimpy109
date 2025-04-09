import pytest


from src.masks import get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", '7000 79 ** 6361'),  # Нормальный номер карты
        ("700079228960", '7000 79 ** 8960'),  # Меньше 16 символов
        ("70007922896063618091", '7000 79 ** 8091'),  # Больше 16 символов
        ("", "**   **"),  # Пустое значение
        ("abcddefghjkltyui", "abcd de ** tyui"),  # Нецифровые символы
    ],
)
def get_mask_card_number(card_number: str) -> str:
    if not card_number:
        return "**   **"

    # Mask logic for normal card numbers (, only digits)
    if len(card_number) == 16 and card_number.isdigit():
        return f"{card_number[:4]} {card_number[4:6]} ** {card_number[-4:]}"

    # Mask logic for card numbers that are not 16 digits but contain only digits
    elif card_number.isdigit():
        return f"{card_number[:4]} {card_number[4:6]} ** {card_number[-4:]}"

    # Mask logic for non-numeric input (for strings with non-digit characters)
    elif len(card_number) > 0:
        return f"{card_number[:4]} {card_number[4:6]}**card_number[-4:]"
    return "**   **"  # For invalid or empty input

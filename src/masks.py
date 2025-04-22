import logging
from datetime import datetime

# Настройка логгера
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Добавляем обработчик для вывода в консоль (можно также настроить запись в файл)
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


def mask_account_number(account_number: str) -> str:
    """Маскирует номер счёта."""
    logger.info(f"Начало работы функции mask_account_number для номера: {account_number}")
    account_number = account_number.strip()
    if not account_number:
        logger.warning("Получена пустая строка для маскировки счёта")
        return ""
    if len(account_number) < 4:
        logger.debug(f"Номер счёта короче 4 символов: {account_number}")
        return "**" + account_number
    masked_number = "**" + account_number[-4:]
    logger.info(f"Счёт успешно замаскирован: {masked_number}")
    return masked_number


def mask_card_number(card_number: str) -> str:
    """Маскирует номер карты."""
    logger.info(f"Начало работы функции mask_card_number для номера: {card_number}")
    card_number = card_number.strip()
    if not card_number:
        logger.warning("Получена пустая строка для маскировки карты")
        return ""
    if len(card_number) < 8:
        logger.warning(f"Номер карты короче 8 символов: {card_number}")
        return card_number
    masked_number = (f"{card_number[:4]} {card_number[4:6]}** ****"
    f" {card_number[-4:]})
    logger.info(f"Карта успешно замаскирована: {masked_number}")
    return masked_number










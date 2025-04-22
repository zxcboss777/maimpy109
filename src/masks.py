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
    masked_number = f"{card_number[:4]} {card_number[4:6]} ** {card_number[-4:]}"
    logger.info(f"Карта успешно замаскирована: {masked_number}")
    return masked_number


def mask_account_card(input_data: str) -> str:
    """Определяет тип данных (счёт/карта) и маскирует соответствующим образом."""
    logger.info(f"Начало работы функции mask_account_card для данных: {input_data}")
    input_data = input_data.strip()
    if not input_data:
        logger.warning("Получена пустая строка для маскировки")
        return ""
    if input_data.startswith("Счет "):
        account_number = input_data[len("Счет "):].strip()
        masked = "Счет " + mask_account_number(account_number)
        logger.info(f"Результат маскировки счёта: {masked}")
        return masked
    else:
        parts = input_data.rsplit(" ", 1)
        if len(parts) < 2:
            logger.warning(f"Не удалось разделить тип карты и номер: {input_data}")
            return input_data
        card_type, number = parts
        masked = card_type + " " + mask_card_number(number)
        logger.info(f"Результат маскировки карты: {masked}")
        return masked


def get_date(date_str: str) -> str:
    """Парсит дату из формата ISO в DD.MM.YYYY."""
    logger.info(f"Начало работы функции get_date для строки: {date_str}")
    try:
        dt = datetime.strptime(date_str.strip(), '%Y-%m-%dT%H:%M:%S')
        formatted_date = dt.strftime('%d.%m.%Y')
        logger.info(f"Дата успешно преобразована: {formatted_date}")
        return formatted_date
    except ValueError as e:
        logger.error(f"Ошибка преобразования даты {date_str}: {e}")
        raise ValueError(f"Invalid date format: {date_str}")







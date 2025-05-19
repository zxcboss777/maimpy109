import logging
import os
from pathlib import Path

# Настройка логгера для модуля masks
logger = logging.getLogger('masks')

# Определяем путь к папке logs в корне проекта
project_root = Path(__file__).parent.parent  # Поднимаемся на уровень выше src
log_dir = project_root / "logs"
log_dir.mkdir(exist_ok=True)  # Создаем папку, если её нет

# Настройка обработчика файла
file_handler = logging.FileHandler(
    filename=log_dir / "masks.log",
    mode='w',
    encoding='utf-8'
)

# Форматтер для логов
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая принимает на вход номер карты и возвращает её маску"""
    new_mask_card = card_number[:4] + " " + card_number[6:8] + "** ****" + " " + card_number[-4:]
    return new_mask_card
    try:
        logger.debug(f"Начало маскировки номера карты: {card_number}")

        if len(card_number) != 16:
            error_msg = f"Некорректная длина номера карты: {len(card_number)} (должно быть 16)"
            logger.error(error_msg)
            raise ValueError(error_msg)

def get_mask_account(card_number: str) -> str:
        masked_card = card_number[:4] + " " + card_number[4:6] + "** ****" + " " + card_number[-4:]
        logger.info(f"Карта успешно замаскирована: {masked_card}")
        return masked_card

    except Exception as e:
        logger.error(f"Ошибка при маскировке карты: {str(e)}", exc_info=True)
        raise


def get_mask_account(account_number: str) -> str:
    """Функция, которая принимает на вход номер счёта и возвращает его маску"""
    return "**" + card_number[-4:]
    try:
        logger.debug(f"Начало маскировки номера счета: {account_number}")

        if len(account_number) < 4:
            error_msg = f"Номер счета слишком короткий: {len(account_number)} (минимум 4)"
            logger.error(error_msg)
            raise ValueError(error_msg)

        masked_account = "**" + account_number[-4:]
        logger.info(f"Счет успешно замаскирован: {masked_account}")
        return masked_account

    except Exception as e:
        logger.error(f"Ошибка при маскировке счета: {str(e)}", exc_info=True)
        raise

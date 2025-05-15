import json
import logging
from pathlib import Path

import requests

# Настройка логгера для модуля utils
logger = logging.getLogger("utils")

# Определяем путь к папке logs в корне проекта
project_root = Path(__file__).parent.parent  # Поднимаемся на уровень выше src
log_dir = project_root / "logs"
log_dir.mkdir(exist_ok=True)  # Создаем папку, если её нет

# Настройка обработчика файла
file_handler = logging.FileHandler(filename=log_dir / "utils.log", mode="w", encoding="utf-8")

# Форматтер для логов
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

url = "https://drive.google.com/file/d/1C0bUdTxUhck-7BoqXSR1wIEp33BH5YXy/view"


def load_transactions(url):
    """Функция для загрузки транзакций по URL"""
    try:
        logger.debug(f"Начало загрузки транзакций. URL: {url}")

        response = requests.get(url)
        logger.debug(f"Получен ответ сервера. Статус: {response.status_code}")

        response.raise_for_status()
        logger.info("HTTP-запрос выполнен успешно")

        data = response.json()
        logger.debug(f"Получено данных: {len(data) if isinstance(data, list) else 1}")

        if isinstance(data, list):
            logger.info(f"Успешно загружено {len(data)} транзакций")
            return data
        else:
            logger.warning("Полученные данные не являются списком")
            return []

    except requests.RequestException as e:
        logger.error(f"Ошибка при выполнении запроса: {str(e)}", exc_info=True)
        return []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка декодирования JSON: {str(e)}", exc_info=True)
        return []
    except Exception as e:
        logger.error(f"Неожиданная ошибка: {str(e)}", exc_info=True)
        return []

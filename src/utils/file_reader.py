import json
from typing import Dict, List

import pandas as pd

from ..utils import utils_logger


def read_json_file(file_path: str) -> list:
    utils_logger.debug(f"Попытка чтения файла: {file_path}")
def read_transactions_from_csv(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из CSV-файла.
    Args:
        file_path (str): Путь к CSV-файлу.
    Returns:
        List[Dict]: Список словарей с транзакциями.
    """
    try:
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        raise ValueError(f"Ошибка при чтении CSV-файла: {e}")


def read_transactions_from_excel(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из Excel-файла.
    Args:
        file_path (str): Путь к Excel-файлу.
    Returns:
        List[Dict]: Список словарей с транзакциями.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                utils_logger.info(f"Файл {file_path} успешно прочитан")
                return data
            else:
                utils_logger.warning(f"Файл {file_path} не содержит список")
                return []
    except (FileNotFoundError, json.JSONDecodeError) as e:
        utils_logger.error(f"Ошибка при чтении файла {file_path}: {e}")
        return []
        df = pd.read_excel(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        raise ValueError(f"Ошибка при чтении Excel-файла: {e}")


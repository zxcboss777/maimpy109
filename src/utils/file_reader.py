import json
from typing import List, Dict
from ..utils import utils_logger


def read_json_file(file_path: str) -> List[Dict]:
def read_json_file(file_path: str) -> list:
    utils_logger.debug(f"Попытка чтения файла: {file_path}")
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                utils_logger.info(f"Файл {file_path} успешно прочитан")
                return data
            else:
                utils_logger.warning(f"Файл {file_path} не содержит список")
                return []
    except (FileNotFoundError, json.JSONDecodeError):
    except (FileNotFoundError, json.JSONDecodeError) as e:
        utils_logger.error(f"Ошибка при чтении файла {file_path}: {e}")
        return []


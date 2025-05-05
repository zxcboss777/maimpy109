# src/utils/file_reader.py
from typing import List, Dict, Any
import json
import pandas as pd
from typing import List, Dict


def read_transactions_from_csv(path: str) -> List[Dict[str, Any]]:
def read_transactions_from_csv(file_path: str) -> List[Dict]:
    """
    Прочитать CSV-файл с транзакциями и вернуть список словарей.
    При любой ошибке чтения выбрасывает ValueError с понятным сообщением.
    Считывает финансовые операции из CSV-файла.
    Args:
        file_path (str): Путь к CSV-файлу.
    Returns:
        List[Dict]: Список словарей с транзакциями.
    """
    try:
        df = pd.read_csv(path)                     # <-- патчируется tests/test_file_reader.py
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")
    except Exception as exc:
        raise ValueError(f"Ошибка при чтении CSV-файла: {exc}")
    except Exception as e:
        raise ValueError(f"Ошибка при чтении CSV-файла: {e}")


def read_transactions_from_excel(path: str) -> List[Dict[str, Any]]:
def read_transactions_from_excel(file_path: str) -> List[Dict]:
    """
    Прочитать Excel-файл с транзакциями и вернуть список словарей.
    При любой ошибке чтения выбрасывает ValueError с понятным сообщением.
    Считывает финансовые операции из Excel-файла.
    Args:
        file_path (str): Путь к Excel-файлу.
    Returns:
        List[Dict]: Список словарей с транзакциями.
    """
    try:
        df = pd.read_excel(path)                   # <-- патчируется tests/test_file_reader.py
        df = pd.read_excel(file_path)  # Changed from read_csv to read_excel
        return df.to_dict(orient="records")
    except Exception as exc:
        raise ValueError(f"Ошибка при чтении Excel-файла: {exc}")
    except Exception as e:
        raise ValueError(f"Ошибка при чтении Excel-файла: {e}")


def read_transactions_from_json(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из JSON-файла.
    Args:
        file_path (str): Путь к JSON-файлу.
    Returns:
        List[Dict]: Список словарей с транзакциями.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


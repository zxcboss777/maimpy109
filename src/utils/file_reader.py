import pandas as pd
from typing import List, Dict


def read_transactions_from_json(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из JSON-файла.

    Args:
        file_path (str): Путь к JSON-файлу.

    Returns:
        List[Dict]: Список словарей с транзакциями.
    """
    import json
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


def read_transactions_from_csv(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из CSV-файла.

    Args:
        file_path (str): Путь к CSV-файлу.

    Returns:
        List[Dict]: Список словарей с транзакциями.
    """
    df = pd.read_csv(file_path)
    return df.to_dict(orient="records")


def read_transactions_from_excel(file_path: str) -> List[Dict]:
    """
    Считывает финансовые операции из Excel-файла.

    Args:
        file_path (str): Путь к Excel-файлу.

    Returns:
        List[Dict]: Список словарей с транзакциями.
    """
    df = pd.read_excel(file_path)
    return df.to_dict(orient="records")


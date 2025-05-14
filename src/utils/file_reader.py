import pandas as pd
import json
from typing import List, Dict


def read_json_file(file_path: str) -> List[Dict]:
    """Читает транзакции из JSON файла"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Ошибка при чтении JSON: {e}")
        return []

def read_csv_file(file_path: str) -> List[Dict]:
    """Читает транзакции из CSV файла"""
    try:
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        print(f"Ошибка при чтении CSV: {e}")
        return []

def read_excel_file(file_path: str) -> List[Dict]:
    """Читает транзакции из Excel файла"""
    try:
        df = pd.read_excel(file_path)
        return df.to_dict(orient="records")
    except Exception as e:
        print(f"Ошибка при чтении Excel: {e}")
        return []

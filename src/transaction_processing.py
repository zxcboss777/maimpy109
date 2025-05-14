import re
from datetime import datetime
from typing import List, Dict

def filter_by_description(transactions: List[Dict], search_string: str) -> List[Dict]:
    """Фильтрует транзакции по описанию с использованием regex"""
    try:
        pattern = re.compile(re.escape(search_string), re.IGNORECASE)
        return [t for t in transactions if 'description' in t and pattern.search(t['description'])]
    except re.error as e:
        print(f"Ошибка в регулярном выражении: {e}")
        return transactions

def count_by_categories(transactions: List[Dict], categories: List[str]) -> Dict[str, int]:
    """Считает количество транзакций по категориям"""
    counts = {category: 0 for category in categories}
    for t in transactions:
        if 'description' in t:
            desc = t['description'].lower()
            for category in categories:
                if category.lower() in desc:
                    counts[category] += 1
    return counts

def filter_by_status(transactions: List[Dict], status: str) -> List[Dict]:
    """Фильтрует транзакции по статусу"""
    return [t for t in transactions if t.get('status', '').upper() == status.upper()]

def sort_transactions(transactions: List[Dict], reverse: bool = False) -> List[Dict]:
    """Сортирует транзакции по дате"""
    def get_date(t):
        try:
            return datetime.strptime(t['date'], '%d.%m.%Y') if 'date' in t else datetime.min
        except ValueError:
            return datetime.min
    return sorted(transactions, key=get_date, reverse=reverse)

def filter_by_currency(transactions: List[Dict], currency: str = 'RUB') -> List[Dict]:
    """Фильтрует транзакции по валюте"""
    return [t for t in transactions if t.get('currency', '').upper() == currency.upper()]

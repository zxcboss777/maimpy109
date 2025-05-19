from src.file_reader import read_json_file, read_csv_file, read_excel_file
from src.transaction_processing import (
    filter_by_description,
    count_by_categories,
    filter_by_status,
    sort_transactions,
    filter_by_currency
)
from typing import List, Dict



def print_transactions(transactions: List[Dict], limit: int = 5):
    """Печатает список транзакций"""
    for i, t in enumerate(transactions[:limit], 1):
        print(f"\n{i}. {t.get('date', 'Нет даты')} - {t.get('description', 'Нет описания')}")
        print(f"От: {t.get('from', 'Не указано')}")
        print(f"Кому: {t.get('to', 'Не указано')}")
        print(f"Сумма: {t.get('amount', 'Не указана')} {t.get('currency', '')}")


def get_file_path(default_path: str, file_type: str) -> str:
    """Запрашивает путь к файлу у пользователя"""
    user_path = input(f"Введите путь к {file_type}-файлу (или Enter для '{default_path}'): ").strip()
    return user_path if user_path else default_path


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Настройки путей по умолчанию
    DEFAULT_PATHS = {
        'JSON': 'transactions.json',
        'CSV': 'C:\\Users\\pavelk\\Downloads\\transactions.csv',
        'XLSX': 'C:\\Users\\pavelk\\Downloads\\transactions_excel.xlsx'
    }

    # Выбор источника данных
    file_readers = {
        '1': ('JSON', read_json_file),
        '2': ('CSV', read_csv_file),
        '3': ('XLSX', read_excel_file)
    }

    while True:
        print("\nВыберите источник данных:")
        for key, (name, _) in file_readers.items():
            print(f"{key}. Получить информацию о транзакциях из {name}-файла")

        choice = input("Ваш выбор (1-3): ").strip()
        if choice in file_readers:
            name, reader = file_readers[choice]
            file_path = get_file_path(DEFAULT_PATHS[name], name)
            transactions = reader(file_path)

            if transactions:
                print(f"\nУспешно загружено {len(transactions)} транзакций.")
                break
            print(f"Не удалось загрузить транзакции. Попробуйте еще раз.")

    # Фильтрация по статусу
    valid_statuses = ['EXECUTED', 'CANCELED', 'PENDING']
    while True:
        print("\nДоступные статусы:", ", ".join(valid_statuses))
        status = input("Введите статус для фильтрации (или Enter чтобы пропустить): ").upper().strip()

        if not status:
            break
        if status in valid_statuses:
            transactions = filter_by_status(transactions, status)
            print(f"Осталось {len(transactions)} транзакций после фильтрации.")
            break
        print(f"Статус '{status}' недоступен.")

    # Дополнительные фильтры
    if input("\nОтсортировать по дате? (да/нет): ").lower() == 'да':
        order = input("По возрастанию или по убыванию? (возрастание/убывание): ").lower()
        transactions = sort_transactions(transactions, order.startswith('у'))

    if input("\nВыводить только рублевые транзакции? (да/нет): ").lower() == 'да':
        transactions = filter_by_currency(transactions, 'RUB')

    if input("\nФильтровать по описанию? (да/нет): ").lower() == 'да':
        keyword = input("Введите ключевое слово: ").strip()
        transactions = filter_by_description(transactions, keyword)

    # Вывод результатов
    print(f"\nИтоговое количество транзакций: {len(transactions)}")
    if transactions:
        print("\nПримеры транзакций:")
        print_transactions(transactions)

        # Анализ по категориям
        if input("\nПроанализировать по категориям? (да/нет): ").lower() == 'да':
            categories = input("Введите категории через запятую: ").strip().split(',')
            if categories:
                counts = count_by_categories(transactions, [c.strip() for c in categories])
                print("\nКоличество транзакций по категориям:")
                for cat, count in counts.items():
                    print(f"{cat}: {count}")
    else:
        print("Нет транзакций, соответствующих критериям.")


if __name__ == "__main__":
    main()

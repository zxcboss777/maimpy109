from unittest.mock import patch, mock_open
from src.finance_operations import read_csv_transactions, read_excel_transactions

# Тест для CSV
@patch("pandas.read_csv")
def test_read_transactions_from_csv(mock_read_csv):
    """
    Тестирует функцию read_transactions_from_csv с использованием Mock.
    """
    # Создаем моковые данные
    mock_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]

    # Настройка мока для pandas.read_csv
    mock_df = mock_read_csv.return_value
    mock_df.to_dict.return_value = mock_data

    # Вызываем тестируемую функцию
    result = read_csv_transactions("mock_path.csv")

    # Проверяем результат
    assert result == mock_data


# Тест для Excel
@patch("pandas.read_excel")
def test_read_transactions_from_excel(mock_read_excel):
    """
    Тестирует функцию read_transactions_from_excel с использованием Mock.
    """
    # Создаем моковые данные
    mock_data = [{"id": 1, "amount": 100}, {"id": 2, "amount": 200}]

    # Настройка мока для pandas.read_excel
    mock_df = mock_read_excel.return_value
    mock_df.to_dict.return_value = mock_data

    # Вызываем тестируемую функцию
    result = read_excel_transactions("mock_path.xlsx")

    # Проверяем результат
    assert result == mock_data


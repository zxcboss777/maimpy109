import json
import csv
import pandas as pd
from src.transaction_filters import filter_by_description
from src.utils.file_reader import read_transactions_from_json, read_transactions_from_csv, read_transactions_from_excel

from src.utils.operation_search import operation_search


from src.utils.operation_counter import operation_counter


def load_json_data(file_path):
@@ -42,6 +47,10 @@ def print_transaction(transaction):
    print(f"Сумма: {amount} {currency}\n")


def filter_by_description(filtered_transactions, search_string):
    pass


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")



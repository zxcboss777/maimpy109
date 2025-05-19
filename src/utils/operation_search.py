def operation_search(operations, search_term):
    """
    Ищет все операции, описание которых содержит строку search_term (нечувствительно к регистру).
    Возвращает список таких операций.
    """
    return [operation for operation in operations if search_term.lower() in operation["description"].lower()]

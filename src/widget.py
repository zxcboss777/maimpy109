
def mask_account_card(account_info: str) -> str:
    """
    Маскирует номер карты или счета.

    Args:
        account_info (str): Строка формата 'Visa Platinum 7000792289606361' 
                            или 'Счет 73654108430135874305'.

    Returns:
        str: Строка с замаскированным номером.
    """
    # Разделяем строку на название и номер
    match = re.match(r"(.*?)(\d+)$", account_info)
    if not match:
        raise ValueError("Неверный формат входных данных")

    name, number = match.groups()

    # Применяем соответствующую маскировку
    if name.strip().startswith("Счет"):
        return f"{name} {mask_account_number(number)}"
    else:
        return f"{name} {mask_card_number(number)}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из ISO-формата в формат 'ДД.ММ.ГГГГ'.

    Args:
        date_str (str): Строка с датой в формате 'YYYY-MM-DDTHH:MM:SS.mmmmmm'.

    Returns:
        str: Строка с датой в формате 'ДД.ММ.ГГГГ'.
    """
    try:
        date_obj = datetime.fromisoformat(date_str)
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Неверный формат даты")
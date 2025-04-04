def get_mask_card_number(card_number: int) -> str:
    """
    Маскирует номер банковской карты.

    :param card_number: Номер банковской карты (число).
    :return: Маскированный номер карты (строка).
    """
    card_str = str(card_number)
    if len(card_str) != 16:
        raise ValueError("Номер карты должен состоять из 16 цифр.")
    masked = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
    return masked


def get_mask_account(account_number: int) -> str:
    """
    Маскирует номер банковского счета.

    :param account_number: Номер банковского счета (число).
    :return: Маскированный номер счета (строка).
    """
    account_str = str(account_number)
    if len(account_str) < 4:
        raise ValueError("Номер счета должен содержать как минимум 4 цифры.")
    masked = f"**{account_str[-4:]}"
    return masked

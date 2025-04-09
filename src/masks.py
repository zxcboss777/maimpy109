def mask_card_number(card_number):
    if not card_number:
        return "**   **"
    return card_number[:4] + " " + card_number[4:6] + " ** " + card_number[-4:]


# Алиас для функции
get_mask_card_number = mask_card_number


def mask_account_number(account_number):
    if not account_number:
        return "**"
    return "**" + account_number[-4:]


# Алиасы для функций
get_mask_account = mask_account_number




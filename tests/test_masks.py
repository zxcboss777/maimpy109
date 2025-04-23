from src.masks import mask_account_number, mask_card_number


def test_mask_card_number():
    assert mask_card_number("1234123412341234") == "1234 12** **** 1234"
    assert mask_card_number("0000000000000000") == "0000 00** **** 0000"


def test_mask_account_number():
    assert mask_account_number("1234123412341234") == "**1234"
    assert mask_account_number("0000000000000000") == "**0000"

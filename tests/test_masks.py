import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79 ** **** 6361"),
        ("712379228960", "Некорректный ввод данных"),
        ("", "Некорректный ввод данных"),
        ("6788gghg", "Некорректный ввод данных"),
    ],
)
def test_get_mask_card_number(card_number: str, expected: str):
    """Тестирование маскировки номера карты"""
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135584305", "**4305"),
        ("736541084301358", "Некорректный ввод данных"),
        ("", "Некорректный ввод данных"),
    ],
)
def test_get_mask_account(account_number: str, expected: str):
    """Тестирование маскировки номера счета"""
    assert get_mask_account(account_number) == expected

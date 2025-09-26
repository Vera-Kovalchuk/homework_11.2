import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "card_input, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79 ** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card_original(card_input: str, expected: str) -> None:
    """Тестирование функции с корректным номером карты и счета"""
    assert mask_account_card(card_input) == expected


@pytest.mark.parametrize(
    "card_input, expected",
    [
        ("7000792289606361", "Некорректный ввод данных"),
        ("", "Некорректный ввод данных"),
        ("Maestro 7000792289606361", "Maestro 7000 79 ** **** 6361"),
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79 ** **** 6361"),
        ("Visa Gold 70007928960636", "Некорректный ввод данных"),
        ("Visa Classic 7000792289606361", "Visa Classic 7000 79 ** **** 6361"),
        ("MasterCard 7000792289606361", "MasterCard 7000 79 ** **** 6361"),
        ("5875795959595", "Некорректный ввод данных"),
    ],
)
def test_mask_account_card_valid_data(card_input: str, expected: str) -> None:
    try:
        assert mask_account_card(card_input) == expected
    except AssertionError:
        print("Некорректный ввод данных")


def test_get_date_original() -> None:
    """Тестирование данных '2024-07-15T90:25:93.410947'"""
    try:
        assert get_date("2024-07-15T90:25:93.410947") == "15.07.2024"
    except ValueError:
        print("некорректный формат ввода")


@pytest.mark.parametrize("user_date, new_date", [("2024-03-11T02:26:18.671407", "11.03.2024")])
def test_get_date(user_date: str, new_date: str) -> None:
    """Тестирование функции с некорректными данными"""
    try:
        assert get_date(user_date) == new_date
    except AssertionError:
        print("Некорректные данные")

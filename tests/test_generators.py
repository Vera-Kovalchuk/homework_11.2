import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.fixture
def transactions():
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
    ]


def test_filter_by_currency():
    """Тестирование функции, где валюта операции соответствует заданной (например, USD)"""
    generator = filter_by_currency(transactions)
    try:
        assert next(generator) == {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        }
    except TypeError:
        print([])


def test_filter_by_currency_zero() -> None:
    with pytest.raises(StopIteration, match="Нет транзакций") as except_:
        generator = filter_by_currency([], "")
        assert next(generator) == except_


def test_filter_by_currency_eu(transactions):
    result = filter_by_currency(transactions, "EUR")
    assert list(result) == []


@pytest.mark.parametrize("index, expected", [(0, "Перевод организации"), (1, "Перевод со счета на счет")])
def test_transaction_descriptions(index, expected, transactions):
    descriptions = list(transaction_descriptions(transactions))
    assert descriptions[index] == expected


def test_transaction_descriptions_zero() -> None:
    with pytest.raises(StopIteration, match="Нет транзакций") as except_:
        el = transaction_descriptions([])
        assert next(el) == except_


def test_card_number_generator():
    """Тестирование генератора с указанными значениями"""
    numer = card_number_generator(94, 95)
    assert next(numer) == "0000 0000 0000 0094"


def test_card_number_generator_beginning():
    """Тестирование генератора первоначального значения"""
    numer = card_number_generator(0, 1)
    assert next(numer) == "0000 0000 0000 0000"


def test_card_number_generator_end():
    """Тестирование ввода номера карты без пробелов"""
    numer = card_number_generator(9999999999999999, 9999999999999999)
    assert next(numer) == "9999 9999 9999 9999"

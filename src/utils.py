import json
import logging
import os
from json import JSONDecodeError
from typing import Any

from src.external_api import currency_conversion

# Получаем абсолютный путь до текущей директории
current_dir = os.path.dirname(os.path.abspath(__file__))


# Создаем путь до файла логов относительно текущей директории
rel_log_file_path = os.path.join(current_dir, "../logs/utils.log")
abs_log_file_path = os.path.abspath(rel_log_file_path)


# Добавляем логгер, который записывает логи в файл.
logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(abs_log_file_path, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

financial_transactions_logger = logging.getLogger()
transaction_amount_logger = logging.getLogger()


def financial_transactions(path: str) -> list:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        financial_transactions_logger.info("Открытие файла с транзакциями")
        with open(path, encoding="utf-8") as financial_file:
            try:
                transactions = json.load(financial_file)
            except JSONDecodeError:
                financial_transactions_logger.error("Ошибка файла с транзакциями")
                return []
        if not isinstance(transactions, list):
            financial_transactions_logger.error("Список транзакций пуст")
            return []
        financial_transactions_logger.info("Создан список словарей с транзакциями")
        return transactions
    except FileNotFoundError:
        financial_transactions_logger.error("Файл с транзакциями не найден")
        return []


def transaction_amount(trans: dict, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if trans["operationAmount"]["currency"]["code"] == currency:
        amount = trans["operationAmount"]["amount"]
        transaction_amount_logger.info("Валюта в транзакциях RUB")
    else:
        amount = currency_conversion(trans)
        transaction_amount_logger.info("Результат конвертации валют")
    return amount

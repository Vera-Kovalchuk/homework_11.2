import logging

import pandas as pd

from src.utils import current_dir

PATH_TO_CSV = current_dir / "files" / "transactions.csv"
PATH_TO_EXCEL = current_dir / "files" / "transactions_excel.xlsx"

logger = logging.getLogger("files")
logger.setLevel(logging.INFO)
fileHandler = logging.FileHandler(current_dir / "logs" / "files.log", encoding="UTF-8", mode="w")
fileFormatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
fileHandler.setFormatter(fileFormatter)
logger.addHandler(fileHandler)

logger_csv = logging.getLogger("csv")
logger_xlsx = logging.getLogger("xlsx")


def read_csv(current_dir: str) -> list:
    """Функция считывает транзакции из csv-файла и преобразует в список словарей с транзакциями"""
    logger_csv.debug("Открывает csv-файл для чтения")
    try:
        reader_csv = pd.read_csv(current_dir, delimiter=";")
        logger_csv.debug("csv-файл считан")
    except FileNotFoundError:
        logger_csv.error("Файл csv не найден")
        return []
    return reader_csv.to_dict(orient="records")


def read_xlsx(current_dir: str) -> list:
    """Функция считывает транзакции из excel-файла и преобразует в список словарей с транзакциями"""
    logger_xlsx.debug("Открывает excel-файл для чтения")
    try:
        reader_xlsx = pd.read_excel(current_dir)
        logger_xlsx.debug("excel-файл считан")
    except FileNotFoundError:
        logger_xlsx.error("Файл excel не найден")
        return []
    return reader_xlsx.to_dict(orient="records")

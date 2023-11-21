import json
import logging
from typing import Any


def utils_logging() -> Any:
    logging.basicConfig(
        level=logging.DEBUG,
        filename="logging_utils.log",
        filemode="w",
        format="%(asctime)s %(name)s %(levelname)s: %(message)s",
        encoding="utf-8",
    )
    return logging.getLogger()


def deserialization_json_file(json_path: str) -> list:
    """Функция принимает параметр json_path (имя json файла), возвращает список словарей если файл найден,
    или пустой список при условии, что файла не найден или поврежден и не соответствует стандарту json"""
    try:
        with open(json_path, encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError, ValueError):
        return []


def sum_of_transactions(transaction: dict) -> float | ValueError:
    """Функция принимает словарь transaction и возвращает результат по ключу amount типа float или
    ValueError с сообщением 'Транзация выполнена не в рублях. Укажите транзакцию в рублях' если транзакция
    проведена не в рублях"""
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        raise ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях")

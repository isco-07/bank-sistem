import json
from typing import Any


def deserialization_json_file(json_path: str) -> list:
    """Функция принимает параметр json_path (имя json файла), возвращает список словарей если файл найден,
    или пустой список при условии, что файла не найден или поврежден и не соответствует стандарту json"""
    try:
        with open(f"../data/{json_path}", "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def sum_of_transactions(transaction: dict) -> float | Any:
    """Функция принимает словарь transaction и возвращает результат по ключу amount типа float или
    ValueError с сообщением 'Транзация выполнена не в рублях. Укажите транзакцию в рублях' если транзакция
    проведена не в рублях"""
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        return float(transaction["operationAmount"]["amount"])
    else:
        print("Транзация выполнена не в рублях. Укажите транзакцию в рублях")
        return ValueError

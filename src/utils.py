import json

from src.logger import my_logger


def deserialization_json_file(json_path: str) -> list:
    """Функция принимает параметр json_path (имя json файла), возвращает список словарей если файл найден,
    или пустой список при условии, что файла не найден или поврежден и не соответствует стандарту json"""
    try:
        with open(json_path, encoding="utf-8") as f:
            my_logger().info("Operation successful...")
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError, ValueError):
        my_logger().error("The file was not found or could not be processed")
        return []


def sum_of_transactions(transaction: dict) -> float | ValueError:
    """Функция принимает словарь transaction и возвращает результат по ключу amount типа float или
    ValueError с сообщением 'Транзация выполнена не в рублях. Укажите транзакцию в рублях' если транзакция
    проведена не в рублях"""
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        my_logger().info("The transaction was executed in rubles")
        return float(transaction["operationAmount"]["amount"])
    else:
        my_logger().error("The transaction was not executed in rubles")
        raise ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях")

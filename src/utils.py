import json
import logging

logger = logging.getLogger("utils_log")
file_handler = logging.FileHandler("funcs_log.log", "w")
console_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.setLevel(level=logging.INFO)


def deserialization_json_file(json_path: str) -> list:
    """Функция принимает параметр json_path (имя json файла), возвращает список словарей если файл найден,
    или пустой список при условии, что файла не найден или поврежден и не соответствует стандарту json"""
    try:
        with open(json_path, encoding="utf-8") as f:
            logger.info("Operation successful...")
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError, ValueError):
        logger.error("The file was not found or could not be processed")
        return []


def sum_of_transactions(transaction: dict) -> float | ValueError:
    """Функция принимает словарь transaction и возвращает результат по ключу amount типа float или
    ValueError с сообщением 'Транзация выполнена не в рублях. Укажите транзакцию в рублях' если транзакция
    проведена не в рублях"""
    if transaction["operationAmount"]["currency"]["code"] == "RUB":
        logger.info("The transaction was executed in rubles")
        return float(transaction["operationAmount"]["amount"])
    else:
        logger.error("The transaction was not executed in rubles")
        raise ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях")

import re
from collections import Counter


def search_by_regex(operations_list: list[dict], search_word: str) -> list[dict]:
    """Функция принимать список словарей с данными о банковских операциях и строку поиска и возвращает
    список словарей, у которых в описании есть данная строка."""
    pattern = re.compile(search_word)
    return [
        operation
        for operation in operations_list
        if "description" in operation.keys() and pattern.search(operation["description"])
    ]


def counter_categories(operations_list: list[dict], categories_dict: dict) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и словарь категорий операций
    и возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций
    в каждой категории."""
    new_category_dict = Counter(
        o["description"]
        for o in operations_list
        if "description" in o.keys() and o["description"] in categories_dict["description"]
    )
    return dict(new_category_dict)

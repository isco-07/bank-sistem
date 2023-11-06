from typing import Generator, Iterator


def filter_by_currency(trans_list: list[dict], cur_name: str) -> Iterator:
    """Функция принимает список словарей и строку:
    trans_list: list[dict]
    cur_name: str
    фильтрует список словарей и возвращает отфильтрованный список словарей типа Iterator"""
    return filter(lambda item: item["operationAmount"]["currency"]["code"] == cur_name, trans_list)


def transaction_descriptions(trans_list: list[dict]) -> Generator:
    """Функция принимает список словарей:
    trans_list: list[dict]
    и возвращает генератор словаря по ключу ["description"]"""
    for item in trans_list:
        yield item["description"]


def card_number_generator(num1: int, num2: int) -> Generator:
    """Функция принимает два числа:
    num1: int
    num2: int
    и возвращает генератор строки. Пример: 0000 0000 0000 0000"""
    for item in range(num1, num2 + 1):
        gen_num = str(item).rjust(16, "0")
        yield f"{gen_num[:4]} {gen_num[4:8]} {gen_num[8:12]} {gen_num[12:]}"

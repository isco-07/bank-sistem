from datetime import datetime


def filter_dict_list_by_state(dict_list: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и строковую переменную и возвращает отфильтрованный список словарей,
    где значение по ключу state равно строковой переменной state"""
    return list(filter(lambda x: x["state"] == state, dict_list))


def dict_list_by_date(dict_list: list, sort_rev: bool = False) -> list:
    """Функция принимает список словарей переменную bool типа и возращает отсортированный список словарей
    по ключу date по убыванию или возрастанию в зависимости от второго параметра функции"""
    return sorted(
        dict_list,
        key=lambda x: datetime.strptime(" ".join(x["date"].split("T")), "%Y-%m-%d %H:%M:%S.%f").date(),
        reverse=sort_rev,
    )


def make_sort_list_products(dict_list: list, category: str | None = None) -> list:
    """Функция принимает 2 параметра: список словарей с продуктами, необязательный параметр category.
    Возвращает отсоритрованный список словарей по убыванию ключа price определенной категории
    товаров, если category не None, или список всех продуктов"""
    if category is None:
        return sorted(dict_list, key=lambda x: int(x["price"]), reverse=True)
    return sorted(
        list(filter(lambda x: x["category"] == category, dict_list)), key=lambda x: int(x["price"]), reverse=True
    )

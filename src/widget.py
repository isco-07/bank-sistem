from functools import reduce


def disguise_widget(card_info: str) -> str:
    """принимает на вход строку информацией тип карты/счета и номер карты/счета и
    возвращает эту строку с замаскированным номером карты/счета."""
    card_info_list = card_info.strip().split()
    if len(card_info_list[-1]) == 16:
        card_info_list[-1] = " ".join(
            [card_info_list[-1][:4], card_info_list[-1][4:6] + "**", "****", card_info_list[-1][13:]]
        )
    else:
        card_info_list[-1] = "".join([card_info_list[-1][ind] if ind > -5 else "*" for ind in range(-6, 0)])
    return " ".join(card_info_list)


def return_date(date_string: str) -> str:
    """Принимает строку с данными и возвращает дату в формате dd.mm.yyyy"""
    return ".".join(date_string.split("T")[0].split("-")[::-1])


def new_list(args_list: list) -> list:
    """Принимает на вход список строк и возвращает список строк, в которых первая и последняя буквы совпадают.
    Если список пустой, возвращает пустой список."""
    if len(args_list) == 0:
        return args_list
    return [word for word in args_list if len(word) == 0 or word.lower()[0] == word.lower()[-1]]


def mul_two_max(numbers_list: list) -> int:
    """Принимает на вход список целых чисел и возвращает максимальное произведение двух чисел из списка.
    Если в списке менее двух чисел, возвращает 0"""
    if len(numbers_list) < 2:
        return 0
    else:
        return reduce(lambda a, b: a * b, sorted([abs(number) for number in numbers_list], reverse=True)[:2])

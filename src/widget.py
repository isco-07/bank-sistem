from src import masks


def disguise_widget(card_info: str) -> str:
    """принимает на вход строку информацией тип карты/счета и номер карты/счета и
    возвращает эту строку с замаскированным номером карты/счета."""
    card_info_list = card_info.strip().split()
    if len(card_info_list[-1]) == 16:
        card_info_list[-1] = masks.disguise_card(card_info_list[-1])
    else:
        card_info_list[-1] = masks.disguise_acc_number(card_info_list[-1])
    return " ".join(card_info_list)


def return_date(date_string: str) -> str:
    """Принимает строку с данными и возвращает дату в формате dd.mm.yyyy"""
    return ".".join(date_string.split("T")[0].split("-")[::-1])

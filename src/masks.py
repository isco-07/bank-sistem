import os
import textwrap


def disguise_card(card_number: str) -> str:
    """Возвращается маска карты"""
    card_mask = "".join([card_number[ind] if ind < 6 or ind > 11 else "*" for ind in range(16)])
    return " ".join(textwrap.wrap(card_mask, 4))


def disguise_acc_number(acc_number: str) -> str:
    """Возвращается маска номера счета"""
    acc_number_mask = "".join([acc_number[ind] if ind > -5 else "*" for ind in range(-6, 0)])
    return acc_number_mask


def files_counter(way: str, req_flag: bool = False) -> dict:
    folders_counter = 0
    files_counter = 0
    for root, dirs, files in os.walk(way):
        for _ in dirs:
            folders_counter += 1
        for _ in files:
            files_counter += 1
    return {"files": files_counter, "folders": folders_counter}



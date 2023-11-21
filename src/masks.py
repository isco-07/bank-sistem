import logging
from typing import Any


def masks_logging() -> Any:
    logging.basicConfig(
        level=logging.DEBUG,
        filename="logging_masks.log",
        filemode="w",
        format="%(asctime)s %(name)s %(levelname)s: %(message)s",
        encoding="utf-8",
    )
    return logging.getLogger()


def disguise_card(card_number: str) -> str:
    """Возвращается маска карты"""
    return " ".join([card_number[:4], card_number[4:6] + "**", "****", card_number[12:]])


def disguise_acc_number(acc_number: str) -> str:
    """Возвращается маска номера счета"""
    acc_number_mask = "".join([acc_number[ind] if ind > -5 else "*" for ind in range(-6, 0)])
    return acc_number_mask

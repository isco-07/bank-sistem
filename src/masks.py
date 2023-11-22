import logging

logger = logging.getLogger("masks_log")
file_handler = logging.FileHandler("funcs_log.log", "w")
console_handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.setLevel(level=logging.INFO)


def disguise_card(card_number: str) -> str:
    """Возвращается маска карты"""
    logger.info("The card is disguised")
    return " ".join([card_number[:4], card_number[4:6] + "**", "****", card_number[12:]])


def disguise_acc_number(acc_number: str) -> str:
    """Возвращается маска номера счета"""
    acc_number_mask = "".join([acc_number[ind] if ind > -5 else "*" for ind in range(-6, 0)])
    logger.info("account number disguised")
    return acc_number_mask

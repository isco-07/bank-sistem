from src.logger import my_logger


def disguise_card(card_number: str) -> str:
    """Возвращается маска карты"""
    my_logger().info("The card is disguised")
    return " ".join([card_number[:4], card_number[4:6] + "**", "****", card_number[12:]])


def disguise_acc_number(acc_number: str) -> str:
    """Возвращается маска номера счета"""
    acc_number_mask = "".join([acc_number[ind] if ind > -5 else "*" for ind in range(-6, 0)])
    my_logger().info("account number disguised")
    return acc_number_mask

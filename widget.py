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

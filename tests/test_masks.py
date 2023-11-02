from src.masks import disguise_acc_number, disguise_card


def test_disguise_card() -> None:
    assert disguise_card("7000792289606361") == "7000 79** **** 6361"


def test_disguise_acc_number() -> None:
    assert disguise_acc_number("73654108430135874305") == "**4305"

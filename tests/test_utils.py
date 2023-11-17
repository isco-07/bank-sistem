import pytest

from src.utils import deserialization_json_file, sum_of_transactions


@pytest.mark.parametrize(
    "ind, expected",
    [
        (
            "../data/operations.json",
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            },
        ),
        ("opera.json", []),
    ],
)
def test_deserialization_json_file(ind: str, expected: float | ValueError) -> None:
    first_dict = (
        deserialization_json_file(ind)[0]
        if len(deserialization_json_file(ind)) > 0
        else deserialization_json_file(ind)
    )
    assert first_dict == expected


@pytest.fixture
def foo() -> dict:
    return {
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560",
    }


def test_sum_of_transactions(foo: dict) -> None:
    with pytest.raises(ValueError):
        assert sum_of_transactions(foo)
    assert sum_of_transactions(deserialization_json_file("../data/operations.json")[0]) == 31957.58

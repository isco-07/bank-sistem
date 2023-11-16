import pytest

from src.utils import deserialization_json_file, sum_of_transactions


@pytest.mark.parametrize(
    "ind, expected",
    [
        (
            "operations.json",
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
def foo() -> list:
    return [31957.58, ValueError, ValueError, 48223.05]


def test_sum_of_transactions(foo: list) -> None:
    for i in range(4):
        assert sum_of_transactions(deserialization_json_file("operations.json")[i]) == foo[i]

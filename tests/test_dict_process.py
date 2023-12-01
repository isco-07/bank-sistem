import os

import pytest

from src.dict_process import counter_categories, search_by_regex
from src.utils import deserialization_json_file


@pytest.fixture()
def func() -> list:
    way_to_file = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")
    out_list = deserialization_json_file(way_to_file)
    return out_list


def test_counter_categories(func: list) -> None:
    assert counter_categories(func, {"description": ["Открытие вклада", "Перевод со счета на счет"]}) == {
        "Открытие вклада": 10,
        "Перевод со счета на счет": 15,
    }


def test_search_by_regex(func: list) -> None:
    assert search_by_regex(func, "Открытие вклада")[:5] == [
        {
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {"amount": "48223.05", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431",
        },
        {
            "id": 596171168,
            "state": "EXECUTED",
            "date": "2018-07-11T02:26:18.671407",
            "operationAmount": {"amount": "79931.03", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 72082042523231456215",
        },
        {
            "id": 863064926,
            "state": "EXECUTED",
            "date": "2019-12-08T22:46:21.935582",
            "operationAmount": {"amount": "41096.24", "currency": {"name": "USD", "code": "USD"}},
            "description": "Открытие вклада",
            "to": "Счет 90424923579946435907",
        },
        {
            "id": 172864002,
            "state": "EXECUTED",
            "date": "2018-12-28T23:10:35.459698",
            "operationAmount": {"amount": "49192.52", "currency": {"name": "USD", "code": "USD"}},
            "description": "Открытие вклада",
            "to": "Счет 96231448929365202391",
        },
        {
            "id": 801684332,
            "state": "EXECUTED",
            "date": "2019-11-05T12:04:13.781725",
            "operationAmount": {"amount": "21344.35", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Открытие вклада",
            "to": "Счет 77613226829885488381",
        },
    ]

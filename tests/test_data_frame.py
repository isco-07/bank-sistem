import os

import pandas as pd
import pytest

from src.data_frame import read_csv_file, read_xlsx_file


@pytest.fixture
def files_df() -> dict:
    df = {
        "id": [650703, 3598919, 593027],
        "state": ["EXECUTED", "EXECUTED", "CANCELED"],
        "date": ["2023-09-05T11:30:32Z", "2020-12-06T23:00:58Z", "2023-07-22T05:02:01Z"],
        "amount": [16210, 29740, 30368],
        "currency_name": ["Sol", "Peso", "Shilling"],
        "currency_code": ["PEN", "COP", "TZS"],
        "from": ["Счет 58803664561298323391", "Discover 3172601889670065", "Visa 1959232722494097"],
        "to": ["Счет 39745660563456619397", "Discover 0720428384694643", "Visa 6804119550473710"],
        "description": ["Перевод организации", "Перевод с карты на карту", "Перевод с карты на карту"],
    }
    return pd.DataFrame(df).to_dict()


def test_read_csv_file(files_df: dict) -> None:
    work_path = os.path.join(os.path.dirname(__file__), "..", "data", "transactions.csv")
    assert read_csv_file(work_path).iloc[:3].to_dict() == files_df


def test_read_xlsx_file(files_df: dict) -> None:
    work_path = os.path.join(os.path.dirname(__file__), "..", "data", "transactions_excel.xlsx")
    assert read_xlsx_file(work_path).iloc[:3].to_dict() == files_df

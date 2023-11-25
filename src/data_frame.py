from typing import Any

import pandas as pd


def read_csv_file(file_path: str) -> Any:
    """Функция принимает путь к файлу считывает данные чере метод read_csv библиотеки pandas
    и возвращает DataFrame"""
    csv_list = pd.read_csv(file_path, delimiter=";")
    return csv_list


def read_xlsx_file(file_path: str) -> Any:
    """Функция принимает путь к файлу считывает данные чере метод read_excel библиотеки pandas
    и возвращает DataFrame"""
    xlsx_list = pd.read_excel(file_path)
    return xlsx_list

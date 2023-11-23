import logging
from typing import Any


def my_logger() -> Any:
    """Функция создает и взвращает logger с хендлерами на запись в файл и вывод в консоль и форматер вида
    (временная метка, название модуля, уровень серьезности и сообщение, описывающее событие или ошибку)"""
    logger = logging.getLogger("my_log")
    file_handler = logging.FileHandler("funcs_log.log", "w")
    console_handler = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    logger.setLevel(level=logging.INFO)
    return logger

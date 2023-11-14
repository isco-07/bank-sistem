from datetime import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: None | str = None) -> Callable:
    """Функция принимает имя файла или значение None, создает функцию-декоратор wrapped которая принимает другую
    функцию, проверяет ее через try/catch, возвращает результат этой функции и записывает ее log в filename в случае
     если передано имя файла, или возвращает ошибку или записывает log ошибки в filename если также в функцию передано
     имя файла для записи"""

    def wrapped(function: Callable) -> Callable:
        @wraps(function)
        def inner(*args: Any, **kwargs: dict) -> Any:
            try:
                result = function(*args, **kwargs)
                log_message = f"{str(datetime.now())[:-7]} {function.__name__} ok\n"
            except Exception as e:
                log_message = (
                    f"{str(datetime.now())[:-7]} {function.__name__} error: <{type(e).__name__}>. "
                    f"Inputs: {args}, {kwargs}\n"
                )
                result = None
            if filename is None:
                return log_message
            else:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(log_message)
            return result

        return inner

    return wrapped

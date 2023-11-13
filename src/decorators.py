from datetime import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: None | str = None) -> Callable:
    def wrapped(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: dict) -> Any:
            try:
                func(*args, **kwargs)
            except Exception as e:
                result = (
                    f"{str(datetime.now())[:-7]} {func.__name__} error: <{type(e).__name__}>. "
                    f"Inputs: {args}, {kwargs}\n"
                )
            else:
                result = f"{str(datetime.now())[:-7]} {func.__name__} ok\n"
            if filename is None:
                return result
            else:
                with open(filename, "a", encoding="utf-8") as f:
                    f.write(result)
                return func(*args, **kwargs)

        return inner

    return wrapped

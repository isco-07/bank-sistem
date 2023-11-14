import os
from datetime import datetime
from typing import Any

import pytest

from src.decorators import log


@pytest.mark.parametrize(
    "arg_1, arg_2, expected", [(1, 0, "func error: <ZeroDivisionError>. Inputs: (1, 0), {}"), (1, 2, "func ok")]
)
def test_log(arg_1: Any, arg_2: Any, expected: str) -> None:
    filename = "mylog.txt"
    if os.path.exists(filename):
        os.remove(filename)

    @log(filename)
    def func(x: int, y: int) -> float:
        return x / y

    now = str(datetime.now())[:-7]
    func(arg_1, arg_2)
    with open(filename) as f:
        log_message = f.read().strip()

    expected_log = f"{now} {expected}"
    assert log_message == expected_log

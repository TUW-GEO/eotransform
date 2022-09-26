import sys
from pathlib import Path

import pytest

sys.path.append((Path(__file__).parent / "helpers").as_posix())


def pytest_addoption(parser):
    parser.addoption("--slow", action="store_true",
                     default=False,
                     help="include tests marked slow")


@pytest.fixture(scope='session')
def slow_factor(pytestconfig):
    return 10.0 if pytestconfig.getoption("slow") else 1.0

import time
from contextlib import contextmanager
from typing import Sequence, Iterable, Iterator

from eotransform.protocol.sink import Sink
from eotransform.protocol.transformer import Transformer


class AssertIntStream(Sink[int]):
    def __init__(self, expected: Sequence[int]):
        self._expected = expected
        self._n = 0

    def __call__(self, x: int) -> None:
        assert self._expected[self._n] == x
        self._n += 1

    def assert_all_visited(self):
        assert self._n == len(self._expected)


@contextmanager
def wait_up_to(seconds: float):
    start = time.time()
    yield
    sleep_time = seconds - (time.time() - start)
    if sleep_time > 0:
        time.sleep(sleep_time)


class SourceStub(Iterable):
    def __init__(self, n, operation_time, raises_error_at):
        self._n = n
        self._operation_time = operation_time
        self._raises_error_at = raises_error_at or {}
        self._i = 0

    def __iter__(self) -> Iterator:
        return self

    def __next__(self):
        with wait_up_to(self._operation_time):
            if self._i == self._n:
                raise StopIteration
            if self._i in self._raises_error_at:
                raise self._raises_error_at[self._i]
            self._i += 1
            return self._i - 1


class ProcessStub(Transformer):
    def __init__(self, operation_time, raises_error_at=None):
        self._operation_time = operation_time
        self._raises_error_at = raises_error_at or {}
        self._i = 0

    def __call__(self, x):
        with wait_up_to(self._operation_time):
            if self._i in self._raises_error_at:
                raise self._raises_error_at[self._i]
            self._i += 1
            return x


class SinkStub(Sink):
    def __init__(self, operation_time, raises_error_at):
        self._operation_time = operation_time
        self._raises_error_at = raises_error_at or {}
        self._i = 0

    def __call__(self, _) -> None:
        if self._i in self._raises_error_at:
            raise self._raises_error_at[self._i]
        self._i += 1


class SinkSpy(SinkStub):
    def __init__(self, operation_time, raises_error_at):
        super().__init__(operation_time, raises_error_at)
        self.received_values = []

    def __call__(self, x) -> None:
        with wait_up_to(self._operation_time):
            super().__call__(x)
            self.received_values.append(x)

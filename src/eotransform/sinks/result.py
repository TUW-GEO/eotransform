from typing import TypeVar

from eotransform.protocol.sink import Sink, SinkT
from eotransform.result import Result

ErrT = TypeVar("ErrT")


class SinkUnwrapped(Sink[Result[SinkT, ErrT]]):
    def __init__(self, wrapped_sink: Sink[SinkT], ignore_exceptions=None):
        self._wrapped_sink = wrapped_sink
        self._ignore_exceptions = ignore_exceptions or set()

    def __call__(self, x: Result[SinkT, ErrT]) -> None:
        x = x.ignore(self._ignore_exceptions)
        if not x.is_ignored():
            self._wrapped_sink(x.unwrap())

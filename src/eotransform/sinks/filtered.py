from typing import Callable

from eotransform.protocol.sink import Sink, SinkT


class SinkFiltered(Sink[SinkT]):
    def __init__(self, wrapped_sink: Sink[SinkT], predicate: Callable[[SinkT], bool]):
        self._wrapped_sink = wrapped_sink
        self._predicate = predicate

    def __call__(self, x: SinkT) -> None:
        if self._predicate(x):
            self._wrapped_sink(x)

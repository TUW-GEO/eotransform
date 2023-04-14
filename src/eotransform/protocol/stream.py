from abc import abstractmethod
from typing import Generic, TypeVar

StreamInT = TypeVar('StreamInT')


class StreamIn(Generic[StreamInT]):
    @abstractmethod
    def send(self, x: StreamInT) -> None:
        ...

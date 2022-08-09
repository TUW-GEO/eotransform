from abc import abstractmethod
from typing import TypeVar, Generic

TransformerT = TypeVar('TransformerT')
TransformerU = TypeVar('TransformerU')


class Transformer(Generic[TransformerT, TransformerU]):
    @abstractmethod
    def __call__(self, x: TransformerT) -> TransformerU:
        ...

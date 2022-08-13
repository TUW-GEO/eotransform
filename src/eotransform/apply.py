from typing import TypeVar, Callable

from eotransform.protocol.transformer import Transformer, TransformerT, TransformerU

ApplyT = TypeVar('ApplyT')
ApplyU = TypeVar('ApplyU')


class Apply(Transformer[ApplyT, ApplyU]):
    def __init__(self, fn: Callable[[ApplyT], ApplyU]):
        self._fn = fn

    def __call__(self, x: TransformerT) -> TransformerU:
        return self._fn(x)

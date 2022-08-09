from typing import Any

from eotransform.protocol.transformer import Transformer


class Add(Transformer[int, int]):
    def __init__(self, v):
        self._v = v

    def __call__(self, x: int) -> int:
        return x + self._v


class Mul(Transformer[int, int]):
    def __init__(self, v):
        self._v = v

    def __call__(self, x: int) -> int:
        return x * self._v


class ReplaceWithString(Transformer[Any, str]):
    def __init__(self, string: str):
        self._string = string

    def __call__(self, x: Any) -> str:
        return self._string

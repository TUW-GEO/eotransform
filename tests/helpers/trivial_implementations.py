from eotransform.protocol.transformer import Transformer


class Add(Transformer[int, int]):
    def __init__(self, v):
        self._v = v

    def __call__(self, x: int) -> int:
        return x + self._v
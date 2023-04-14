from typing import TypeVar

from eotransform.protocol.stream import StreamIn
from eotransform.protocol.transformer import Transformer

SendStreamInT = TypeVar('SendStreamInT')


class SendToStream(Transformer[SendStreamInT, SendStreamInT]):
    def __init__(self, stream: StreamIn[SendStreamInT]):
        self._stream = stream

    def __call__(self, x: SendStreamInT) -> SendStreamInT:
        self._stream.send(x)
        return x

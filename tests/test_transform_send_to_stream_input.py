import pytest

from eotransform.protocol.stream import StreamIn
from eotransform.transformers.send_to_stream import SendToStream


class StreamedInputSpy(StreamIn[int]):
    def __init__(self):
        self.received_input = None

    def send(self, x: int) -> None:
        self.received_input = x


@pytest.fixture
def stream():
    return StreamedInputSpy()


def test_sending_input_to_stream(stream):
    send = SendToStream(stream)
    assert send(42) == 42
    assert stream.received_input == 42

from concurrent.futures import ThreadPoolExecutor

from eotransform.result import Result
from eotransform.sinks.result import SinkUnwrapped
from eotransform.streamed_process import streamed_process
from eotransform.protocol.sink import Sink
from eotransform.protocol.transformer import Transformer
from eotransform.transformers.result import ApplyToOkResult

# begin-snippet: example_transformer_multiply
class Multiply(Transformer[int, int]):
    def __init__(self, factor: int):
        self.factor = factor

    def __call__(self, x: int) -> int:
        return x * self.factor
# end-snippet


# begin-snippet: example_sink_accumulate
class AccumulatingSink(Sink[int]):
    def __init__(self):
        self.result = 0

    def __call__(self, x: int) -> None:
        self.result += x
# end-snippet

def test_doc_example_streamed_results():
    # begin-snippet: example_streamed_results
    def a_data_source():
        for i in range(4):
            if i == 1:
                yield Result.error(RuntimeError("A runtime error occured!"))
            else:
                yield Result.ok(i)

    accumulated = AccumulatingSink()
    sink = SinkUnwrapped(accumulated, ignore_exceptions={RuntimeError})
    with ThreadPoolExecutor(max_workers=3) as ex:
        streamed_process(a_data_source(), ApplyToOkResult(Multiply(2)), sink, ex)

    assert accumulated.result == 10
    # end-snippet

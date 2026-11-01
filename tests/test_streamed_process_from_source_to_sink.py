import time
from concurrent.futures import ThreadPoolExecutor
from typing import Iterable, Iterator

import pytest

from doubles import AssertIntStream, SourceStub, ProcessStub, SinkSpy
from eotransform.streamed_process import streamed_process
from eotransform.utilities.profiling import PerformanceClock
from trivial_implementations import Add

EPSILON = 1 / 32


@pytest.fixture
def executor():
    with ThreadPoolExecutor(max_workers=2) as e:
        yield e


def test_process_source_and_put_in_sink(executor):
    out_sink = AssertIntStream(expected=[1, 2, 3])
    streamed_process([0, 1, 2], Add(1), out_sink, executor)
    out_sink.assert_all_visited()


def test_interleave_processing_and_sour_and_sink_operations(executor, slow_factor):
    """
    Testing interleaving INput IO, PRocess and OuTput IO:
    IN->IN->IN
      ->PR->PR->PR
          ->OT->OT->OT
    """
    source = make_io_source(n=3, operation_time=(1 / 16) * slow_factor)
    process = make_process(operation_time=(1 / 16) * slow_factor)
    sink = make_io_sink(operation_time=(1 / 16) * slow_factor)

    streamed_process_clock = PerformanceClock()
    with streamed_process_clock.measure():
        streamed_process(source, process, sink, executor)

    assert streamed_process_clock.mean_measures < (5 / 16 + EPSILON) * slow_factor


def make_io_source(n, operation_time=0.0, raises_error_at=None):
    return SourceStub(n, operation_time, raises_error_at)


def make_process(operation_time=0.0, raises_error_at=None):
    return ProcessStub(operation_time, raises_error_at)


def make_io_sink(operation_time=0.0, raises_error_at=None):
    return SinkSpy(operation_time, raises_error_at)


class SourceError(RuntimeError):
    ...


@pytest.mark.parametrize("err_idx", [0, 1, 2])
def test_hand_through_loading_errors(executor, err_idx):
    error_source = make_io_source(n=3,
                                  raises_error_at={err_idx: SourceError("something bad has happened during loading.")})
    with pytest.raises(SourceError):
        streamed_process(error_source, make_process(), make_io_sink(), executor, loading_timeout=0.01)


class SinkError(RuntimeError):
    ...


@pytest.mark.parametrize("err_idx", [0, 1, 2, 3])
def test_hand_through_storing_errors(executor, err_idx):
    error_sink = make_io_sink(raises_error_at={err_idx: SinkError("something bad has happened during storing.")})
    with pytest.raises(SinkError):
        streamed_process(make_io_source(n=4), make_process(), error_sink, executor, storing_timeout=0.01)


class ProcessError(RuntimeError):
    ...


@pytest.mark.parametrize("err_idx", [0, 1, 2, 3])
def test_cleanup_properly_when_process_errors(executor, err_idx):
    error_process = make_process(
        raises_error_at={err_idx: ProcessError("something bad has happened during processing.")})
    with pytest.raises(ProcessError):
        streamed_process(make_io_source(n=4), error_process, make_io_sink(), executor)


def test_sink_stores_last_successful_values_after_process_error(executor):
    error_process = make_process(raises_error_at={2: ProcessError("something bad happened at the end.")})
    sink = make_io_sink()
    try:
        streamed_process(make_io_source(n=3), error_process, sink, executor)
    except ProcessError:
        ...
    assert sink.received_values == [0, 1]


LOADING_TIMEOUT = 0.25


class SlowLoadSource(Iterable):
    def __init__(self, n: int, slow_at: int, load_time: float) -> None:
        self._n = n
        self._slow_at = slow_at
        self._load_time = load_time

    def __iter__(self) -> Iterator:
        for i in range(self._n):
            if i == self._slow_at:
                time.sleep(self._load_time)
            yield i


@pytest.mark.parametrize("timeouts", [1.5, 2.5])
def test_load_exceeding_loading_timeout_is_reported_as_timeout(executor: ThreadPoolExecutor, timeouts: float) -> None:
    slow_source = SlowLoadSource(n=4, slow_at=2, load_time=timeouts * LOADING_TIMEOUT)
    with pytest.raises(TimeoutError, match="loading_timeout"):
        streamed_process(slow_source, make_process(), make_io_sink(), executor, loading_timeout=LOADING_TIMEOUT)


def test_load_failure_surfaces_without_waiting_for_loading_timeout(executor: ThreadPoolExecutor) -> None:
    generous_timeout = 5.0
    error_source = make_io_source(n=3, raises_error_at={1: SourceError("unreadable input")})

    clock = PerformanceClock()
    with clock.measure(), pytest.raises(SourceError):
        streamed_process(error_source, make_process(), make_io_sink(), executor, loading_timeout=generous_timeout)

    assert clock.mean_measures < generous_timeout / 10, "load failure waited for the loading timeout before surfacing"


def test_sink_stores_last_successful_values_after_loading_error(executor):
    error_source = make_io_source(n=3, raises_error_at={2: SourceError("something bad happened at the end.")})
    sink = make_io_sink()
    try:
        streamed_process(error_source, make_process(), sink, executor, loading_timeout=0.01)
    except SourceError:
        ...
    assert sink.received_values == [0, 1]

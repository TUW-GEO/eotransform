import time
from contextlib import contextmanager


class PerformanceClock:
    def __init__(self):
        self._measures = []

    @contextmanager
    def measure(self):
        start = time.time()
        yield
        self._measures.append(time.time() - start)

    @property
    def total_measures(self):
        return sum(self._measures)

    @property
    def mean_measures(self):
        return self.total_measures / len(self._measures)

    def drop_first(self):
        self._measures = self._measures[1:]
        return self

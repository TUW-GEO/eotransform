import pytest

from eotransform.result import Result
from eotransform.transformers.result import MapOnOkResult


def test_map_on_ok_result_transforms_ok_result():
    x = Result.ok(42)
    assert MapOnOkResult(lambda r: r + 1)(x).unwrap() == 43


def test_map_on_ok_result_hands_through_error_without_applying_any_transformation():
    def a_transform(_):
        assert False

    x = Result.error(AssertionError("an error occurred"))
    x = MapOnOkResult(a_transform)(x)
    with pytest.raises(AssertionError):
        x.unwrap()

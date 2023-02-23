from p016_sum_triangle import sum_triangle
import pytest

def zero():
    assert sum_triangle(0) == 0

def small_n():
    assert sum_triangle(1) == 1
    assert sum_triangle(2) == 3
    assert sum_triangle(5) == 15
    assert sum_triangle(11) == 66

def large_n():
    assert sum_triangle(1000) == 500500
    assert sum_triangle(1500) == 1125750


@pytest.mark.timeout(0.05)
def time_limit():
    assert sum_triangle(10000) == 50005000
    assert sum_triangle(18327) == 167948628
    assert sum_triangle(471337) == 111079519453
    assert sum_triangle(97317417) == 4735339874434653

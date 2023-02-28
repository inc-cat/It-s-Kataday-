from p017_get_averages import get_averages
import pytest


def test_empty():
    assert get_averages([]) == None


def test_one_element():
    assert get_averages([[5]]) == 5
    assert get_averages([[1]]) == 1


def test_singular_array():
    assert get_averages([[1, 2, 3]]) == 2
    assert get_averages([[4, 6, 8]]) == 6


def test_multi_array():
    assert (
        get_averages(
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ]
        )
        == 5
    )

    assert (
        get_averages(
            [
                [9, 1, 5],
                [20, 30, 40],
                [12, 2],
                [19, 20, 21, 22, 23],
            ]
        )
        == 17.23
    )


@pytest.mark.timeout(0.05)
def test_time():
    new_list = [i * 2 for i in range(100000)]

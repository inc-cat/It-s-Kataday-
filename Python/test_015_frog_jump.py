from p015_frog_jump import frog_jumps
import pytest


def test_frog_jumps():
    assert frog_jumps(10, 85, 30) == 3
    assert frog_jumps(0, 300, 40) == 8


def test_extreme_conditions():
    assert frog_jumps(1000, 1000, 20) == 0


@pytest.mark.timeout(0.01)
def test_frog_10ms():
    assert frog_jumps(0, 100000000, 2) == 50000000


@pytest.mark.timeout(0.01)
def test_extreme_10ms():
    assert frog_jumps(-2000000000, 2000000000, 1) == 4000000000

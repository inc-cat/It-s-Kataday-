from p003_diff_to_fib import diff_to_fib


def test_zero_difference():
    assert diff_to_fib(5) == 0
    assert diff_to_fib(13) == 0
    assert diff_to_fib(1597) == 0


def test_difference():
    assert diff_to_fib(4) == 1
    assert diff_to_fib(1000) == 597
    assert diff_to_fib(50025) == 25000


def test_large_numbers():
    assert diff_to_fib(1000000) == 346269
    assert diff_to_fib(58362941) == 4883045
    assert diff_to_fib(1000000000) == 134903170

from p009_obj_filter import obj_filter


def test_empty_object():
    def function(arg):
        return

    assert obj_filter({}, function) == {}


def test_true_function():
    def function(arg):
        return True

    assert obj_filter({1: 1, 2: 2, 3: 3}, function) == {1: 1, 2: 2, 3: 3}


def test_false_function():
    def function(arg):
        return False

    assert obj_filter({1: 1, 2: 2, 3: 3}, function) == {}


def test_odd_numbers():
    def function(arg):
        return arg % 2 == 1

    assert obj_filter({1: 1, 2: 2, 3: 3}, function) == {1: 1, 3: 3}

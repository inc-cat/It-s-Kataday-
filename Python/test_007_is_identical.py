from p007_is_identical import is_identical


def test_empty_object():
    assert is_identical([], []) == True


def test_differences():
    assert is_identical({"a": "a"}, {"b": "b"}) == False
    assert is_identical({1: 1, 2: 2, 3: 3, 4: 4}, {1: 1, 2: 2, 3: 5, 4: 4}) == False


def test_subsets():
    assert is_identical({"a": "a", "b": "b"}, {"a": "a", "b": "b", "c": "c"}) == False
    assert is_identical({1: 1, 2: 2, 3: 3}, {1: 1, 2: 2}) == False


def test_identical_objects():
    assert is_identical({1: 1, 2: 2, 3: 3}, {1: 1, 2: 2, 3: 3}) == True
    assert (
        is_identical(
            {1: "hello", 2: "goodbye", 3: 4, 4: True},
            {1: "hello", 2: "goodbye", 3: 4, 4: True},
        )
        == True
    )


def test_different_nested():
    assert (
        is_identical({1: 1, 2: 2, 3: {4: 4, 5: 5}}, {1: 1, 2: 2, 3: {4: 4, 5: 6}})
        == False
    )
    assert (
        is_identical(
            {1: 1, 2: 2, 3: {4: 4, 5: {7: 7}}}, {1: 1, 2: 2, 3: {4: 4, 5: {7: 6}}}
        )
        == False
    )


def test_identical_nested():
    assert (
        is_identical({1: 1, 2: 2, 3: {4: 4, 5: 5}}, {1: 1, 2: 2, 3: {4: 4, 5: 5}})
        == True
    )
    assert (
        is_identical(
            {1: 1, 2: 2, 3: {4: 4, 5: {7: 7}}}, {1: 1, 2: 2, 3: {4: 4, 5: {7: 7}}}
        )
        == True
    )

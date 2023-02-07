from p008_check_mutation import check_mutation


def test_1d_dict():
    original_dict = {1: 1, 2: 2, 3: 3}
    new_dict = check_mutation(original_dict)
    mutable = original_dict is new_dict
    assert mutable == False


def test_1d_list():
    original_list = [1, 2, 3]
    new_list = check_mutation(original_list)
    mutable = original_list is new_list
    assert mutable == False


def test_2d_dict():
    original_dict = {
        1: 1,
        "a": "a",
        "b": {"c": "c", "d": "d"},
        2: {3: 3, 4: {5: 5, 6: {7: 7, 8: {9: 9, 10: 10}}}},
    }
    new_dict = check_mutation(original_dict)
    mutable = original_dict is new_dict
    assert mutable == False


def test_2d_list():
    original_list = [
        {1: 1},
        [[1, 3], 2, 2],
        {
            4: [1, 2, 1, {7: 1, 1: 4, 9: {12: 1}, 5: [6, 1, 3, 1]}],
            10: 1,
        },
        [1, 1, {1: 1}],
        [[[[[[[[[7]]]]]]]]],
    ]
    new_list = check_mutation(original_list)
    mutable = original_list is new_list
    assert mutable == False

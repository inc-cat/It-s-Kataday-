from p010_count_data import count_data


def test_individual_types():
    assert count_data(1) == {
        "int": 1,
        "float": 0,
        "str": 0,
        "bool": 0,
        "list": 0,
        "dict": 0,
        "function": 0,
    }
    assert count_data(0.5) == {
        "int": 0,
        "float": 1,
        "str": 0,
        "bool": 0,
        "list": 0,
        "dict": 0,
        "function": 0,
    }
    assert count_data("0.5") == {
        "int": 0,
        "float": 0,
        "str": 1,
        "bool": 0,
        "list": 0,
        "dict": 0,
        "function": 0,
    }
    assert count_data(False) == {
        "int": 0,
        "float": 0,
        "str": 0,
        "bool": 1,
        "list": 0,
        "dict": 0,
        "function": 0,
    }
    assert count_data([]) == {
        "int": 0,
        "float": 0,
        "str": 0,
        "bool": 0,
        "list": 1,
        "dict": 0,
        "function": 0,
    }
    assert count_data({}) == {
        "int": 0,
        "float": 0,
        "str": 0,
        "bool": 0,
        "list": 0,
        "dict": 1,
        "function": 0,
    }
    assert count_data(test_individual_types) == {
        "int": 0,
        "float": 0,
        "str": 0,
        "bool": 0,
        "list": 0,
        "dict": 0,
        "function": 1,
    }


def test_nested_types():
    assert count_data({1: "hi"}) == {
        "int": 0,
        "float": 0,
        "str": 1,
        "bool": 0,
        "list": 0,
        "dict": 1,
        "function": 0,
    }
    assert count_data({1: "hi", 2: "no", 3: "yes"}) == {
        "int": 0,
        "float": 0,
        "str": 3,
        "bool": 0,
        "list": 0,
        "dict": 1,
        "function": 0,
    }
    assert count_data(
        {
            1: 1,
            2: [1, 2, 3, {1: True, 2: count_data, 3: [1, 2, 3]}],
            3: "hi",
            4: {1: True, 2: False, 3: ["string", "is", "not", {1: "here"}]},
            5: count_data,
            6: [
                {1: [[[3, 4, 5, "hi", "northcoders", ["Edd!"]]]], 2: "something here"},
            ],
        }
    ) == {
        "int": 1,
        "float": 0,
        "str": 2,
        "bool": 1,
        "list": 2,
        "dict": 3,
        "function": 2,
    }

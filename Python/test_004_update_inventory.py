from p004_update_inventory import update_inventory


def test_identical_lists():
    items_1 = [
        [20, "jeans"],
        [30, "mobile phones"],
        [10, "shoes"],
    ]
    items_2 = [
        [1, "jeans"],
        [12, "mobile phones"],
        [20, "shoes"],
    ]
    answer = [
        [21, "jeans"],
        [42, "mobile phones"],
        [30, "shoes"],
    ]

    assert update_inventory(items_1, items_2) == answer


def test_individual_lists():
    items_1 = [[10, "apples"], [20, "bananas"], [15, "carrots"], [19, "dragonfruit"]]
    items_2 = [[37, "carrots"], [41, "eggplant"], [109, "figs"], [2000000000, "kiwis"]]
    answer = [
        [10, "apples"],
        [20, "bananas"],
        [52, "carrots"],
        [19, "dragonfruit"],
        [41, "eggplant"],
        [109, "figs"],
        [2000000000, "kiwis"],
    ]

    assert update_inventory(items_1, items_2) == answer


def test_unsorted_lists():
    items_1 = [
        [14, "figs"],
        [27, "hammers"],
        [3, "deck chairs"],
        [12, "yachts"],
        [1, "airports"],
    ]
    items_2 = [
        [9, "hammers"],
        [56, "coffee grinders"],
        [2, "airports"],
        [15, "dust collections"],
        [9.5, "zippers"],
    ]
    answer = [
        [3, "airports"],
        [56, "coffee grinders"],
        [3, "deck chairs"],
        [15, "dust collections"],
        [14, "figs"],
        [36, "hammers"],
        [12, "yachts"],
        [9.5, "zippers"],
    ]

    assert update_inventory(items_1, items_2) == answer

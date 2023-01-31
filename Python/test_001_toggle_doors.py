from p001_toggle_doors import toggle_doors

def test_doors():
    test_100 = toggle_doors(100)
    assert test_100 == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    test_496 = toggle_doors(496)
    assert test_496 == [
        1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 
        121, 144, 169, 196, 225, 256, 289, 
        324, 361, 400, 441, 484
        ]

    test_1000 = toggle_doors(1000)
    assert test_1000 == [
        1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 
        144, 169, 196, 225, 256, 289, 324, 361, 400, 
        441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961
        ]
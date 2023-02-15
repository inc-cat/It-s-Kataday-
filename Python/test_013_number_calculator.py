from p013_number_calculator import NumberCalculator


def test_generate():
    numbers = NumberCalculator(1, 2, 3)
    assert numbers.generate() == [1, 2, 3, 2]
    numbers = NumberCalculator(2, 4, 6)
    assert numbers.generate() == [2, 4, 6, 2]
    numbers = NumberCalculator(2, 2, 2)
    assert numbers.generate() == [2, 2, 2, 3]
    assert numbers.generate() == [2, 2, 2, 3, 3]


def test_midpoint():
    numbers = NumberCalculator(1, 2, 3)
    assert numbers.get_midpoint() == 2
    numbers.generate()
    assert numbers.get_midpoint() == 2
    numbers = NumberCalculator(9, 4, 1)
    numbers.generate()
    numbers.generate()
    numbers.generate()
    numbers.generate()
    assert numbers.get_midpoint() == 4


def test_unique_factors():
    numbers = NumberCalculator(1, 2, 3)
    assert numbers.get_unique_factors() == [2, 3]
    numbers.generate()
    assert numbers.get_unique_factors() == [3]
    numbers = NumberCalculator(3, 2, 4)
    assert numbers.get_unique_factors() == [3, 4]
    numbers.generate()
    numbers.generate()
    assert numbers.get_unique_factors() == []

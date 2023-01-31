from p002_is_coprime import is_coprime


def test_same_numbers():
    test_5_5 = is_coprime(5, 5)
    assert test_5_5 == False

    test_2222_2222 = is_coprime(2222, 22222)
    assert test_2222_2222 == False

    test_1_1_1 = is_coprime(3, 3, 3)
    assert test_1_1_1 == False


def coprime_true():
    test_57_58 = is_coprime(57, 58)
    assert test_57_58 == True

    test_13_17 = is_coprime(13, 17)
    assert test_13_17 == True

    test_15_1111 = is_coprime(15, 1111)
    assert test_15_1111 == True

    test_9_11_273 = is_coprime(9, 11, 273)
    assert test_9_11_273 == True

def coprimie_false():
    test_10000000_100 = is_coprime(10000000, 100)
    assert test_10000000_100 == False

    test_56_300279 = is_coprime(56, 300279)
    assert test_56_300279 == False

    test_6923544303_377 = is_coprime(6923544303, 377)
    assert test_6923544303_377 == False

    test_10_15_30_40 = is_coprime(10, 15, 30, 40)
    assert test_10_15_30_40 == False

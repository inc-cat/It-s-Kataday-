import math


def is_coprime(*args):
    if math.gcd(*args) == 1:
        return True
    return False

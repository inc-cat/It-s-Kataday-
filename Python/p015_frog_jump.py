import math


def frog_jumps(a, b, d):
    numbers = sorted([a, b], reverse=True)
    return abs(math.ceil((numbers[0] - numbers[1]) / d))

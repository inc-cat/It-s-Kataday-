import math


def toggle_doors(n):

    steps = math.floor(math.sqrt(n))
    return [i**2 for i in range(1, steps + 1)]

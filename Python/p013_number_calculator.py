import math
from collections import defaultdict


class NumberCalculator:
    def __init__(self, *args):
        self.numbers = list(args)
        if len(self.numbers) == 0:
            raise Exception("Nothing numbers added!")

    def generate(self):
        added_number = math.ceil(
            sum(self.numbers) / self.numbers[len(self.numbers) - 1]
        )
        self.numbers.append(added_number)
        print(self.numbers)
        return self.numbers

    def get_midpoint(self):
        self.numbers.sort()
        if len(self.numbers) % 2 == 0:
            midpoint = int(len(self.numbers) / 2) - 1
        else:
            midpoint = int(math.floor(len(self.numbers) / 2))

        return self.numbers[midpoint]

    def get_unique_factors(self):
        factors = defaultdict(lambda: 0)
        for number in self.numbers:
            for i in range(1, number + 1):
                if number % i == 0:
                    factors[i] += 1

        final_list = []
        for ints in factors.keys():
            if factors[ints] == 1:
                final_list.append(ints)

        return final_list


numbers = NumberCalculator(9, 4, 1)
numbers.generate()
numbers.generate()
numbers.generate()
numbers.generate()

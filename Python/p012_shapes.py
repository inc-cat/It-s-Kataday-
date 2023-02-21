import math


class Shape:
    def __init__(self, m, kg):
        self.m = m
        self.kg = kg

    def get_volume(self):
        raise Exception("Abstract method must be overwritten by subclass!")

    def get_surface_area(self):
        raise Exception("Abstract method must be overwritten by subclass!")

    def get_density(self):
        raise Exception("Abstract method must be overwritten by subclass!")


class Cube(Shape):
    def __init__(self, m, kg):
        super().__init__(m, kg)

    def get_volume(self):
        return self.m**3

    def get_surface_area(self):
        return 6 * self.m**2

    def get_density(self):
        return self.kg / self.get_volume()


class Sphere(Shape):
    def __init__(self, m, kg):
        super().__init__(m, kg)

    def get_volume(self):
        return 4 * math.pi * self.m**3 / 3

    def get_surface_area(self):
        return 4 * math.pi * self.m**2

    def get_density(self):
        return self.kg / self.get_volume()


b = Cube(10, 6)

print(round(b.get_density(), 2))

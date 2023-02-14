from unittest import TestCase
from p012_shapes import Shape, Sphere, Cube


class ShapesTestCase(TestCase):
    def test_initiate(self):
        shape = Shape(0, 0)
        with self.assertRaises(Exception):
            shape.get_volume()


def test_sphere_class():
    sphere = Sphere(5, 2)
    assert round(sphere.get_volume(), 2) == 523.6
    assert round(sphere.get_surface_area(), 2) == 314.16
    assert round(sphere.get_density(), 5) == 0.00382


def test_cube_class():
    cube = Cube(10, 6)
    assert round(cube.get_density(), 2) == 0.01
    assert round(cube.get_surface_area(), 2) == 600
    assert round(cube.get_density(), 2) == 0.01

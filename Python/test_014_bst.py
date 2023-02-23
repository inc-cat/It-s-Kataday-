from unittest import TestCase
from p014_bst import Node, BST


class NodeTestCase(TestCase):
    def test_initiate(self):
        node = Node(10)
        assert node.value == 10
        assert node.smaller == None
        assert node.larger == None

    def test_insert_node(self):
        node = Node(100)
        node.insert_node(150)
        assert node.value == 100
        assert node.smaller == None
        assert node.larger.value == 150
        assert node.larger.smaller == None

        node.insert_node(50)

        assert node.smaller.value == 50
        assert node.smaller.smaller == None

    def test_errors(self):
        node = Node(10)
        with self.assertRaises(Exception):
            node.insert_node("a")
        with self.assertRaises(Exception):
            node.insert_node(10)

    def test_contains(self):
        node = Node(10)

        node.insert_node(1)
        assert node.contains(1) == True

        integers = [2, 4, 8, 16, 128, 64, 32]
        for add_node in integers:
            node.insert_node(add_node)

        extra_numbers = [2, 3, 4, 5, 7, 8, 16, 32, 51, 64, 127, 128, 190]

        for examine in extra_numbers:
            if examine in integers:
                assert node.contains(examine) == True
            else:
                assert node.contains(examine) == False

    def test_locate(self):
        node = Node(10)
        for add_numbers in [2, 3, 4, 5, 7, 8, 16, 32, 51, 64, 127, 128, 190]:
            node.insert_node(add_numbers)

        assert node.locate(190) == "larger.larger.larger.larger.larger.larger.larger"
        assert node.locate(3) == "smaller.larger"

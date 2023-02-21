import re


class Node:
    def __init__(self, value):
        self.value = value
        self.smaller = None
        self.larger = None

    def __repr__(self) -> str:
        return f"Node(value={self.value}, smaller={self.smaller}, larger={self.larger})"

    def get_node(self):
        return self

    def insert_node(self, value):
        if not isinstance(value, (int, float)) or value == self.value:
            raise Exception("Unable to insert value")

        if value > self.value:
            high_low = "larger"
        else:
            high_low = "smaller"

        if getattr(self, high_low) == None:
            setattr(self, high_low, Node(value))
        else:
            getattr(self, high_low).insert_node(value)

    def contains(self, value):
        print(self)
        if not isinstance(value, (int, float)):
            raise Exception("Numbers only.")

        if value == self.value:
            return True

        if value > self.value:
            high_low = "larger"
        else:
            high_low = "smaller"

        if getattr(self, high_low) == None:
            return False
        else:
            return getattr(self, high_low).contains(value)

    def locate(self, value):
        if not isinstance(value, (int, float)):
            raise Exception("Numbers only.")

        if value == self.value:
            return ""

        if value > self.value:
            high_low = "larger"
        else:
            high_low = "smaller"

        if getattr(self, high_low) == None:
            return
        else:
            path_string = high_low + "." + getattr(self, high_low).locate(value)
            return re.sub(r"\.$", "", path_string)


class BST(Node):
    def replace(self, node):
        if isinstance(node, Node):
            self.value = node.value
            self.smaller = node.smaller
            self.larger = node.larger
        else:
            raise Exception("replace() only accepts arguments of type Node")

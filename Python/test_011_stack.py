from p011_stack import Stack


def test_initialise():
    stack = Stack()
    assert stack.show() == {}


def test_add():
    stack = Stack()
    stack.append(1)
    assert stack.show() == {1: 1}


def test_pop():
    stack = Stack()
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.pop()
    assert stack.show() == {1: 1, 2: 2}


def test_empty():
    stack = Stack()
    assert stack.is_empty() == True
    stack.append(1)
    assert stack.is_empty() == False


def test_full():
    stack = Stack(1)
    assert stack.is_full() == False
    stack.append(1)
    assert stack.is_full() == True


def test_peek():
    stack = Stack()
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    stack.append(5)
    stack.append(6)
    assert stack.peek() == 6


def test_clear():
    stack = Stack()
    stack.append(1)
    stack.append(2)
    stack.append(3)
    stack.append(4)
    stack.append(5)
    stack.append(6)
    stack.append(7)
    stack.clear()
    assert stack.show() == {}


def test_autofill():
    stack = Stack(4)
    stack.append(True)
    stack.auto_fill(False)
    assert stack.show() == {1: True, 2: False, 3: False, 4: False}

class Stack:
    def __init__(self, max=10):
        self.max = max
        self.storage = []

    def append(self, inp):
        if len(self.storage) < self.max:
            self.storage.append(inp)
            print(self.storage)

    def pop(self):
        if len(self.storage) > 0:
            return self.storage.pop(len(self.storage) - 1)

    def show(self):
        print(self.storage)

    def is_empty(self):
        if len(self.storage) == 0:
            return True
        return False

    def is_full(self):
        if len(self.storage) == self.max:
            return True
        return False

    def peek(self):
        if len(self.storage) == 0:
            return
        return self.storage[len(self.storage) - 1]

    def clear(self):
        self.storage = []

    def auto_fill(self, inp):

        for filler in range(self.max - len(self.storage)):
            self.storage.append(inp)

    def show(self):
        show_stack = {}
        for stack_cycle in range(len(self.storage)):
            show_stack[stack_cycle + 1] = self.storage[stack_cycle]

        return show_stack

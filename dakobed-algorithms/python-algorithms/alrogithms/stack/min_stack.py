"""
Design a min stack that can access the top element and the minimum element in constant time


Maintain a stack of tuples whose first value is the elements value, the second the minimum element that has been
encountered

"""


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        current_minimum = min(x, self.getMin())
        self.stack.append((x, current_minimum))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0] if self.stack else None

    def getMin(self):
        return self.stack[-1][1] if self.stack else float('inf')

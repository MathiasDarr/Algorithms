class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.front = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        topElement = self.stack2.pop()
        while self.stack2:
            self.stack1.append(self.stack2.pop())
        return topElement

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) == 0

obj = MyQueue()
obj.push(1)
obj.push(2)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()
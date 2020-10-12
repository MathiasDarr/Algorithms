class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.root = root
        self._reset()

    def _reset(self):
        self.node = self.root
        self.stack = []

    def __iter__(self):
        self._reset()
        return self

    def __next__(self) -> int:
        """
        @return the next smallest number
        """
        while self.node:
            self.stack.append(self.node)
            self.node = self.node.left

        self.node = self.stack.pop()
        ret_val = self.node.val
        self.node = self.node.right
        return ret_val

    next = __next__


    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.stack or self.node
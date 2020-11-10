class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root):
        self.inOrder = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.inOrder.append(node.val)
            dfs(node.right)
        dfs(root)

        self.index =0

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index +=1
        return self.inOrder[self.index-1]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.index < len(self.inOrder):
            return True
        else:
            return False


root = TreeNode(7)
root.left = TreeNode(3)
root.right = TreeNode(15)
root.right.left = TreeNode(9)
root.right.right = TreeNode(20)

iterator = BSTIterator(root)
iterator.next()    # return 3
iterator.next()    # return 7
iterator.hasNext()  # return true
iterator.next()    # return 9
iterator.hasNext()  # return true
iterator.next()    # return 15
iterator.hasNext()  # return true
iterator.next()   # return 20
iterator.hasNext()  # return false



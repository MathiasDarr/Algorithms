class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inOrderIterative(self, root):
        if not root:
            return
        stack = []
        current = root
        while current or len(stack) > 0:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            print(current.val)
            current = current.right


root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(1)
solution = Solution()
solution.inOrderIterative(root)

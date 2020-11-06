class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root):
        inOrder = []
        stack = []
        current = root
        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            inOrder.append(current.val)
            current = current.right
        return inOrder
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
solution = Solution()
solution.inorderTraversal(root)
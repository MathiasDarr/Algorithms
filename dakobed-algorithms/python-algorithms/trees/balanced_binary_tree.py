class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root):
        def dfs(node):
            if not node:
                return 1
            left = dfs(node.left)
            right = dfs(node.right)
            if abs(left-right) > 1:
                return -1
            return max(left, right) + 1

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

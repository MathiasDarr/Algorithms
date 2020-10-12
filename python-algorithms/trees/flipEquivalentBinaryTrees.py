class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, root1, root2):
        pass


solution = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(8)
root.right = TreeNode(3)
root.right.left = TreeNode(6)

root = TreeNode(1)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(6)

root.right.left = TreeNode(2)
root.right.right = TreeNode(5)
root.right.right.left = TreeNode(8)
root.right.right.right = TreeNode(7)


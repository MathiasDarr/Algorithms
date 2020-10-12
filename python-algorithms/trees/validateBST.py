class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root):
        return self.isValidRecursive(root, float('-inf'),float('inf'))
    def isValidRecursive(self, node, minValue, maxValue):
        if not node:
            return True
        if node.val <= minValue or node.val >= maxValue:
            return False
        return self.isValidRecursive(node.left, minValue, node.val) and self.isValidRecursive(node.right, node.val, maxValue)

root = TreeNode(1)
root.left = TreeNode(1)

# root = TreeNode(6)
# root.left = TreeNode(4)
# root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(7)

solution = Solution()
solution.isValidBST(root)
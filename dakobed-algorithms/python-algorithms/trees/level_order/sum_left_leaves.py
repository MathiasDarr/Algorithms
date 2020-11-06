class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root):
        self.lSum = 0
        def recursiveLeftSum(node, isLeft):
            if not node:
                return
            if not node.left and not node.right and isLeft:
                self.lSum += node.val
                return
            recursiveLeftSum(node.left, True)
            recursiveLeftSum(node.right, False)
        recursiveLeftSum(root, False)
        return self.lSum

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
solution.sumOfLeftLeaves(root)
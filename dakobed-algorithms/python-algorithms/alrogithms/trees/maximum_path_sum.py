class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root):
        self.max_path_sum = float('-inf')
        self.maxPathSumRecursive(root)
        return self.max_path_sum
    def maxPathSumRecursive(self, node):
        if not node:
            return 0
        left = max(0, self.maxPathSumRecursive(node.left))
        right = max(0, self.maxPathSumRecursive(node.right))
        self.max_path_sum = max(self.max_path_sum, left+right+node.val)
        return max(left, right) + node.val

root = TreeNode(-10)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
solution.maxPathSum(root)
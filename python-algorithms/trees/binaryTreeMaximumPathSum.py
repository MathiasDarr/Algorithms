class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def maxPathSum(self, root):
        self.maxSum = float('-inf')
        self.maxPathSumRecursive(root)
        return self.maxSum

    def maxPathSumRecursive(self, node):
        if node == None:
            return 0
        left = max(0, self.maxPathSumRecursive(node.left))
        right = max(0, self.maxPathSumRecursive(node.right))
        self.maxSum = max(self.maxSum, left + right + node.val)
        return max(left, right) + node.val



head = TreeNode(-10)
head.left = TreeNode(9)
head.right = TreeNode(20)
head.right.left = TreeNode(15)
head.right.right = TreeNode(7)
solution = Solution()
solution.maxPathSum(head)
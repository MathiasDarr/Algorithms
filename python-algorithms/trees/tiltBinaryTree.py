class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root):
        if not root:
            return 0
        self.tilt = 0
        def findSum(node):
            if not node:
                return 0
            left = right = 0
            if node.left:
                left = findSum(node.left)
            if node.right:
                right = findSum(node.right)
            self.tilt += abs(right-left)
            return left+right+node.val
        findSum(root)
        return self.tilt


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)

solution = Solution()
solution.findTilt(root)

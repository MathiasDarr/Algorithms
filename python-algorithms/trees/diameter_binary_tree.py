class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):

        self.maxDiameter = 0
        def dfs(node):
            if not node:
                return 0
            left = 0
            right = 0
            if node.left:
                left = dfs(node.left)
            if node.right:
                right = dfs(node.right)
            self.maxDiameter = max(self.maxDiameter, left+right)
            return max(left, right) + 1
        dfs(root)
        return self.maxDiameter

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
solution = Solution()
solution.diameterOfBinaryTree(root)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root) -> bool:
        def dfs(node, minValue, maxValue):
            if node.val < minValue or node.val > maxValue:
                return False
            return dfs(node.left, float('-inf'), node.val) and dfs(node.right, node.val, float('inf'))
        return dfs(root, float('inf'), float('-inf'))

root = TreeNode(5)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(6)

solution = Solution()
solution.isValidBST(root)
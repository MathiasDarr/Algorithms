class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isUnivalTree(self,root):
        if not root:
            return True
        root_value = root.val
        def dfs(node):
            if not node:
                return True
            if node.val != root_value:
                return False
            return dfs(node.left) and dfs(node.right)
        return dfs(root)

root = TreeNode(1)
root.left = TreeNode(1)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right.right = TreeNode(2)

solution = Solution()
solution.isUnivalTree(root)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root, sum):
        def dfs(node, current_sum):
            if not node:
                return False
            if not node.left and not node.right and node.val + current_sum == sum:
                return True
            return dfs(node.left, current_sum+node.val) or dfs(node.right, current_sum+node.val)

        return dfs(root, 0)

root = TreeNode(-2)
# root.left = TreeNode(4)
root.right = TreeNode(-3)
# root.left.left = TreeNode(11)
# root.right.left = TreeNode(13)
# root.right.right = TreeNode(4)
# root.right.right.right = TreeNode(1)
# root.left.left.left = TreeNode(7)
# root.left.left.right = TreeNode(2)
solution = Solution()
solution.hasPathSum(root, -5)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root):
        def dfs(root):
            if not root: return 0
            # divided
            left = dfs(root.left)
            right = dfs(root.right)
            # conquer/merge
            if left == -1 or right == -1: return -1  # early stop

            if abs(left - right) > 1: return -1
            return max(left, right) + 1

        res = dfs(root)
        return res >= 0

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)
root.right.right.right.right = TreeNode(2)
solution = Solution()
solution.isBalanced(root)
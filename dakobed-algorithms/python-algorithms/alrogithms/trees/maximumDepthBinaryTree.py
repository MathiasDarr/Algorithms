class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root) :

        def dfs(node, depth):
            if not node:
                return depth
            ldepth = dfs(node.left, depth+1)
            rdepth = dfs(node.right, depth+1)
            return max(ldepth, rdepth)
        return dfs(root, 0)


solution = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
solution.maxDepth(root)
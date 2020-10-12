class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root):
        if not root:
            return 0
        array = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            array.append(root.val)
            dfs(root.right)
        dfs(root)
        return min([abs(s-t) for s, t in zip(array,array[1:])])

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
solution = Solution()
minDiff = solution.minDiffInBST(root)
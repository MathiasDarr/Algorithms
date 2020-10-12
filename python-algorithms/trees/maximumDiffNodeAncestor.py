class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root: TreeNode):
        self.maxDiff = 0
        if not root:
            return 0
        def dfs(node, minValue, maxValue):
            if not node:
                return
            if node.val< minValue:
                minValue = node.val
            if node.val> maxValue:
                maxValue = node.val
            self.maxDiff = max([self.maxDiff, abs(maxValue-node.val), abs(minValue - node.val)])
            if node.left:
                dfs(node.left, minValue, maxValue)
            if node.right:
                dfs(node.right, minValue, maxValue)


        dfs(root, root.val, root.val)
        return self.maxDiff


root = TreeNode(8)
root.left = TreeNode(3)

root.right = TreeNode(10)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.left.left = TreeNode(1)

root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)

solution = Solution()
solution.maxAncestorDiff(root)
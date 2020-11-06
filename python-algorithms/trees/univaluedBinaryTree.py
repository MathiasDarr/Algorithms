class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root):
        self.result = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)

        dfs(root)
        return self.result

    def isUnivalTree(self, root):
        if not root or ( not root.left and not root.right):
            return True
        stack = []
        val = root.val
        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)
        while stack:
            node = stack.pop()
            if node.val != val:
                return False
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return True

root = TreeNode(1)
root.left = TreeNode(4)
root.left.left = TreeNode(4)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(1)
root.left.right = TreeNode(4)
root.left.right.right = TreeNode(1)

solution = Solution()
solution.longestUnivaluePath(root)

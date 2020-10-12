class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root):
        result = []
        def dfs(node, currentPath):
            if not node.left and not node.right:
                result.append("->".join(currentPath + [str(node.val)]))
                return
            if node.left:
                dfs(node.left, currentPath + [str(node.val)])
            if node.right:
                dfs(node.right, currentPath + [str(node.val)])

        dfs(root, [])

        return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
solution = Solution()
result = solution.binaryTreePaths(root)
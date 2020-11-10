class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root):


        def dfs(node, path):
            if not node.left and not node.right:
                paths.append('->'.join(path))
            if node.left:
                dfs(node.left, path + [str(node.left.val)])
            if node.right:
                dfs(node.right, path + [str(node.right.val)])

        if not root:
            return []
        paths = []
        dfs(root, [str(root.val)])
        return paths

solution = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)

solution.binaryTreePaths(root)
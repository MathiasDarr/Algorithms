class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root):
        output = []
        def dfs(node, path):
            if not node:
                return
            if not node.left and not node.right:
                output.append(path+[node.val])
                return
            dfs(node.left, path +[node.val])
            dfs(node.right, path +[node.val])

        dfs(root, [])
        return output

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
solution = Solution()
solution.binaryTreePaths(root)
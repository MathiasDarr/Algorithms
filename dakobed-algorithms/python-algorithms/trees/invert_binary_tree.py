class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inOrderTraversal(self, node):
        if not node:
            return
        self.inOrderTraversal(node.left)
        print(node.val)
        self.inOrderTraversal(node.right)

    def invertTree(self, root):
        def dfs(node):
            if not node:
                return
            left = dfs(node.left)
            right = dfs(node.right)
            node.left = right
            node.right = left
            return node
        return root

solution = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

newRoot = solution.invertTree(root)
solution.inOrderTraversal(newRoot)
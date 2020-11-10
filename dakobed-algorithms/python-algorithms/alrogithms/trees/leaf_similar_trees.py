class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def leafSimilar(self, root1, root2):

        def dfs(node, leaves):
            if not node:
                return
            dfs(node.left, leaves)
            if not node.left and not node.right:
                leaves.append(node.val)
            dfs(node.right, leaves)

        leaves_tree1 = []
        leaves_tree2 = []
        dfs(root1, leaves_tree1)
        dfs(root2, leaves_tree2)

        return leaves_tree1 == leaves_tree2


root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(9)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

root2 = TreeNode(3)
root2.left = TreeNode(5)
root2.right = TreeNode(1)
root2.left.left = TreeNode(6)
root2.left.right = TreeNode(7)

root2.right.left = TreeNode(4)
root2.right.right = TreeNode(2)
root2.right.right.left = TreeNode(9)
root2.right.right.right = TreeNode(8)


solution = Solution()
solution.leafSimilar(root, root2)
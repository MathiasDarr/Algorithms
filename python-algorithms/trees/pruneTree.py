class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def printInOrder(self, root):
        def dfs(node, depth):
            if not node:
                return
            dfs(node.left, depth=1)
            print("node val {} and depth {} ".format(node.val, depth))
            dfs(node.right, depth+1)
        dfs(root, 0)

    def pruneTree(self, root):
        def dfs(node):
            if not node:
                return False
            left = dfs(node.left)
            right = dfs(node.right)

            if not left:
                node.left = None
            if not right:
                node.right = None

            return True if left or right or node.val == 1 else False
        return root if dfs(root) else None

root = TreeNode(0)
root.right = TreeNode(0)
root.right.left = TreeNode(0)
root.right.right = TreeNode(0)
solution = Solution()

solution.printInOrder(root)

newRoot = solution.pruneTree(root)
print("after prune")
solution.printInOrder(newRoot)
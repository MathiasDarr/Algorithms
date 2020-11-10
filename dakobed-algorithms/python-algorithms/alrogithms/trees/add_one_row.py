class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def printInOrdre(self, node):
        if not node:
            return
        self.printInOrdre(node.left)
        print(node.val)
        self.printInOrdre(node.right)


    def addOneRow(self, root, v, d):
        def dfs(root, d, isLeft):
            if d == 1:
                if root is None:
                    return TreeNode(v)
                if isLeft:
                    return TreeNode(v, root, None)
                else:
                    return TreeNode(v, None, root)
            if root is None:
                return
            root.left = dfs(root.left, d - 1, True)
            root.right = dfs(root.right, d - 1, False)
            return root

        return dfs(root, d, True)


solution = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right.left = TreeNode(5)

solution.addOneRow(root, 1, 2)


solution.printInOrdre(root)
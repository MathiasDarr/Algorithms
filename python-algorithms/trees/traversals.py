class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root):
        self.result = []
        self.postorderTraversalRecursive(root)
        return self.result
    def postorderTraversalRecursive(self, node):
        if not node:
            return
        self.postorderTraversalRecursive(node.left)
        self.postorderTraversalRecursive(node.right)
        self.result.append(node.val)


    def preorderTraversal(self, root):
        self.result = []
        self.preorderTraversalRecursive(root)
        return self.result
    def preorderTraversalRecursive(self, node):
        if not node:
            return
        self.result.append(node.val)
        self.preorderTraversalRecursive(node.left)
        self.preorderTraversalRecursive(node.right)

    def inorderTraversal(self, root):
        self.result = []
        self.inorderTraversalRecursive(root)
        return self.result
    def inorderTraversalRecursive(self, node):
        if not node:
            return
        self.inorderTraversalRecursive(node.left)
        self.result.append(node.val)
        self.inorderTraversalRecursive(node.right)



root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
solution = Solution()
solution.postorderTraversal(root)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, t):
        self.output = []
        def preorder(node):
            if not node:
                return
            self.output += str(node.val)
            if node.left:
                self.output.append('(')
                preorder(node.left)
                self.output.append(')')
            if node.right:
                if not node.left:
                    self.output.append('(')
                    self.output.append(')')
                self.output.append('(')
                preorder(node.right)
                self.output.append(')')
        preorder(t)
        return ''.join(self.output)

solution = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)

solution.tree2str(root)


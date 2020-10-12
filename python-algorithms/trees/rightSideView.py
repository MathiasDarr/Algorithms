class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            newstack = []
            level = []
            while stack:
                node = stack.pop(0)
                level.append(node.val)
                if node.left:
                    newstack.append(node.left)
                if node.right:
                    newstack.append(node.right)
            result.append(level[-1])
            stack = newstack
        return result



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
solution = Solution()
result = solution.rightSideView(root)
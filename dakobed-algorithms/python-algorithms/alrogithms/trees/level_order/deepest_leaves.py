class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root):
        if not root:
            return 0
        stack = [root]
        while stack:
            newstack = []
            level_sum = 0
            while stack:
                node = stack.pop()
                level_sum += node.val
                if node.left:
                    newstack.append(node.left)
                if node.right:
                    newstack.append(node.right)
            stack = newstack
        return level_sum

solution = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(6)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.left.left = TreeNode(7)
root.right.right.right = TreeNode(8)

solution.deepestLeavesSum(root)
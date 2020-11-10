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
        right_side_view = []
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
            print(level)
            right_side_view.append(level[-1])
            stack = newstack
        return right_side_view

    def largestValues(self, root):
        if not root:
            return []


        stack = [root]
        larget_value_per_row = []
        while stack:
            level = []
            current_level_max = float('-inf')
            while stack:
                node = stack.pop()
                current_level_max = max(current_level_max, node.val)
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            larget_value_per_row.append(current_level_max)
            stack = level
        return larget_value_per_row

solution = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
solution.rightSideView(root)
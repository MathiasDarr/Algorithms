"""
LeetCode 199. Binary Tree Right Side View

This is quite clearly a level order problem, for which we do BFS with a queue.

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):
        if not root:
            return
        right_side_view = []
        queue = [root]
        while queue:
            new_queue =[]
            level = []
            while queue:
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            right_side_view.append(level[-1])
            queue = new_queue
        return right_side_view

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)
solution = Solution()
solution.rightSideView(root)
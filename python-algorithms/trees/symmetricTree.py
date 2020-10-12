class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def isSymmetric(self, root):
#
#         stack = [root]
#         levels = []
#         while stack:
#             new_stack = []
#             level = []
#             while stack:
#                 node = stack.pop(0)
#                 level.append(node.val)
#                 new_stack.append(node.left)
#                 new_stack.append(node.right)
#             levels.append(level)
#             stack = new_stack
#         return levels


class Solution:
    def isSymmetric(self, root):
        return self.isMirror(root, root)
    def isMirror(self, t1, t2):
        if t1 == None and t2 == None:
            return True
        if t1 == None or t2 == None:
            return False
        if t1.val != t2.val:
            return False
        return self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(4)
solution = Solution()
isSymmetric = solution.isSymmetric(root)
"""Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in
the given BST.

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root):
        pass

solution = Solution()
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(2)
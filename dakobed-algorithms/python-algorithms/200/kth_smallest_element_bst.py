"""
LeetCode 230 kth smallest element in a BST

Given a binary search tree, write a function kth smallest to find the kth smallest element in it

Recursive inorder solution:
    O(n)

Iterative solution:

What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How
would you optimize the kthSmallest routine?


"""
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallestIterative(self, root, k):
        if not root:
            return
        stack = deque()
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                k -=1
                if k == 0:
                    return node.val
                node = node.right
        return -1

    def kthSmallest(self, root, k):
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            inorder.append(node.val)
            dfs(node.right)

        k
        inorder = []
        dfs(root)
        return inorder[k-1]


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)

solution = Solution()
solution.kthSmallestIterative(root, k=3)
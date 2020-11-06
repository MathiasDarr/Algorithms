"""
Iterative traversals.

PreOrder:

    Which do I add first right or left?


Iterative:

Algorithm goes as follows

maintain a variable current_node initialized to root

Iterate until the stack is empty or current_node is none
    - Until current node has no left children, add left child to stack, updating current_node = current_node.left

    - Once no more left children can be added to stack, we pop a node from the stack, adding its value to the result
        - We process the left most children first since they are on the top of the stack

    - Set current_node = current_node.right, iterating through right subtree



"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inOrderTraversal(self, root):
        if not root:
            return []
        stack = []
        inorder = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            inorder.append(node.val)
            node = node.right

        return inorder

    def preorderTraversal(self, root):

        if not root:
            return []
        queue= deque([root])
        preorder = []
        while queue:
            node = queue.pop()
            if node:
                preorder.append(node.val)
                queue.append(node.right)
                queue.append(node.left)



        return preorder

root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(3)
root.left.left = TreeNode(2)

solution = Solution()
solution.inOrderTraversal(root)
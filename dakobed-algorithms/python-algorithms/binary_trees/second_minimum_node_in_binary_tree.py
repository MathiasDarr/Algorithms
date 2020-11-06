"""
Given a binary tree s.t that
Binary Tree constratins
    1) every node has one or two child nodes, but never one.
    2) every node's value is the minimum of it's childrens value
        node.val = min(node.left.val, node.right.val)

    Given such a binary tree, return the second minimum value in the set made of all the node's value in the whole tree

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findSecondMinimumValue(self, root):
        def dfs(node):
            if not node:
                return
            unique_values.add(node.val)
            dfs(node.left)
            dfs(node.right)

        unique_values = set()

        dfs(root)

        ### By the constraints placed on the tree, the root value is the minimum value.
        min_value  = root.val
        second_smallest = float('inf')

        for v in unique_values:
            if min_value < v < second_smallest:
                second_smallest = v
        return second_smallest if second_smallest!= float('inf') else -1

root = TreeNode(2)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
solution = Solution()
solution.findSecondMinimumValue(root)
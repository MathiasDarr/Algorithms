"""
LeetCode 337 House Robber III

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the
"root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that
"all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked
houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.


RECURSIVE SOLUTION:

- Make recursive calls, two cases,
    1) this house is robbed, and the two children not
    2) this house has not been robbed, the two children have been robbed

Algorithm:
    helper function takes a node as input and returns a two-element array, where the first element represents the maximum
    amount of money the htief can rob if starting from this node w/out robbing this node.  The second element is the maximum
    amount of money the their can rob if starting from this node & robbing this node

MEMOIZATION + RECURSION SOLUTION



"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root):
        def helper(node):
            if not node:
                return (0,0)
            left = helper(node.left)
            right = helper(node.right)
            rob_this_node = node.val + left[1] + right[1]
            not_rob_this_node = max(left) + max(right)
            return [rob_this_node, not_rob_this_node]

        return max(helper(root))


root = TreeNode(3)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(3)
root.right.right = TreeNode(1)

solution = Solution()
solution.rob(root)
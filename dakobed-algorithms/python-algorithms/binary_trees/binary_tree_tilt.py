"""

The tilt of a node is defined as
tilt(node) = abs(sum(node.left) - sum(node.right)

The tilt of a node therefore is the difference between left and right subtree sums

Recursive function that returns the subtree sum of a node


tilt(node) = abs(left_subtree_sum - right_subtree_sum)

return left_subtree_sum + right_subtree_sum + node.val


"""



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root):
        self.cumulative_tilt = 0
        def dfs(node, current_sum):
            if not node:
                return 0
            leftsum = dfs(node.left, current_sum + node.val)
            rightsum = dfs(node.right, current_sum + node.val)
            self.cumulative_tilt += abs(rightsum-leftsum)
            return leftsum + rightsum + node.val
        dfs(root, 0)
        return self.cumulative_tilt


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

solution = Solution()
solution.findTilt(root)
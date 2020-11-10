"""

Path sum III,

Given a binary tre in which each node contains an integer value
find the number of paths that sum to a given a value, the path does not have to start at the root.

traverse the binary tree, calling dfs from each node




"""


from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root, target):
        def preorder(node, curr_sum):
            nonlocal count
            if not node:
                return

            curr_sum += node.val
            if curr_sum == target:
                count += 1

            count += h[curr_sum - target]
            h[curr_sum] += 1
            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)
            h[curr_sum] -= 1

        h = defaultdict(int)
        count = 0
        preorder(root, 0)
        return count



        # def dfs(node, path, current_sum):
        #     if current_sum == target:
        #         paths.append([*path])
        #     if not node:
        #         return
        #     if node.left:
        #         dfs(node.left, path + [node.left.val], current_sum + node.left.val)
        #     if node.right:
        #         dfs(node.right, path + [node.right.val], current_sum + node.right.val)
        #
        # if not root:
        #     return
        # stack = [root]
        # paths = []
        # while stack:
        #     node = stack.pop()
        #     dfs(node, [], 0)
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
        # return paths





    def hasPathSum(self, root, sum):
        def dfs(node, current_sum):
            if not node:
                return False
            if not node.left and not node.right and node.val + current_sum == sum:
                return True
            return dfs(node.left, current_sum+node.val) or dfs(node.right, current_sum+node.val)

        return dfs(root, 0)

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.right.right = TreeNode(11)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.left = TreeNode(1)


solution = Solution()
solution.pathSum(root, 8)
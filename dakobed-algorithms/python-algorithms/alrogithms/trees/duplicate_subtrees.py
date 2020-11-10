"""
Returns root of all subtrees which have a duplicate

Serialize the following tree
        1
    2       3
         4      5


1,2,#,#,3,4,#,#,5,#,#

"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import defaultdict

class Solution:
    def findDuplicateSubtrees(self, root):

        def dfs_serialization(node):
            if not node:
                return '#'
            left = dfs_serialization(node.left)
            right = dfs_serialization(node.right)
            serialization = '{},{},{}'.format(node.val, left, right)
            hashMap[serialization] = hashMap.get(serialization, 0) + 1
            if hashMap[serialization] == 2:
                result.append(node)
            return serialization
        hashMap = {}
        result = []
        dfs_serialization(root)
        return result




root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(2)
root.right.left.left = TreeNode(4)
root.right.right = TreeNode(4)


solution = Solution()
duplicates = solution.findDuplicateSubtrees(root)
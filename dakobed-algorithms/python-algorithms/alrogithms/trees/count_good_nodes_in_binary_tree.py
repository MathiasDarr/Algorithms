"""
Recursive


"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root):

        def dfs(node, maximum_value):
            if not node:
                 return
            # print("I am at node: {} & the maximum value is: {}".format(node.val, maximum_value))
            if node.val >= maximum_value:
                self.n_nodes +=1
            new_max = max(node.val, maximum_value)
            dfs(node.left, new_max)
            dfs(node.right, new_max)
        self.n_nodes = 0
        dfs(root, float('-inf'))
        return self.n_nodes

# root = TreeNode(3)
# root.left = TreeNode(1)
# root.right = TreeNode(4)
# root.left.left = TreeNode(3)
# root.right.left = TreeNode(1)
# root.right.right = TreeNode(5)


root = TreeNode(3)
root.left = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)

solution = Solution()
solution.goodNodes(root)
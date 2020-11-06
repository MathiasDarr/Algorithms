class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubTree(self, s, t):

        def dfs(nodes, nodet):
            if not nodes and not nodet:
                return True
            if not nodes or not nodet:
                return False
            if nodes.val != nodet.val:
                return False
            return dfs(nodes.left, nodet.left) and dfs(nodes.right, nodet.right)

        stack = [s]
        while stack:
            node = stack.pop()
            if node.val == t.val:
                if dfs(node, t):
                    return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False



s = TreeNode(3)
s.left = TreeNode(4)
s.right = TreeNode(5)
s.left.left = TreeNode(1)
s.left.right = TreeNode(2)
s.left.right.left = TreeNode(0)

t = TreeNode(4)
t.left = TreeNode(1)
t.right = TreeNode(2)


solution = Solution()
solution.isSubTree(s,t)
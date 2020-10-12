class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubTreeRecursive(self, sNode, tNode):
        if not sNode and not tNode:
            return True
        if not sNode or not tNode:
            return False
        if sNode.val != tNode.val:
            return False
        return self.isSubTreeRecursive(sNode.left, tNode.left) and self.isSubTreeRecursive(sNode.right, tNode.right)


    def isSubTree(self, s, t):
        if not t:
            return not s
        stack = [s]
        while stack:
            node = stack.pop()
            if node.val == t.val:
                if self.isSubTreeRecursive(node, t):
                    return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False


r1 = TreeNode(3)
r1.left = TreeNode(4)
r1.right = TreeNode(5)
r1.left.left = TreeNode(1)
r1.left.right = TreeNode(2)

r2 = TreeNode(20)
r2.left = TreeNode(1)
r2.right = TreeNode(2)

solution = Solution()
solution.isSubTree(r1, r2)
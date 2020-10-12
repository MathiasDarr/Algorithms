class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root, L, R):
        self.result = 0
        def dfs(node):
            if not node:
                return
            if node.val >= L and node.val <= R:
                self.result += node.val
            if node.val > L:
                dfs(node.left)
            if node.val < R:
                dfs(node.right)
        dfs(root)
        return self.result

    def rangeSumIterative(self, root, L,R):
        result = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                print(node.val)
                if L<= node.val <= R:
                    result += node.val
                if node.val > L:
                     stack.append(node.left)
                if node.val < R:
                     stack.append(node.right)
        return result
solution = Solution()
root = TreeNode(10)
root.left = TreeNode(5)
root.left.right = TreeNode(8)
root.left.right.left = TreeNode(7)

root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.right.right = TreeNode(18)
solution.rangeSumBST(root, 7,15)

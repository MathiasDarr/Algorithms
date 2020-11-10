from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def printInOrder(self, root):
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            print(node.val)
            dfs(node.right)
        dfs(root)

    def invertTree(self, root):
        def dfs(node):
            if not node:
                return None
            left = dfs(node.left)
            right = dfs(node.right)

            node.right = left
            node.left = right
            return node

        return dfs(root)

    def inverTreeIterative(self, root):
        if not root:
            return root

        queue = deque()
        queue.append(root)

        while len(queue):
            node = queue.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

solution = Solution()
solution.printInOrder(root)
print("invert")
newRoot = solution.invertTree(root)
solution.printInOrder(newRoot)

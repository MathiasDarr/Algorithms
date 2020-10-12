class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
class Solution:
    def preorder(self, root):
        self.result = []
        self.preorderRecursive(root)
        return self.result
    def preorderRecursive(self, node):
        if not node:
            return
        self.result.append(node.val)
        if node.children:
            for child in node.children:
                self.preorderRecursive(child)

    def postrder(self, root):
        self.result = []
        self.postorderRecursive(root)
        return self.result
    def postorderRecursive(self, node):
        if not node:
            return
        if node.children:
            for child in node.children:
                self.postorderRecursive(child)
        self.result.append(node.val)

root = Node(1)
left = Node(3)
left.children = [Node(5), Node(6)]
root.children =[left, Node(2), Node(4)]

solution = Solution()
result = solution.postrder(root)
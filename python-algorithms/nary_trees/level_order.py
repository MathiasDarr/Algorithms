class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root):
        levels = []
        stack = [root]
        while stack:
            newstack = []
            level = []
            while stack:
                node = stack.pop(0)
                level.append(node.val)
                if node.children:
                    newstack += node.children
            levels.append(level)
            stack = newstack
        return levels
root = Node(1)
left = Node(3)
left.children = [Node(5), Node(6)]
root.children =[left, Node(2), Node(4)]

solution = Solution()
results = solution.levelOrder(root)

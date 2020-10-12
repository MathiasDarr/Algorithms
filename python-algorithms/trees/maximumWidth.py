class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     max_width = 0
#     leftmost_positions = {}
#
#     def widthOfBinaryTree(self, root):
#         self.get_width(root, 0, 1)
#         return self.max_width
#     def get_width(self, root, depth, position):
#         if root == None:
#             return
#
#         if depth not in self.leftmost_positions:
#             self.leftmost_positions[depth] = position
#
#         self.max_width = max(self.max_width, position - self.leftmost_positions[depth] +1)
#         self.get_width(root.left, depth+1, position * 2)
#         self.get_width(root.right, depth+1, position * 2+1)

class Solution:
    def widthOfBinaryTree(self, root):
        if not root:
            return 0
        max_width = 0
        stack = [(root, 1)]
        while stack:
            newstack = []
            while stack:
                node, position = stack.pop()
                if node.left:
                    newstack.append((node.left, position *2))
                if node.right:
                    newstack.append((node.right, position *2 +1))

            if len(newstack) > 0:
                positions = [entry[1] for entry in newstack]
                positions.sort()
                node1pos = positions[0]
                node2pos = positions[-1]
                max_width = max(max_width, node2pos - node1pos + 1)
            elif len(newstack) ==0:
                max_width = max(max_width, 1)
            stack = newstack
        return max_width

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(1)
root.right.right = TreeNode(4)
root.left.right = TreeNode(2)


# root.left.left.left = TreeNode(2)
# root.right.right.right = TreeNode(4)

# root.left.left = TreeNode(5)
# root.left.right = TreeNode(3)
# root.right.right = TreeNode(9)
solution = Solution()
solution.widthOfBinaryTree(root)

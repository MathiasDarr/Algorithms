class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printRightChildren(self, node):
        while node:
            print(node.val)
            node = node.right
    def preOrder(self, head):
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            print(node.val)


    def flatten(self, root):
        if not root or (not root.left and not root.right):
            return
        stack = [root]
        while stack:
            current = stack.pop()
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
            root.right = current
            root = root.right
            root.left = None


            # if not current:
            #     current.right = stack.pop()
            #     current = current.right
            # else:
            #     if current.right:
            #         stack.append(current.right)
            #     current.right = current.left
            #     current = current.left





root = TreeNode(0)
root.left = TreeNode(2)
root.right = TreeNode(5)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right.right = TreeNode(6)

solution = Solution()
print('before flatten')
solution.preOrder(root)
solution.flatten(root)
print('after flatten')

solution.printRightChildren(root)
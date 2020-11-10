class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def print_in_order(self,node):
        if not node:
            return
        self.print_in_order(node.left)
        print(node.val)
        self.print_in_order(node.right)


    def searchBST(self, root, val):
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == val:
                return node
            elif node.val > val and node.left:
                stack.append(node.left)
            elif node.val < val and node.right:
                stack.append(node.right)
        return None

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

solution = Solution()
subTree = solution.searchBST(root, 2)

solution.print_in_order(subTree)
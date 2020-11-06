class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root, k):
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            inorder_array.append(node.val)
            inorder(node.right)

        inorder_array = []
        inorder(root)
        return inorder_array[k-1]

    def kthSmallestIterative(self, root, k):
        if not root:
            return []
        stack = []
        current_node = root
        while current_node or stack:
            while current_node:
                stack.append(current_node)
                current_node = current_node.left
            current_node = stack.pop()
            k -=1
            if k ==0:
                return current_node.val
            current_node = current_node.right
        return -1


        # if not root:
        #     return []
        # stack = []
        # current_node = root
        #
        # while current_node or stack:
        #     while current_node:
        #         stack.append(current_node.left)
        #         current_node = current_node.left
        #     current_node = stack.pop()
        #     k -= 1
        #     if k == 0:
        #         return current_node.val
        #     current_node = current_node.right
        #

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(2)

solution = Solution()
solution.kthSmallest(root,1)

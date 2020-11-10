"""
Delete a node in a BST
search w/ DFS for the node w/ the key to be deleted

If we find it, attempt to replace this node with the smallest node in the right subtree, it is guaranteed to not break
the BST ordering of the tree.

If the right subtree is empty, replace the deleted node w/ the left subtree

Recursive Solution:
    What do we return? Nothing? Node?

In this case we return a node.

node.left = recusrsive(node.left)

Once we have found the node,
    find the smallest node in the right subtree

        call this node smallest_right
            if empty, simply return the left subtree
            if not empty, set the left pointer of smallest_right to node.left

        if not empty, set the left value of the


"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def print_in_order(self, node):
        if not node:
            return
        self.print_in_order(node.left)
        print(node.val)
        self.print_in_order(node.right)

    def deleteNode(self, root, key):
        def dfs(node):
            if not node:
                return None
            if node.val == key:
                smallestNode_in_right = self.findSmallest(node.right)
                if not smallestNode_in_right:
                    return node.left
                smallestNode_in_right.left = node.left
                return node.right
            elif key < node.val:
                node.left = self.deleteNode(node.left, key)
                return node
            elif key > node.val:
                node.right = self.deleteNode(node.right, key)
                return node
        return dfs(root)

    def findSmallest(self, root):
        if not root:
            return None
        while root.left:
            root = root.left
        return root

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

solution = Solution()
new_root = solution.deleteNode(root, 3)
solution.print_in_order(new_root)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: TreeNode, to_delete):
        to_delete_set = set(to_delete)
        res = []

        def helper(root, is_root):
            if not root: return None
            root_deleted = root.val in to_delete_set
            if is_root and not root_deleted:
                res.append(root)
            root.left = helper(root.left, root_deleted)
            root.right = helper(root.right, root_deleted)
            return None if root_deleted else root
        helper(root, True)
        return res

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
solution = Solution()
solution.delNodes(root, [1,5])
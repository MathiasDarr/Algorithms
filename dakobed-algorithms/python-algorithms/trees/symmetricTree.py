class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root):
        queue = [root, root]
        while queue:
            t1 = queue.pop(0)
            t2 = queue.pop(0)
            if not t1 and not t2:
                continue
            if not t1 or not t2:
                return False
            if t1.val != t2.val:
                return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        return True

    # def isSymmetric(self, root):
    #     def isMirror(node1, node2):
    #         if not node1 and not node2:
    #             return True
    #         if not node1 or not node2:
    #             return False
    #         if node1.val != node2.val:
    #             return False
    #         return isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)
    #     return isMirror(root, root)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
solution = Solution()
solution.isSymmetric(root)
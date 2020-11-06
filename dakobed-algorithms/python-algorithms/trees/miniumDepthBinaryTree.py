class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = 0
        stack = [root]
        while stack:
            newstack = []
            depth +=1
            while stack:
                node = stack.pop()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    newstack.append(node.left)
                if node.right:
                    newstack.append(node.right)
            stack = newstack
        return depth
root = TreeNode(2)

root.right = TreeNode(3)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


solution = Solution()
solution.minDepth(root)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrderBottom(self, root):
        levels = []
        queue = [root]
        while queue:
            new_queue =[]
            level = []
            while queue:
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            levels.append(level)
            queue = new_queue
        return levels

solution = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.left.left = TreeNode(15)
root.left.right = TreeNode(7)

solution.levelOrderBottom(root)
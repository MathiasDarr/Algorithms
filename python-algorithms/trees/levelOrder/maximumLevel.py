class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root):
        if not root:
            return
        queue = [root]
        level = 0
        maxLevel = 0
        maxLevelSum = root.val
        while queue:
            level +=1
            newqueue = []
            levelsum = 0
            while queue:
                node = queue.pop(0)
                levelsum += node.val
                newqueue.append(node.left) if node.left else None
                newqueue.append(node.right) if node.right else None

            print('level sum: {}'.format(levelsum))
            if levelsum > maxLevelSum:
                maxLevel = level
                maxLevelSum = levelsum
            queue = newqueue
        return maxLevel


root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(0)
root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)

solution = Solution()
solution.maxLevelSum(root)
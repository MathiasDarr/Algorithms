class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        # if not root:
        #     return
        # stack = [root]
        # levels =[]
        # while stack:
        #     newstack = []
        #     level = []
        #     while stack:
        #         node = stack.pop(0)
        #         level.append(node.val)
        #         newstack.append(node.left) if node.left else None
        #         newstack.append(node.right) if node.right else None
        #     levels.append(level)
        #     stack = newstack
        # return [row if i %2 ==0 else row[::-1] for i, row in enumerate(levels)]

        queue = [root]
        output = []

        while queue:
            newQueue = []
            level = []
            while queue:
                node = queue.pop(0)
                level.append(node.val)
                if node.left:
                    newQueue.append(node.left)
                if node.right:
                    newQueue.append(node.right)
            output.append(level)
            print(output)
            queue = newQueue
        return [row if i %2 ==0 else row[::-1] for i, row in enumerate(output)]

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)



# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.right.right = TreeNode(5)

solution = Solution()
solution.zigzagLevelOrder(root)

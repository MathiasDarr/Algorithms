class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isMonotonic(sequence, increasing=True):
    if increasing:
        return all(earlier < later for earlier, later in zip(sequence, sequence[1:]))
    else:
        return all(earlier > later for earlier, later in zip(sequence, sequence[1:]))

#
# print(isMonotonic([3, 3, 7], True))


class Solution:

    def isMonotonic(self, sequence, increasing=True):
        if increasing:
            return all(earlier < later for earlier, later in zip(sequence, sequence[1:]))
        else:
            return all(earlier > later for earlier, later in zip(sequence, sequence[1:]))

    def isEvenOddTree(self, root):
        if not root:
            return True

        queue = [root]
        levels = []
        level_count = 0
        while queue:
            new_queue = []
            level = []
            while queue:
                node = queue.pop(0)
                level.append(node.val)

                if level_count % 2 == 1:
                    if node.val % 2 == 1:
                        return False
                else:
                    if node.val % 2 == 0:
                        return False



                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
            levels.append(level)

            if level_count % 2 == 1:
                if not self.isMonotonic(level, False):
                    return False
            else:
                if not self.isMonotonic(level, True):
                    return False
            level_count += 1
        return True


root = TreeNode(5)

root.left = TreeNode(9)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)

root.right = TreeNode(1)
root.right.left = TreeNode(7)

solution = Solution()
solution.isEvenOddTree(root)

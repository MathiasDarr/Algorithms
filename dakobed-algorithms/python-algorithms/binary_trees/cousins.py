"""
Nodes are cousins if they are at same depth but have different parents

Make use of a hash map to keep track of each nodes parents.  If the values x and y are found on the same row,
return True if the parents (as found in the hash map) are not the same

"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def isCousins(self, root, x, y):
        queue = [(root, TreeNode(-1))]
        while queue:
            new_queue = []
            level_map = {}
            while queue:
                node, parent = queue.pop()
                level_map[node.val] = parent.val
                if node.left:
                    new_queue.append((node.left, node))
                if node.right:
                    new_queue.append((node.right, node))

            if x in level_map and y in level_map and level_map[x] != level_map[y]:
                return True
            queue = new_queue
        return False


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.right = TreeNode(5)

solution = Solution()
solution.isCousins(root, 2, 3)
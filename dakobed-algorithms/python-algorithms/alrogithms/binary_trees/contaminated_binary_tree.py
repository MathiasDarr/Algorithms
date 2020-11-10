"""
LeetCode 1261

"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root):

        def dfs(node, i):
            if not node:
                return
            node.val = i
            self.element_hash_set.add(i)
            dfs(node.left, (2*i)+1)
            dfs(node.right, (2*i)+2)

        self.element_hash_set = set()
        dfs(root, 0)

    def find(self, target):
        return target in self.element_hash_set

root = TreeNode(-1)
root.left = TreeNode(-1)
root.right = TreeNode(-1)
root.left.left = TreeNode(-1)
root.left.right = TreeNode(-1)

findElements = FindElements(root)
findElements.find(8)


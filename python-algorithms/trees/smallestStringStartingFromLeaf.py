class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def smallestFromLeaf(self, root):
        self.result = "~"
        def dfs(node, path):
            if not node:
                return
            path.append(chr(node.val + ord('a')))
            if not node.left and not node.right:
                self.result = min(self.result, ''.join(reversed(path)))

            dfs(node.left, path)
            dfs(node.right, path)
            path.pop()
        dfs(root, [])
        return self.result

root = TreeNode(25)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(0)
root.right.right = TreeNode(2)



# root = TreeNode(2)
# root.left = TreeNode(2)
# root.left.right = TreeNode(1)
# root.left.right.left = TreeNode(0)
#
# root.right = TreeNode(1)
# root.right.left = TreeNode(0)


solution = Solution()
solution.smallestFromLeaf(root)


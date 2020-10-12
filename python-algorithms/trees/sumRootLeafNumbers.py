class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    result = 0
    def sumNumbers(self, root):
        if not root:
            return 0
        def dfs(node, path):
            if not node.left and not node.right:
                path = path + [node.val]
                number = 0

                for i in range(len(path)-1,-1, -1):
                    number  += path[i] * 10 **(len(path) -i-1)
                self.result += number
                return
            if node.left:
                dfs(node.left, path + [node.val])
            if node.right:
                dfs(node.right, path+ [node.val])
        dfs(root, [])
        return self.result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
solution = Solution()
solution.sumNumbers(root)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root):
        def dfs(node, minNode, maxNode):
            if not node:
                return
            if node.val < minNode.val:
                print('yes')

                node.val, minNode.val = minNode.val, node.val
                return
            elif node.val > maxNode.val:
                print('yes')
                node.val, maxNode.val = maxNode.val, node.val
                return
            dfs(node.left, minNode, node) and dfs(node.right, node, maxNode)

        dfs(root, TreeNode(float('-inf')), TreeNode(float('inf')))


        # def dfs(node, minV, maxV):
        #     if not node:
        #         return True
        #     if node.val < minV or node.val > maxV:
        #         return False
        #     return dfs(node.left, minV, node.val) and dfs(node.right, node.val, maxV)
        # return dfs(root, float('-inf'), float('inf'))

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(2)
solution = Solution()

print(root.val)
solution.recoverTree(root)
print(root.val)
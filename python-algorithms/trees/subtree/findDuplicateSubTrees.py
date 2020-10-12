import collections

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printinOrder(self, root):
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            print(node.val)
            dfs(node.right)
        dfs(root)

    def deserialize(self, bstString):
        def dfs(nums):
            pass
        return dfs(bstString.split(','))



    def findDuplicateSubtrees(self, root):

        hashMap = {}
        result = []
        def preorder(node):
            if not node:
                return '#'
            left = preorder(node.left)
            right = preorder(node.right)
            serialization = '{},{},{}'.format(node.val, left, right)
            hashMap[serialization] = hashMap.get(serialization, 0) + 1
            if hashMap[serialization] ==2:
                result.append(node)
            return serialization
        preorder(root)
        return result

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

root.right.left = TreeNode(2)
root.right.left.left = TreeNode(4)
root.right.right = TreeNode(4)

solution = Solution()
duplicates = solution.findDuplicateSubtrees(root)


for tree in duplicates:
    solution.printinOrder(tree)
    print("next tree")


# newRoot = solution.deserialize(bstString)
# solution.printinOrder(newRoot)

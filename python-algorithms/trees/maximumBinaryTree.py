class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def printInOrder(self, root):
        if not root:
            return
        self.printInOrder(root.left)
        print(root.val)
        self.printInOrder(root.right)
    def printPreOrder(self, root):
        if not root:
            return
        print(root.val)
        self.printPreOrder(root.left)
        self.printPreOrder(root.right)
    def constructMaximumBinaryTree(self, nums):
        return self.recursiveMaximumBinaryTree(nums)

    def recursiveMaximumBinaryTree(self, nums):
        if len(nums) ==0:
            return
        if len(nums) ==1:
            return TreeNode(nums[0])

        maxValue = float('-inf')
        indexMax = -1
        for i, num in enumerate(nums):
            if num > maxValue:
                maxValue = num
                indexMax = i
        node = TreeNode(maxValue)
        node.left = self.recursiveMaximumBinaryTree(nums[:indexMax])
        node.right = self.recursiveMaximumBinaryTree(nums[indexMax+1:])
        return node

    def insertIntoMaxTree(self, root, val):
        def dfs(root):
            if not root or root.val < val:
                return TreeNode(val, root, None)
            root.right = dfs(root.right)
            return root
        return dfs(root)


    # def insertIntoMaxTree(self, root, val):
    #     nums = self.getInOrder(root)
    #     return self.recursiveMaximumBinaryTree(nums +[val])
        # if val > root.val:
        #     newRoot = TreeNode(val)
        #     newRoot.left = root
        #     return newRoot
        # stack = [(root, 0, False)]
        # while stack:
        #     node, parent, left = stack.pop()
        #     if val > node.val:
        #         newRoot = TreeNode(val)
        #         prerderArray = self.getPreOrder(newRoot)
        #         newRoot = self.recursiveMaximumBinaryTree(prerderArray)
        #         if left:
        #             parent.left = newRoot
        #             parent.left.left = node
        #         else:
        #             parent.right = newRoot
        #             parent.right.left = node
        #         break
        #     else:
        #         if node.left:
        #             stack.append((node.left, node, True))
        #         if node.right:
        #             stack.append((node.right, node, False))
        # return root

    def getPreOrder(self, root):
        results = []
        stack = [root]
        while stack:
            node = stack.pop()
            results.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return results

    def getInOrder(self, root):
        result = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        dfs(root)
        return result
        #
        # def getPreOrderRecursive(node):
        #     if not node.left and not node.right:
        #         return
        #     results.append(node.val)
        #     getPreOrderRecursive(node)
        #     getPreOrderRecursive(node.right)
        # getPreOrderRecursive(root)
        # return results


nums = [3,2,1,6,0,5]
solution = Solution()
# root = solution.constructMaximumBinaryTree(nums)

root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(4)
root.left.right = TreeNode(1)
# solution.getInOrder(root)
newRoot = solution.insertIntoMaxTree(root,3)
solution.printInOrder(newRoot)
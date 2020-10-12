class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:



    def buildTree(self, preorder, inorder):
        def helper(preStart, inStart, inEnd):
            if preStart >= len(preorder) or inStart > inEnd:
                return None
            root = TreeNode(preorder[preStart])
            inOrderIndex = inorder.index(root.val)
            root.left = helper(preStart+1, inStart, inOrderIndex-1)
            root.right = helper(preStart+inOrderIndex-inStart+1, inOrderIndex+1, inEnd)
            return root
        return helper(0,0,len(inorder) -1)

    def printInOrder(self, node):
        if not node:
            return
        if node.left:
            self.printInOrder(node.left)
        print(node.val)
        if node.right:
            self.printInOrder(node.right)


preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
solution = Solution()
root = solution.buildTree(preorder, inorder)
solution.printInOrder(root)
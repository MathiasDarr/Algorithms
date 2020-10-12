class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head, root):
        if root == None:
            return False
        if head.val == root.val and self.isPathExists(head, root):
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)


    def isPathExists(self, head, root):
        if head == None:
            return True
        if root == None:
            return False
        if head.val == root.val:
            return self.isPathExists(head.next, root.left) or self.isPathExists(head.next, root.right)
        else:
            return False

    # def isSubPath(self, head, root):
    #     listVals = self.listValues(head)
    #
    #     def dfs(node, listIndex):
    #         if listIndex == len(listVals):
    #             return True
    #         if not node:
    #             return False
    #
    #         print(listIndex)
    #         if node.val == listVals[listIndex]:
    #             nextIndex = listIndex +1
    #         elif node.val == listVals[0]:
    #             nextIndex = 1
    #         else:
    #             nextIndex = 0
    #         return dfs(node.left, nextIndex) or dfs(node.right, nextIndex)
    #
    #
    #     return dfs(root, 0)
    #
    # def listValues(self, head):
    #     listVals = []
    #     while head:
    #         listVals.append(head.val)
    #         head = head.next
    #
    #     return listVals

    def inOrderTraversal(self, root):
        inOrder = []
        def dfs(node, listIndex):
            if not node:
                return
            dfs(node.left)
            inOrder.append(node.val)
            dfs(node.right)
        dfs(root)
        return inOrder

solution = Solution()
head = ListNode(1)
head.next = ListNode(10)


root = TreeNode(1)
root.right = TreeNode(1)
root.right.left = TreeNode(10)
root.right.right = TreeNode(1)
root.right.right.left = TreeNode(9)



root.left = TreeNode(4)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(1)
root.right = TreeNode(4)
root.right.left = TreeNode(2)
root.right.left.left = TreeNode(6)
root.right.left.right = TreeNode(8)
root.right.left.right.right = TreeNode(3)
root.right.left.right.left = TreeNode(1)

solution.isSubPath(head,root)
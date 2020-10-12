class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def minimumDistanceBST(self, root):
        inOrderTraversal = []
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            inOrderTraversal.append(node.val)
            inOrder(node.right)
        inOrder(root)
        return min([abs(n1 - n2) for n1, n2 in zip(inOrderTraversal, inOrderTraversal[1:])])
        # return inOrderTraversal
        # return min([n1-n2 for n1, n2 in zip(inOrder, inOrder[1:])])



    def printInOrder(self, root):
        if not root:
            return
        self.printInOrder(root.left)
        print(root.val)
        self.printInOrder(root.right)

    def mergeTrees(self, t1, t2):
        if not t1:
            return t2
        elif not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1

    def mergeTreesIterative(self, t1, t2):
        if not t1 and not t2:
            return
        elif not t1:
            return t2
        elif not t2:
            return 2

        newRoot = TreeNode(t1.val + t2.val)
        stack = [(t1.left,t2.left), (t1.right, t2.right)]

        while stack:
            node1, node2 = stack.pop()
            node1.val += node2.val
            if not node1.left:
                node1.left = node2.left
            else:
                stack.append((node1.left,node2.left))

            if not node1.right:
                node1.right = node2.right
            else:
                stack.append((node1.right,node2.right))





root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)

root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(9)
root2.right.right = TreeNode(29)

solutuion = Solution()
newRoot = solutuion.mergeTrees(root, root2)
solutuion.printInOrder(newRoot)

order = solutuion.minimumDistanceBST(root2)
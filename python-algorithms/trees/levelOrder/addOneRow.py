class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def printInOrder(self, root):
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            print(node.val)
            dfs(node.right)
        dfs(root)
    def addOneRow(self, root, v, d):
        if d ==1:
            return TreeNode(v, root, None)
        stack = [(root,1)]
        while len(stack) > 0:
            node, depth = stack.pop()
            if not node:
                continue
            if depth == d-1:
                temp = node.left
                node.left = TreeNode(v)
                node.left.left = temp
                temp = node.right
                node.right = TreeNode(v)
                node.right.right = temp
            else:
                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))
        return root
        # def dfs(node, depth, left):
        #     if depth ==d-1:
        #         if node is None:
        #             return TreeNode(v)
        #         if left:
        #             return TreeNode(v, node, None)
        #         else:
        #             return TreeNode(v, None, node)
        #     if not node:
        #         return
        #     node.left = dfs(node.left, depth+1, True)
        #     node.right = dfs(node.right, depth+1, False)
        #     return node
        # return dfs(root, 1, True)

    #
    # def addOneRow(self, root, v, d):
    #     stack = [(root, None, False)]
    #     depth = 1
    #     while depth < d-1:
    #         newStack = []
    #         while stack:
    #             node, parent, left = stack.pop()
    #             if node.left:
    #                 newStack.append((node.left, node, True))
    #             if node.right:
    #                 newStack.append((node.right, node, False))
    #         depth +=1
    #         if len(newStack) == 0:
    #             break
    #         stack = newStack
    #
    #         print([node.val for node, _, _ in stack])
    #     for node, parent, left in stack:
    #         newNode = TreeNode(v)
    #         if left:
    #             newNode.left = node
    #             parent.left = newNode
    #         else:
    #             newNode.right = node
    #             parent.right = newNode
    #     return [node.val for node , _, _ in stack]


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right.left = TreeNode(5)



# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(1)

# root.right = TreeNode(6)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(1)
# root.right.left = TreeNode(5)



# root.left = TreeNode(2)
# root.right = TreeNode(6)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(1)
# root.right.left = TreeNode(5)

solution = Solution()
# solution.printInOrder(root)

v = 1
d = 2
newRoot = solution.addOneRow(root, 1, 2)
solution.printInOrder(newRoot)
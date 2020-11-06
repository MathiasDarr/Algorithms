"""
Path sum II

Given a binary tree and a target value, return all root-leaf paths s.t that path's sum equals the given the given sum

Path sum III
find number of paths that sum to a given value, don't necsarrily have to end at a leaf



"""



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def printInOrder(self, node):
        if not node:
            return
        self.printInOrder(node.left)
        print(node.val)
        self.printInOrder(node.right)

    def pathSum(self, root, target):
        if not root:
            return 0
        def dfs(node, path, path_sum):
            if node:
                if path_sum == target:
                    paths.append(path)
                    self.count +=1
                if node.left:
                    dfs(node.left, path + [node.left.val], path_sum + node.left.val)
                if node.right:
                    dfs(node.right, path + [node.right.val], path_sum + node.right.val)
        stack = [root]
        paths = []
        self.count = 0
        while stack:
            node = stack.pop()
            dfs(node, [], 0)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return self.count



    def pathSumRootToLeaf(self, root, target):
        """
        This function returns the paths from root to leaf that sum to target
        """
        def dfs(node, path, path_sum):
            if not node.left and not node.right:
                if path_sum == target:
                    paths.append(path)
                    return
            if node.left:
                dfs(node.left, path + [node.left.val], path_sum + node.left.val)
            if node.right:
                dfs(node.right, path + [node.right.val], path_sum + node.right.val)
        paths = []
        dfs(root, [root.val], root.val)
        return paths

solution = Solution()
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(-3)
root.right.right = TreeNode(11)
root.left.left = TreeNode(3)
root.left.right = TreeNode(2)
root.left.left.left = TreeNode(3)
root.left.left.right = TreeNode(-2)
root.left.right.right = TreeNode(1)

solution.pathSum(root, 8)
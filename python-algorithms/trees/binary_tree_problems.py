class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def leftLeafSum(self, root):
        self.lsum = 0

        self.recursiveLeftSum(root, False)
        return self.lsum
    def recursiveLeftSum(self, node, isleft):
        if not node:
            return
        if not node.left and not node.right:
            if isleft:
                self.lsum += node.val

        self.recursiveLeftSum(node.left, True)
        self.recursiveLeftSum(node.right, False)

    def levelOrder(self, root):
        if not root:
            return
        stack = [root]
        levels =[]
        while stack:
            newstack = []
            level = []
            while stack:
                node = stack.pop(0)
                level.append(node.val)
                newstack.append(node.left) if node.left else None
                newstack.append(node.right) if node.right else None
            levels.append(level)
            stack = newstack
        return levels


    def averageOfLevels(self, root):
        if not root:
            return
        stack = [root]
        averages =[]
        while stack:
            newstack = []
            level = []
            while stack:
                node = stack.pop(0)
                level.append(node.val)
                newstack.append(node.left) if node.left else None
                newstack.append(node.right) if node.right else None


            averages.append(sum(level)/len(level))
            stack = newstack
        return averages

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
solution.leftLeafSum(root)

levels = solution.levelOrder(root)

print("The sum of the left leaves is " + str(solution.leftLeafSum(root)))

def sortedArrayBST(arr):
    if not arr:
        return None
    left = 0
    right = len(arr)-1
    mid = int(left + (right - left) / 2)
    node = TreeNode(arr[mid])

    node.left = sortedArrayBST(arr[:mid])
    node.right = sortedArrayBST(arr[mid+1:])
    return node


arr = [-10, -3,0, 5, 9]
tree = sortedArrayBST(arr)


'''
Maximum & Minimum Depth of binary trees
'''

class Solution:
    def maximumDepth(self, root):
        return self.maximumDepthRecursive(root, 0)
    def minimumDepth(self, root):
        if root == None:
            return 0
        depth = 0
        stack = [root]
        while stack:
            newstack = []
            depth +=1
            while stack:
                node = stack.pop()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    newstack.append(node.left)
                if node.right:
                    newstack.append(node.right)
            stack = newstack
        return depth

    def maximumDepthRecursive(self, node, depth):
        if not node:
            return depth
        ldepth = self.maximumDepthRecursive(node.left, depth+1)
        rdepth = self.maximumDepthRecursive(node.right, depth+1)
        return max(ldepth, rdepth)


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
solution = Solution()
print("The maximum dpeth of this binaryh tree is " + str(solution.maximumDepth(root)))
print("The minimum dpeth of this binaryh tree is " + str(solution.minimumDepth(root)))


def pathSum(root, target):
    return pathSumRecursive(root, target)


def pathSumRecursive( root, target):
    if not root.left and not root.right:
        return True if root.val == target else False

    leftPath = False
    rightPath = False
    if root.left:
        leftPath = pathSumRecursive(root.left, target - root.val)
    if root.right:
        rightPath = pathSumRecursive(root.right, target - root.val)

    return leftPath or rightPath


# class Solution:
#     def isSymmetric(self, root: TreeNode) -> bool:
#         pass
#     def isSameTree(s, t):
#         if not s and not t:
#             return True
#         if not s or not t:
#             return False
#
#
#     def isSymmetricIterative(self, root):
#
#
#
# root = TreeNode(3)
# root.left = TreeNode(4)
# root.right = TreeNode(4)
# root.left.left = TreeNode(2)
# root.right.right = TreeNode(2)
# print("These two trees are symmetirc " + str(isSymmetric(root)))
#
# haspath = pathSum(root, 9)


def isSubtree(s,t):
    if not s:
        return False
    if isSame(s,t):
        return True
    return isSubtree(s.left, t) or isSubtree(s.right, t)

def isSame(s, t):
    if not s and not t:
        return True
    if not s or not t:
        return False
    if s.val != t.val:
        return False
    return isSame(s.left, t.left) and isSame(s.right, t.right)


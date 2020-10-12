class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def decimalToBinary(n):
    return bin(n).replace("0b","")


def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


class Solution:

    def sumRootToLeaf(self, root):
        self.paths = []
        def dfs(node, path):
            if not node.left and not node.right:
                self.paths.append(path + [node.val])
                return
            if node.left:
                dfs(node.left, path +[node.val])
            if node.right:
                dfs(node.right, path + [node.val])


        dfs(root, [])
        currentSum = 0
        for binary in self.paths:
            binary_number =  ''.join([str(b) for b in binary])
            currentSum += binaryToDecimal(int(binary_number))
        return currentSum
root = TreeNode(1)
root.left = TreeNode(0)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

solution = Solution()
results = solution.sumRootToLeaf(root)

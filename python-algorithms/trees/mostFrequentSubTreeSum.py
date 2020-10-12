class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFrequentTreeSum(self, root):
        freqs = {}
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left) if node.left else 0
            right = dfs(node.right) if node.right else 0
            subTreeSum = left + right + node.val
            freqs[subTreeSum] = freqs.get(subTreeSum,0) +1
            return subTreeSum

        dfs(root)
        freqsList = sorted(freqs.items(), key=lambda item: item[1])
        maxFreq = freqsList[-1][1]
        results = []
        for i in range(len(freqsList) - 1, -1, -1):
            if freqsList[i][1] == maxFreq:
                results.append(freqsList[i][0])
        return freqs

solution = Solution()
root = TreeNode(1)
# root.left = TreeNode(2)
root.right = TreeNode(1)

results = solution.findFrequentTreeSum(root)


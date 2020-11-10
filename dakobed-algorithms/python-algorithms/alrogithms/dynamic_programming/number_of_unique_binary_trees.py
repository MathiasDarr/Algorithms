"""
LeetCode 96

For each value of n, we choose a root value
    - root = r
    - the number of unique trees w/ n values whose root is r is
        n trees w/ values less than r * n trees w/ values greater than r

Memoization Solution:

    recursive

Iterative
    - Proceeds similary but notice that only half of the calculations are required

    - Double for loop:
        Fix an i, s.t dp[i] = number of unique BSTs with i values


How are we going to generate the trees



n = 4




"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n:
            return []
        dp = [[None for j in range(n+1)] for i in range(n+2)]

        for i in range(1, n+2):
            dp[i][i-1] = [None]
        # l length
        for l in range(1, n+1):
            for i in range(1, n-l+2):
                j = i + l - 1
                dp[i][j] = []
                for k in range(i, j+1):
                    left_subtrees = dp[i][k-1]
                    right_subtrees = dp[k+1][j]
                    for lefttree in left_subtrees:
                        for righttree in right_subtrees:
                            root = TreeNode(k)
                            root.left = lefttree
                            root.right = righttree
                            dp[i][j].append(root)
        return dp[1][n]


    def numTrees(self, n):
        dp = {0:1, 1:1, 2:2}

        for i in range(2, n+1):
            # mid = i//2 + (1 if i % 2 ==1 else 0)
            dp[i] = 0
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]

    #def numTrees(self, n):
        # def num_unique_recursive(number):
        #     if number in memo:
        #         return memo[number]
        #     total = sum([num_unique_recursive(i-1) * num_unique_recursive(number-i) for i in range(1, number+1)])
        #     memo[number] = total
        #     return total
        #
        # memo = {0:1, 1:1}
        # return num_unique_recursive(n)

solution = Solution()
solution.generateTrees(3)
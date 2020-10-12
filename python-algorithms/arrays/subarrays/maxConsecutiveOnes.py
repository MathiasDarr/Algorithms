class Solution:
    def longestOne(self, A, K):
        left = 0
        maxLength = 0
        for right in range(len(A)):
            if A[right] == 0:
                if K>=0:
                    K -=1
                    while K < 0:
                        if A[left] == 0:
                            K+=1
                        left +=1
            maxLength = max(maxLength, right-left + 1)
        print("{} {}".format(right,left))
        return maxLength
A = [1,1,1,0,0,0,1,1,1,1,0]
K = 2

solution = Solution()
solution.longestOne(A,K)
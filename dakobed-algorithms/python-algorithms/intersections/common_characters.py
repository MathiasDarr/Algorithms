from collections import Counter
class Solution:
    def commonChars(self, A):
        intersection = Counter(A[0])
        for word in A:
            intersection &= Counter(word)
        return list(intersection.elements())

solution = Solution()
solution.commonChars(["bella","label","roller"])

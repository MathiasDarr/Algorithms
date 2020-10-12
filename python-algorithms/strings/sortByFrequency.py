from collections import Counter
class Solution:
    def frequencySort(self, s):
        sCounter = Counter(s)
        sortedByCount = sorted(sCounter.items(), key=lambda x: x[1], reverse=True)
        return ''.join([key * count for key, count in sortedByCount])

solution = Solution()
s = 'tree'
solution.frequencySort(s)
class Solution:
    def reverseWords(self,s):
        return ' '.join([word[::-1] for word in s.split(" ")])
    def reverseStr(self, s, k):
        splitS = [s[i:i + k] for i in range(0, len(s), k)]
        return ''.join([split[::-1] if i%2 ==0 else split for i,split in enumerate(splitS)])
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) -1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left+=1
            right -=1
        return s
# s = "Let's take LeetCode contest"
# solution = Solution()
# solution.reverseWords(s)

solution = Solution()
s2 = "abcdefg"
solution.reverseStr(s2, 2)


s = ["h","e","b","l","l","o"]
solution.reverseString(s)
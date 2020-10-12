


class Solution:
    def numDecodings(self, s):
        dp = [-1] * len(s)
        def recur(s, decode_pointer):
            if decode_pointer >= len(s):
                return 1
            if dp[decode_pointer] > -1:
                return dp[decode_pointer]

            answer = 0
            for i in range(1, 3):
                if decode_pointer + i <= len(s):
                    substr = s[decode_pointer:decode_pointer + i]
                    if int(substr) >= 1 and int(substr) <= 26 and not substr.find('0') == 0:
                        answer += recur(s, decode_pointer + i)
            dp[decode_pointer] = answer
            return dp[decode_pointer]

        return recur(s, 0)
    def numDecodings(self, s):

        dp = [-1] * len(s)
        def recur(s, index):
            if index >= len(s):
                return 1
            if dp[index] != -1:
                return dp[index]
            dp[index] = sum([recur(s, index+i) for i in [1,2]  for substring in s[index:index+i] if index+i<=len(s) and int(s[index:index+i]) >0 and int(s[index:index+i]) <26])
            return dp[index]

        return recur(s, 0)

s = "12"
solution = Solution()
solution.numDecodings(s)
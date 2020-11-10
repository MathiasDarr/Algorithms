"""

Given two strings S and T, return if they are equal after backspacking


"""



class Solution:


    def backspaceCompare(self, S, T):
        def build_string(string):
            news = []
            for c in string:
                if c != '#':
                    news.append(c)
                else:
                    if len(news) > 0:
                        news.pop()
            return ''.join(news)
        return build_string(S) == build_string(T)

solution = Solution()
S = "ab#c"
T = "ad#c"

solution.backspaceCompare(S, T)
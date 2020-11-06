class Solution:
    def findComplement(self, num):
        binary = bin(num)[2:]
        answer = 0
        for i, v in enumerate(binary[::-1]):
            if v == '0':
                answer += 2 ** i
        return answer

solution = Solution()
solution.findComplement(5)
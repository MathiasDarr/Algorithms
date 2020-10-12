class Solution:
    def pathInZigZagTree(self, label):
        n = label
        level = 0
        while n >0:
            n //= 2
            level +=1

        nlevel = level
        path = []
        n = label
        if level % 2 ==0:
            x = n - 2 ** (level - 1)
            n = (2 ** (level) - 1) - x

        while nlevel >0:
            odd = (nlevel-1) % 2
            if odd:
                x = n - 2 ** (nlevel-1)
                newIndex = (2 ** (nlevel) - 1) -x
                path.append(int(newIndex))
            else:
                path.append(int(n))
            n = n/2 if n % 2 ==0 else (n-1)/2
            nlevel -=1
        return path[::-1]

solution = Solution()
solution.pathInZigZagTree(26)
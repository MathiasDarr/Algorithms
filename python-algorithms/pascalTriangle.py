class Solution:
    def generate(self, numRows ):
        if numRows ==0:
            return []
        elif numRows == 1:
            return [1]
        row1 = [1]
        row2 = [1,1]
        output= [row1, row2]
        for i in range(2,numRows):
            row = []
            for j in range(1, i):
                row.append(output[i-1][j] + output[i-1][j-1])
            row = [1] + row + [1]
            output.append(row)
        return output
solution = Solution()
solution.generate(5)
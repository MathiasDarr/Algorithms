class Sol





board = [[1,3,5,7],
         [10, 11, 16,20],
         [23,30,34,60]
         ]

cols = list(zip(*board))
print(cols[0])
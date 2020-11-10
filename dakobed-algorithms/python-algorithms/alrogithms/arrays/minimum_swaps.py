"""

You are given an unordered array consisting of consecutive integers [1, 2, 3, ..., n] without any duplicates. You
are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in
ascending order.

i   arr                   swap (indices)
0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
5   [1, 2, 3, 4, 5, 6, 7]


Solution:
    Look at each index & compare the indexp osition w/ its element value if its the same then move to the next index position

    If index position is not the same as element value than treat element value as index value for finding the next element

"""


def minimumSwaps(arr):
    # initialize number of swaps as 0
    swaps = 0
    # create a dictionary which holds value, index pairs of our array
    # [4,3,1,2] --> {4: 1, 3: 2, 1: 3, 2: 4}
    getIndex = dict(zip(arr, range(1, len(arr) + 1)))
    for i in range(1, len(arr) + 1):
        # swap only if value is not equal to index
        if getIndex[i] != i:
            """
            Example of a proper swap when i=1
            {4: 1, 3: 2, 1: 3, 2: 4} --> {4: 3, 3: 2, 1: 1, 2: 4}
            [4,3,1,2] --> [1,3,4,2]
            Full swap is not required i.e. we don't have to set 1:1 or arr[0]=1(i:i or arr[i-1]=i) because we will never use these two values again. Therefore we can keep these two values as it is. And thus our swap looks as follows.
            {4: 1, 3: 2, 1: 3, 2: 4} --> {4: 3, 3: 2, 1: 3, 2: 4}
            [4,3,1,2] --> [4,3,4,2]
            """
            getIndex[arr[i - 1]] = getIndex[i]
            arr[getIndex[i] - 1] = arr[i - 1]
            swaps += 1
    return swaps



arr = [4,3,1,2]
minimumSwaps(arr)
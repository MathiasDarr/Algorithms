


def plusOne(digits):
    i = len(digits) -1
    result = []
    incrementIndex = -1
    while i >=0:
        if digits[i] == 9 and incrementIndex == -1:
            print(incrementIndex)
            digits[i] = 0
        elif incrementIndex == -1:
            incrementIndex = i
            digits[i] += 1
        result = [digits[i]] + result
        i -=1
    if incrementIndex == -1:
        result = [1] + result
    return result
digits = [9,8,7,6,5,4,3,2,1,0]
plusOne(digits)



def reverse(x):
    rev = 0
    n = x
    if n < 0:
        n = n * (-1)

    while n > 0:
        rev = (rev * 10) + (n % 10)
        n = n // 10

    if rev > 2 ** 31 - 1 or rev < -2 ** 31:
        return 0
    if x < 0:
        return rev * -1
    else:
        return rev

x = 123
rev = reverse(x)
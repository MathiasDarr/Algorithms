

def addBinary(a, b):
    lengthA = len(a)
    lengthB = len(b)

    if(len(a) > len(b)):
        b = '0' * (lengthA - lengthB) + b
    else:
       a = '0' * (lengthB - lengthA) + a

    newInteger = ''

    i = len(a) -1
    carry = 0
    while i >=0:
        sum = carry
        sum += 1 if a[i] == '1' else 0
        sum += 1 if b[i] == '1' else 0

        result = ('1' if sum % 2 == 1 else '0' )
        newInteger = result + newInteger

        carry = 0 if sum < 2 else 1
        i -=1

    if carry == 1:
        newInteger = '1' + newInteger
    return newInteger

a = '1'
b = '111'
result = addBinary(a,b)

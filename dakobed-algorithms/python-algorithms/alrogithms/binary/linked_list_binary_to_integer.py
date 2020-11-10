class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getDecimalValue(self, head):
        number = []
        while head:
            number.append(head.val)
            head = head.next
        return sum([number[i] * (2 ** i) for i in range(len(number[::-1]))])

head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(0)
head.next.next.next = ListNode(1)
head.next.next.next.next = ListNode(0)
head.next.next.next.next.next = ListNode(0)
head.next.next.next.next.next.next = ListNode(1)
head.next.next.next.next.next.next.next = ListNode(1)
head.next.next.next.next.next.next.next.next = ListNode(1)
head.next.next.next.next.next.next.next.next.next = ListNode(0)
head.next.next.next.next.next.next.next.next.next.next = ListNode(0)
head.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
head.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
head.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
head.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)
head.next.next.next.next.next.next.next.next.next.next.next.next.next.next.next = ListNode(0)


solution = Solution()


# answer = 0
# for i in range(len(number[::-1])):
#     answer += number[i] * (2 ** i)
# print(answer)
# answer = sum([number[i] * (2 ** i) for i in range(len(number[::-1]))])

solution.getDecimalValue(head)
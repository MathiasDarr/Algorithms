class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def printList(self, head):

        while head:
            print(head.val)
            head = head.next


    def removeNthFromEnd(self, head, n):
        dummy = ListNode(-1)
        dummy.next = head
        first = dummy
        second = dummy

        for i in range(n):
            first = first.next
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next

solution = Solution()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution.printList(head)

newList = solution.removeNthFromEnd(head, 5)

print('remove ')
solution.printList(newList)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def printList(self, head):
        while head:
            print(head.val)
            head = head.next

    def addTwoNumbers(self, l1, l2):

        dummyHead = ListNode(-1)
        current = dummyHead
        carry = 0
        while l1 or l2:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            sum = v1+v2 +carry
            carry =1 if sum >= 10 else 0
            current.next = ListNode(sum % 10)
            current = current.next

            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        if carry ==1:
            current.next = ListNode(1)

        return dummyHead.next


head1 = ListNode(5)
# head1.next = ListNode(4)
# head1.next.next = ListNode(3)

head2 = ListNode(5)
# head2.next = ListNode(6)
# head2.next.next = ListNode(4)
solution = Solution()
result = solution.addTwoNumbers(head1, head2)
solution.printList(result)
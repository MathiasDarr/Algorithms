class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def printList(self, head):
        while head:
            print(head.val)
            head = head.next

    def oddEvenList(self, head):
        if not head or not head.next:
            return head
        oddHead = head
        evenHead = head.next
        odd = oddHead
        even = evenHead

        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        odd.next = evenHead
        return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

solution = Solution()
newHead = solution.oddEvenList(head)
solution.printList(newHead)
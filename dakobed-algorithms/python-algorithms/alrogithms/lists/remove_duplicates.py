class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def printList(self, head):
        while head:
            print(head.val)
            head = head.next
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head

        prev = None
        current = head
        while current and current.next:
            if current.val != current.next:
                prev = current
                current = current.next
            else:
                while current.next and current.val == current.next.val:
                    current = current.next
                current = current.next
                if prev:
                    prev.next = current
                else:
                    head = current
        return head

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(3)

solution = Solution()
newHead = solution.deleteDuplicates(head)
solution.printList(newHead)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def printList(self, head):
        while head:
            print(head.val)
            head = head.next
    def removeElements(self, head, val):
        dummy = ListNode(-1)
        dummy.next = head
        current = dummy

        while current:
            temp = current.next
            while temp and temp.val == val:
                temp = temp.next
            current.next= temp
            current = current.next
        return dummy.next

head = ListNode(6)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next.next = ListNode(6)


solution = Solution()
removedElements = solution.removeElements(head, 6)
solution.printList(removedElements)
# Definition for singly-linked list.
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
        if head.next and head.val == head.next.val:
            while(head.next and head.val == head.next.val):
                head = head.next
            head = head.next
            return self.deleteDuplicates(head)
        else:
            head.next = self.deleteDuplicates(head.next)
        return head


    def removeDuplicatesII(self, head):
        if not head or not head.next:
            return head

        prev = None
        current = head
        while current and current.next:
            if current.val != current.next.val:
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


# head = ListNode(1)
# head.next = ListNode(1)
# head.next.next = ListNode(2)

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)
head.next.next.next.next.next = ListNode(5)

solution = Solution()
newHead = solution.deleteDuplicates(head)
print('print List')
solution.printList(newHead)



# solution = Solution()
# newHead = solution.deleteDuplicates(head)
# solution.printList(newHead)

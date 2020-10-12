class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge(self, l1, l2):
        while l1:
            l1_next = l1.next
            l2_next = l2.next
            l1.next = l2
            if l1_next == None:
                break
            l2.next = l1_next
            l1 = l1_next
            l2 = l2_next
    def printList(self, head):
        while head:
            print(head.val)
            head = head.next
    def reverseList(self, head):
        prev = None
        current = head

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

    def reorderList(self, head):

        l1 = head

        prev = None
        slow = head
        fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        l2 = self.reverseList(slow)
        self.merge(l1, l2)
        return head

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)


solution = Solution()
# revhead = solution.reverseList(head)

mergedList = solution.reorderList(head)
solution.printList(mergedList)

# solution.printList(revhead)


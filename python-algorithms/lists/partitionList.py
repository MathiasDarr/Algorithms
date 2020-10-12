class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def printList(self, head):
        while head:
            print(head.val)
            head = head.next

    def partition(self, head, x):
        leftList = ListNode(-1)
        rightList = ListNode(-1)
        leftHead = leftList
        rightHead = rightList

        while head:
            if head.val < x:
                leftList.next = head
                leftList = leftList.next
            else :
                rightList.next = ListNode(head.val)
                rightList = rightList.next
            head = head.next
        leftList.next = rightHead.next
        return leftHead.next

head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)

x = 3

solution = Solution()
newHead = solution.partition(head, x)
solution.printList(newHead)
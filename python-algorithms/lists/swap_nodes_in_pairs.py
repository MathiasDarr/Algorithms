class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def printList(self, head):
        while head:
            print(head.val)
            head = head.next
    def swapPairsRecursive(self, head):
        if not head or not head.next:
            return head
        secondNode = head.next
        head.next = self.swapPairsRecursive(head.next.next)
        secondNode.next = head
        return secondNode

    def swapPairsIterative(self, head):
        temp = ListNode(-1)
        temp.next = head
        current = temp

        while current.next and current.next.next:
            firstNode = current.next
            secondNode = current.next.next
            firstNode.next = secondNode.next
            current.next = secondNode
            current.next.next = firstNode
            current = current.next.next
        return temp.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
solution = Solution()
newHead = solution.swapPairsRecursive(head)
solution.printList(newHead)
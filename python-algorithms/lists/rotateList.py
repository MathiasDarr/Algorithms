class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def printList(self, node):
        while node:
            print(node.val)
            node = node.next
    def rotateRight(self, head, k):
        if not head:
            return
        count = 0
        current = head
        prev = ListNode(-1)
        while current:
            count +=1
            prev.next = current
            prev = prev.next
            current = current.next

        k = k % count
        if k ==0:
            return head
        current = head
        newCount = 0
        while newCount < count-k-1:
            newCount +=1
            current = current.next
        newHead = current.next
        prev.next = head
        current.next = None
        return newHead

head = ListNode(1)
head.next = ListNode(2)



k = 2

solution = Solution()
newHead = solution.rotateRight(head, k)
solution.printList(newHead)
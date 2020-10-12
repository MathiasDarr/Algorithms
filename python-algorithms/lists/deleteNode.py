class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def printList(self, head):
        while head:
            print(head.val)
            head = head.next
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

solution = Solution()
head = ListNode(4)
head.next = ListNode(5)
head.next.next = ListNode(1)
head.next.next.next = ListNode(9)

solution.deleteNode(head.next.next)
solution.printList(head)
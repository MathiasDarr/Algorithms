# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse_linked_list(self, head):
        prev = None
        current = head

        while current:
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp
        return prev


def printList(node):
    current = node
    while current:
        print(current.val)
        current = current.next


head = ListNode(1)
head.next = ListNode(2)
head.next = ListNode(3)
solution = Solution()
printList(solution.reverse_linked_list(head))
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
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
    def reverseBetween(self, head, m, n):

        if not head:
            return None

        current = head
        prev = ListNode(-1)
        prev.next = current
        count = 1
        while count < m:
            count +=1
            prev = current
            current = current.next
        oldHead = prev
        while count <= n:
            count +=1
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        tail = current
        oldHead
        print(current.val)


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)

solution = Solution()
# output =solution.reverseList(head)
# solution.printList(output)
solution.reverseBetween(head, 1,4)
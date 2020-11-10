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

    def isPalindrome(self, head):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow = self.reverseList(slow)
        fast = head
        while slow:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(1)

solution = Solution()
solution.isPalindrome(head)
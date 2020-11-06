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
    def plusOne(self, head):
        temp = head
        carry = 1
        head = self.reverseList(head)
        while (temp):
            temp.val += carry
            if temp.val % 10 == 0:
                # update carry for next calulation
                carry = 1
                temp.val = 0
            else:
                # update carry for next calulation
                carry = 0
            temp = temp.next

        # Reverse the modified list
        return self.reverseList(head)


solution = Solution()


head = ListNode(1)
head.next = ListNode(9)
head.next.next = ListNode(9)
head.next.next.next = ListNode(9)
rev = solution.reverseList(head)
plusOneList = solution.plusOne(head)
solution.printList(plusOneList)
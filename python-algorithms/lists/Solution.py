class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        pass

    def reverseList(self, head):

        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev

    def isPalindrome(self, head):
        slow = head
        fast = head

        while (fast != None and fast.next != None):
            fast = fast.next.next
            slow = slow.next

        slow = self.reverseList(slow)

        print("The slow list is ")
        self.printList(slow)

        print("The fast list is ")
        self.printList(fast)

        fast = head
        while slow:
            if(slow.val != fast.val):
                return False
            slow = slow.next
            fast = fast.next


        return True
    def printList(self, head):
        while(head):
            print(head.val)
            head = head.next

    # def mergeTwoLists(self, l1, l2):
    #     def merge(l1, l2):
    #         if l1 is None:
    #             return l2
    #         elif l2 is None:
    #             return l1
    #         else:
    #             if l1.val <= l2.val:
    #                 return ListNode(val = l1.val, next = merge(l1.next, l2))
    #             else:
    #                 return ListNode(val = l2.val, next = merge(l1, l2.next))
    #     return merge(l1, l2)

    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        dummy = ListNode(-1)
        head = dummy

        while(l1 and l2):
            if(l1.val < l2.val):
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next
            head.next = None
        while l1:

            head.next = l1
            l1 = l1.next
            head = head.next
            head.next = None
        while l2:
            head.next = l2
            l2 = l2.next
            head = head.next
            head.next = None
        return dummy.next

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(2)
solution = Solution()
solution.isPalindrome(head)


# head1 = ListNode(1)
# head1.next = ListNode(3)
# head1.next.next = ListNode(4)
# head1.next.next.next = ListNode(8)
#
#
# head2 = ListNode(2)
# head2.next = ListNode(5)
# head2.next.next = ListNode(7)
# solution = Solution()
# mergedHead = solution.mergeTwoLists(head1, head2)
# solution.printList(mergedHead)
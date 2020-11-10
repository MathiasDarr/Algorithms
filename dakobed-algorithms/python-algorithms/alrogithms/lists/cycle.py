class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def detectCyleTwoPointer(self, head):
        if not head or not head.next:
            return None
        slow = head
        fast = head.next

        while slow != fast:
            if not fast.next or not fast.next.next:
                return None
            slow = slow.next
            fast = fast.next.next

    def detectCycle(self, head):
        """
        Return the node at which the cycle beings with the use of a hash map
        :param head:
        :return:
        """
        node_map = set()
        while head:
            if head in node_map:
                return head
            node_map.add(head)
            head = head.next
        return None

head = ListNode(3)
second = ListNode(2)
head.next = second

second.next = ListNode(0)
second.next.next = ListNode(-4)
second.next.next.next = second

solution = Solution()
solution.detectCycle(head)


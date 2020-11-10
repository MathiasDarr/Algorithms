class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def printInOrder(self, root):
        if not root:
            return
        self.printInOrder(root.left)
        print(root.val)
        self.printInOrder(root.right)

    def sortedArrayToBST(self, nums):
        return self.sortedArrayToBSTrecursive(nums)

    def sortedArrayToBSTrecursive(self, nums):
        if len(nums) == 0:
            return None
        if len(nums) ==1:
            return TreeNode(nums[0])
        mid = len(nums)//2
        return TreeNode(nums[mid],  self.sortedArrayToBSTrecursive(nums[:mid]), self.sortedArrayToBSTrecursive(nums[mid+1:]))


    def findMiddle(self, head):

        # The pointer used to disconnect the left half from the mid node.
        prevPtr = None
        slowPtr = head
        fastPtr = head

        # Iterate until fastPr doesn't reach the end of the linked list.
        while fastPtr and fastPtr.next:
            prevPtr = slowPtr
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next

        # Handling the case when slowPtr was equal to head.
        if prevPtr:
            prevPtr.next = None

        return slowPtr
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.sortedListToBSTRecursive(head)
    def sortedListToBSTRecursive(self, head):
        if not head:
            return None
        prev = None
        slow = head
        fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Handling the case when slowPtr was equal to head.
        if prev:
            prev.next = None
        mid = slow
        node = TreeNode(mid.val)

        if head == mid:
            return node

        node.left = self.sortedListToBSTRecursive(head)
        node.right = self.sortedListToBSTRecursive(mid.next)
        return node

solution = Solution()
nums = [-10,-3,0,5,9]
# root = solution.sortedArrayToBST(nums)
# solution.printInOrder(root)


head = ListNode(-10)
head.next = ListNode(-3)
head.next.next = ListNode(0)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(9)

root = solution.sortedListToBST(head)
solution.printInOrder(root)

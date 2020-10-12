class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def printList(self, head):
        while head:
            print(head)
            head = head.next
    def findMiddle(self, head):
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

    def printInorder(self, root):
        if root:
            self.printInorder(root.left)
            print(root.val)
            self.printInorder(root.right)

    def sortedArrayToBst(self, nums):
        return self.sortedArrayToBSTrecursive(nums)

    def sortedArrayToBSTrecursive(self, nums):
        if len(nums) == 0:
            return None
        if len(nums) ==1:
            return TreeNode(nums[0])
        mid = len(nums) //2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBSTrecursive(nums[:mid])
        root.right = self.sortedArrayToBSTrecursive(nums[mid+1:])
        return root

    def sortedListToBST(self, head):



        if not head:
            return None

        print("After invocation of the list")
        self.printList(head)


        # Find the middle element for the list.
        mid = self.findMiddle(head)
        # The mid becomes the root of the BST.
        node = TreeNode(mid.val)
        # Base case when there is just one element in the linked list
        if head == mid:
            return node

        # Recursively form balanced BSTs using the left and right halves of the original list.
        node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(mid.next)
        return node


array = [-10,-3,0,5,9]
head = ListNode(-10)
head.next = ListNode(-3)
head.next.next = ListNode(0)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(9)
# head.next = ListNode(-3)

solution = Solution()
newHead = solution.sortedListToBST(head)
solution.printList(newHead)

# root = solution.sortedArrayToBst(head)
# solution.printInorder(root)

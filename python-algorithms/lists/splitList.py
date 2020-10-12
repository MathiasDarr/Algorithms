class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def printList(self, node):
        while node:
            print(node.val)
            node = node.next
    def splitListToParts(self, root, k):
        current = root
        count = 0
        while current:
            current = current.next
            count+=1
        smallK, remainder = divmod(count, k)
        bigK = smallK if remainder ==0 else smallK+1

        current = root
        completed = 0
        results = []

        while completed <k:
            count1 = 0
            newRoot = ListNode(-1)
            newHead = newRoot
            while count1 < (bigK if completed < remainder else smallK):
                # print(current.val)
                newRoot.next = ListNode(current.val)
                newRoot = newRoot.next

                current = current.next
                count1 +=1
            results.append(newHead.next)
            completed +=1
        return results

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(7)
head.next.next.next.next.next.next.next = ListNode(8)
head.next.next.next.next.next.next.next.next = ListNode(9)
head.next.next.next.next.next.next.next.next.next = ListNode(10)

solution = Solution()
lists = solution.splitListToParts(head, 3)
l1 = lists[0]
solution.printList(l1)
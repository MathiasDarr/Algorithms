import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def printList(self, head):
        while head:
            print(head.val)
            head = head.next

    def mergeKLists(self, lists):
        heap = []
        i = 0
        for l in lists:
            if l:
                heapq.heappush(heap, (l.val, i, l))
                i +=1

        head = ListNode(-1)
        current = head
        while len(heap) > 0:
            _, currentIndex, currentNode  = heapq.heappop(heap)
            current.next = ListNode(currentNode.val)
            current = current.next
            if currentNode.next:
                heapq.heappush(heap, (currentNode.next.val, currentIndex, currentNode.next))
        return head.next

    # def mergeKLists(self, lists):
    #
    #     newList = ListNode(-1)
    #     current = newList
    #
    #     for i in range(len(lists)-1, -1, -1):
    #         if not lists[i]:
    #             del lists[i]
    #
    #     while len(lists) > 0:
    #         minListIndex = -1
    #         minValue = float('inf')
    #         for i in range(len(lists)):
    #             if lists[i].val < minValue:
    #                 minValue = lists[i].val
    #                 minListIndex = i
    #
    #         current.next = ListNode(lists[minListIndex].val)
    #         current = current.next
    #         lists[minListIndex] = lists[minListIndex].next
    #         if not lists[minListIndex]:
    #             del lists[minListIndex]
    #     return newList.next


head1 = ListNode(1)
head1.next = ListNode(4)
head1.next.next = ListNode(5)

head2 = ListNode(1)
head2.next = ListNode(3)
head2.next.next= ListNode(4)

head3 = ListNode(2)
head3.next = ListNode(6)



lists = [head1,head2, head3]
solution = Solution()
newHead= solution.mergeKLists(lists)
solution.printList(newHead)
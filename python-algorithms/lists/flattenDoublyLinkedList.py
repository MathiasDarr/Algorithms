class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def printForward(self, head):
        while head:
            print(head.val)
            head = head.next
    def printBackwards(self, head):
        prev = None
        while head:
            prev = head
            head = head.next
        print('prev val: {}'.format(prev.val))
        while prev:
            print(prev.val)
            prev = prev.prev

    def flatten(self, head):
        stack = []
        cur = head
        root = head

        while stack or cur:
            if cur.child:
                if cur.next:
                    stack.append(cur.next)
                new = cur.child
                new.prev = cur
                cur.child = None
                cur.next = cur = new
            elif not cur.next and stack:
                cur.next = stack.pop()
                cur.next.prev = cur
                cur = cur.next
            else:
                cur = cur.next
        return root
    # def flatten(self, head):

    #     node = head
    #     while node:
    #         if node.child:
    #             nextNode = node.next
    #             node.child.prev = node
    #             node.next = node.child



    # def flatten(self, head):
    #     def recursive(node):
    #         prev = None
    #     if not head:
    #         return head
    #     recursive(head)

    # def flatten(self, head):
    #     current = head
    #     outHead = Node(-1, None, None, None)
    #     output = outHead
    #     prev = None
    #     stack = []
    #     while current or len(stack) > 0:
    #         if not current:
    #             current = stack.pop()
    #
    #         output.next = Node(current.val, prev, None, None)
    #
    #         output = output.next
    #         print('created node with output: {} and previous val: {}'.format(current.val, prev.val if prev else None))
    #
    #         prev = current
    #         if current.child:
    #             if current.next:
    #                 stack.append(current.next)
    #             current = current.child
    #         else:
    #             # prev = current
    #             current = current.next
    #
    #     return outHead.next

# child2 = Node(11, None, None, None)
# child2.next = Node(12, child2, None, None)
#
# child1 = Node(7, None, None, None)
# child1.next = Node(8, child1, None, child2)
# child1.next.next = Node(9, child1.next, None, None  )
# child1.next.next.next = Node(10, child1.next.next, None, None  )
#
#
# head = Node(1, None, None, None)
# head.next = Node(2, head, None, None)
# head.next.next = Node(3, head.next, None, child1)
# head.next.next.next = Node(4, head.next.next, None, None)
# head.next.next.next.next = Node(5, head.next.next.next, None, None)
# head.next.next.next.next.next = Node(6, head.next.next.next.next, None, None)

child1 = Node(4, None, None, None)
child1.next = Node(5, child1, None, None)

head = Node(1, None, None, None)
head.next = Node(2, head, None, child1)
head.next.next = Node(3, head.next, None, None)


solution = Solution()
# solution.printForward(head)
output = solution.flatten(head)
print('forward')
solution.printForward(output)

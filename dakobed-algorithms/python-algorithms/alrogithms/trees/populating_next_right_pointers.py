"""
We are given a perfect tree where all leaves are on the same level, every parent has two children

Populate the next pointers for each node to point to the node to the right of them.

Recursive:
    Per

Iterative:
    Iterate through the tree until the left child is empty



LeetCode 117 Populating Next Right Pointers In Each Node II
    Instead of a perfect tree in which every non leaf node has two children, nodes in this tree may only have a single
    child node, meaning that we can't set the next pointers on the children directly as we don't have access to the left
    and right nodes at that time.  Instead




"""



class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    # @param root, a tree link node
    # @return nothing

    # def connect(self, root):
    #     def trav(node):
    #         if not node.left and not node.right:
    #             return
    #         if not node.next:
    #             node.left.next = node.right
    #             node.right.next = None
    #         else:
    #             node.left.next = node.right
    #             node.right.next = node.next.left
    #         trav(node.left)
    #         trav(node.right)
    #     if not root:
    #         return
    #     root.next = None
    #     trav(root)

    def recursive_connect(self, root):
        def traverse(node):
            if not node.left and not node.right:
                return
            if not node.next:
                node.left.next = node.right
                node.right.next = None
            else:
                node.left.next = node.right
                node.right.next = node.next.left
            traverse(node.left)
            traverse(node.right)
        if not root:
            return
        traverse(root)
        return root



    def my_iterative_connect(self, root):
        if not root:
            return
        queue = [root]
        while queue:
            level = []
            newqueue = []
            while queue:
                node = queue.pop(0)
                level.append(node)
                if node.left:
                    newqueue.append(node.left)
                if node.right:
                    newqueue.append(node.right)
            for i, node in enumerate(level[:-1]):
                node.next = level[i + 1]
            queue = newqueue
        return root



        # if not root:
        #     return
        # queue = [root]
        # while queue:
        #     level = []
        #     newqueue = []
        #     while queue:
        #         node = queue.pop(0)
        #         level.append(node)
        #         if node.left:
        #             newqueue.append(node.left)
        #         if node.right:
        #             newqueue.append(node.right)
        #     for i, node in enumerate(level[:-1]):
        #         node.next = level[i + 1]
        #     queue = newqueue
        # return root

    def iterative_connect(self, root):
        if not root:
            return
        root.next = None
        trav = root
        while trav.left:
            head = trav.left
            while trav:
                if not trav.next:
                    trav.left.next = trav.right
                    trav.right.next = None
                    trav = head
                    break
                else:
                    trav.left.next = trav.right
                    trav.right.next = trav.next.left
                    trav = trav.next





    # if not root:
    #     return
    #
    # stack = [root]
    #
    # while stack:
    #     size = len(stack)
    #     for i in range(size):
    #         node = stack.pop(0)
    #         if i < size - 1:
    #             node.next = stack[0]
    #         else:
    #             node.next = None
    #
    #         if node.left: stack.append(node.left)
    #         if node.right: stack.append(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

solution = Solution()
levels = solution.connect(root)
level = levels[-1]

for i, node in enumerate(level[:-1]):
    node.next = level[i+1]
    print(node.val)
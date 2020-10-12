class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTreeRecursive(self, p,q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTreeRecursive(p.left, q.left) and self.isSameTreeRecursive(p.right, q.right)

    def isSameTree(self, p, q):
        pqueue = [p]
        qqueue = [q]

        while pqueue and qqueue:
            pnode = pqueue.pop()
            qnode = qqueue.pop()
            if pnode.val != qnode.val:
                return False
            if pnode.left and qnode.left:
                pqueue.append(pnode.left)
                qqueue.append(qnode.left)
            elif pnode.left or qnode.left:
                return False
            if pnode.right and qnode.right:
                pqueue.append(pnode.right)
                qqueue.append(qnode.right)
            elif pnode.right or qnode.right:
                return False
        return True


q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)
q.right.right = TreeNode(2)


p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)
p.right.right = TreeNode(2)

solution = Solution()
solution.isSameTree(p,q)
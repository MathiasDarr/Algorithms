class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def printinOrder(self, root):
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            print(node.val)
            dfs(node.right)
        dfs(root)

    def serialize(self, root):
        def preorder(node):
            if not node:
                return '#'
            left = preorder(node.left)
            right = preorder(node.right)
            return '{},{},{}'.format(str(node.val), left, right)
        return preorder(root)

    def deserialize(self, data):
        def dfs():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        vals = iter(data.split(','))
        return dfs()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
solution = Codec()
btString = solution.serialize(root)
newRoot = solution.deserialize(btString)
solution.printinOrder(newRoot)


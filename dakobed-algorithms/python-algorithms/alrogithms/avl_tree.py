"""
Implementation of an AVL Tree , self balancing BST

Balance Factor: defines the direction the tree is more heavily leaning towards
bf(node) = height(node.left)-height(node.right)




"""


class AVLTreeNode:
    def __init__(self, key, val = None, bf=0):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.bf = bf ## Balance factor
        self.height =


class AVLTree:
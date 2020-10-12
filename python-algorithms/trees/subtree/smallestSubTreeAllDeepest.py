class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delete_dupliate_list_elements(self, dlist):
        delete_indices = set()
        i = 0
        while i < len(dlist) - 1:
            if dlist[i].val == dlist[i + 1].val:
                delete_indices.add(i)
                i += 2
            else:
                i += 1

        for i in range(len(dlist) - 1, -1, -1):
            if i in delete_indices:
                del dlist[i]

    def subtreeWithAllDeepest(self, root):
        if not root:
            return
        stack = [(root, 0, None)]
        parentMap = {root: None}
        dlist = []
        maxDepth = 0
        while stack:
            node, depth, parent = stack.pop(0)
            parentMap[node] = parent
            if depth > maxDepth:
                dlist = []
                dlist.append(node)
                maxDepth = depth
            elif depth == maxDepth:
                dlist.append(node)
            if node.left:
                stack.append((node.left, depth+1, node))
            if node.right:
                stack.append((node.right, depth+1, node))

        while len(dlist) > 0:
            self.delete_dupliate_list_elements(dlist)
            if len(dlist) ==1:
                return dlist[0]
            newList = [parentMap[node] for node in dlist]
            dlist = newList
        return dlist[0]
        #
        # while not all(elem.val == maxDepthList[0] for elem in maxDepthList):
        #     maxDepthList = [parentMap[node] for node in maxDepthList ]
        # return maxDepthList

        # depth = {None: -1}
        # def dfs(node, parent = None):
        #     if node:
        #         depth[node] = depth[parent] +1
        #         dfs(node.left, node)
        #         dfs(node.right, node)
        # dfs(root)
        # return [ node.val for node, nodeDepth in depth.items() if nodeDepth==max(depth.values()) ]



root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.left.left = TreeNode(8)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

solution = Solution()
dlist = solution.subtreeWithAllDeepest(root)


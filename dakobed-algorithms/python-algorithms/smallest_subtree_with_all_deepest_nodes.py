"""
To find the subtree with all of the deepest nodes,
    1) Perform level order traversal, after each iteration having the deepest nodes encountered
        - Maintain a map with nodes pointing to their parent node.


    Remove all duplicates from a list.  No need for anythin fancy.  Just convert to a hashmap & then back to a list!


"""



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right






class Solution:
    def print_in_order(self, root):
        if not root:
            return
        self.print_in_order(root.left)
        print(root.val)
        self.print_in_order(root.right)

    def remove_duplicate_nodes_from_list(self, nodes_list):
        """
        Remove

        :param nodes_list:
        :return:
        """
        nodes_list = list({node: 0 for node in nodes_list})
        return nodes_list


    def subtreeWithAllDeepest(self, root):
        if not root:
            return None

        parent_map = {root: None}
        queue = [(root, None)]

        while queue:
            new_queue =[]
            level = []
            while queue:
                node, parent = queue.pop(0)
                parent_map[node] = parent
                level.append(node)
                if node.left:
                    new_queue.append((node.left, node))
                if node.right:
                    new_queue.append((node.right, node))
            queue = new_queue

        ### Once this loop terminates we have the deepest nodes in a list

        nodes_list = level
        while len(nodes_list) > 1:
            parent_nodes_list = [parent_map[node] for node in nodes_list]
            nodes_list = self.remove_duplicate_nodes_from_list(parent_nodes_list)
        return nodes_list[0]

solution = Solution()
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.right.right = TreeNode(8)
root.right.left = TreeNode(0)

root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

subTree = solution.subtreeWithAllDeepest(root)
solution.print_in_order(subTree)
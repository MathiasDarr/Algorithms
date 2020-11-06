package trees.depth;

import trees.TreeNode;

public class MaximumDepth {
    public static void main(String[] args) {
        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(9);
        root.right = new TreeNode(20);
        root.right.right = new TreeNode(7);
        root.right.left = new TreeNode(15);
        Solution solution = new Solution();
        System.out.println("THE MAXIMUM DEPTH OF THE TREE IS " +solution.maxDepth(root));

    }


}

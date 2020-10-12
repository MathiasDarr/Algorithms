package org.mddarr.trees;

public class Invert {
    public static void main(String[] args){
        TreeNode root = new TreeNode(4);
        root.left = new TreeNode(2);
        root.right = new TreeNode(7);
        Solution solution = new Solution();
        root = solution.invertTree(root);
        solution.printPreOrder(root);
    }
}

package org.mddarr.trees;

public class isValidTree {
    public static void main(String[] args){

        Solution solution = new Solution();
        TreeNode root = new TreeNode(5);
        root.left = new TreeNode(3);
        root.left.right = new TreeNode(4);
        System.out.println("The tree is a valid BST " + solution.isValidBST(root));
    }
}

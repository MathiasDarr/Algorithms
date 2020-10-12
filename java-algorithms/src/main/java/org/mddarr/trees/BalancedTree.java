package org.mddarr.trees;



public class BalancedTree {
    public static void main(String[] args){
        Solution solution = new Solution();
        TreeNode treeNode = new TreeNode(3);
        treeNode.left = new TreeNode(9);
        treeNode.right = new TreeNode(20);
        treeNode.right.right = new TreeNode(7);
        treeNode.right.left = new TreeNode(16);

        treeNode.right.left.right = new TreeNode(16);
        System.out.println("The tree is balanced " + solution.isBalanced(treeNode));
    }
}

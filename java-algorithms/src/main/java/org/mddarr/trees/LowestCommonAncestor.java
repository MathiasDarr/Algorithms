package org.mddarr.trees;

public class LowestCommonAncestor {
    public static void main(String[] args) {


        TreeNode root = new TreeNode(3);
        root.left = new TreeNode(5);
        root.right = new TreeNode(1);
        root.left.left = new TreeNode(6);
        root.left.right = new TreeNode(2);
        root.left.right.left = new TreeNode(7);
        root.left.right.right = new TreeNode(4);
        root.right.right = new TreeNode(8);
        root.right.left = new TreeNode(0);

        TreeNode p = root.left.left;
        TreeNode q = root.left.right.right;

        Solution solution = new Solution();
        TreeNode lca = solution.lowestCommonAncestorBinaryTree(root, p, q);
        System.out.println("The lowest common ancestor of p & q is " + lca.val );

    }

}



//        TreeNode root = new TreeNode(1);
//        root.left = new TreeNode(2);
//        root.right = new TreeNode(3);
//        root.left.left = new TreeNode(4);
//        root.left.right = new TreeNode(5);
//        root.right.left = new TreeNode(6);
//        root.right.right = new TreeNode(7);
//        root.left.left.left = new TreeNode(8);
//        root.left.left.right = new TreeNode(9);
//
//        root.left.right.left = new TreeNode(10);
//        root.left.right.right = new TreeNode(11);
//
//        root.right.left.left = new TreeNode(12);
//        root.right.left.right = new TreeNode(13);
//
//        root.right.right.left = new TreeNode(14);
//        root.right.right.right = new TreeNode(15);

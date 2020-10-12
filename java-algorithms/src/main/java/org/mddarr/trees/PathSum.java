package org.mddarr.trees;

import java.util.List;

public class PathSum {
    public static void main(String[] args){
        TreeNode root = new TreeNode(5);
        root.left = new TreeNode(8);
        root.right = new TreeNode(8);
        Solution solution = new Solution();
        int target = 13;

        List<List<Integer>> results = solution.pathSumII(root, target);
        System.out.println("There is a path from root to leaf with sum of " + results );
    }

}

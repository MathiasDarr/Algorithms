package trees;

import com.sun.source.tree.Tree;

public class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if(p == null  && q == null){
            return true;
        }else if(p==null | q == null){
            return false;
        }else if(p.val != q.val){
            return false;
        }else{
            return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
        }
    }

    public boolean hasPathSum(TreeNode root, int sum) {
        return hasPathSumDFS(root, 0, sum);
    }
    private boolean hasPathSumDFS(TreeNode node, int currentSum, int sum) {
        if(node == null)
            return false;
        if(node.left == null && node.right == null && node.val + currentSum == sum) {
            return true;
        }
        return hasPathSumDFS(node.left, currentSum + node.val, sum) | hasPathSumDFS(node.right, currentSum + node.val, sum);

    }

}



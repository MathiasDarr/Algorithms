package trees.depth;

import trees.TreeNode;

public class Solution {
    public int maxDepth(TreeNode root) {
        return maximumDepth(root, 0);
    }
    public int maximumDepth(TreeNode node, int depth){
        if(node == null)
            return depth;
        int ldepth = maximumDepth(node.left, depth+1);
        int rdepth = maximumDepth(node.right, depth+1);
        return Math.max(ldepth, rdepth);

    }

}

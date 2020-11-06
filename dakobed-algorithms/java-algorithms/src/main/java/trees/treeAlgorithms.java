package trees;

public class treeAlgorithms {
    public static void main(String[] args) {
        TreeNode root1 = new TreeNode(1);
        root1.left = new TreeNode(2);
        root1.right = new TreeNode(3);

        TreeNode root2 = new TreeNode(1);
        root2.left = new TreeNode(2);
        root2.right = new TreeNode(3);
        Solution solution = new Solution();
        System.out.println("The two trees are the same " + solution.isSameTree(root1, root2));

    }

}

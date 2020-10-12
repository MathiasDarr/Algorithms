package org.mddarr.trees;


import java.util.*;

public class Solution {
    int sum ;

    public boolean isSameTree(TreeNode p, TreeNode q){
        if( p ==null && q == null)
            return true;
        if(q == null || p == null)
            return false;
        if(p.val != q.val)
            return false;
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }

    public boolean check(TreeNode q, TreeNode p){
        if(q == null && p == null)
            return true;
        if(q == null || p == null )
            return false;
        if(q.val != p.val)
            return false;
        return true;
    }

    public boolean isSameTreeIterative(TreeNode p, TreeNode q){
        if( p ==null && q == null)
            return true;
        if(q == null || p == null)
            return false;
        Queue<TreeNode[]> node_queue = new ArrayDeque<>();
        TreeNode[] nodes = {p,q};
        node_queue.add(nodes);

        while(node_queue.size() != 0){
            TreeNode[] nodeArray = node_queue.remove();
            if(!check(nodeArray[0], nodeArray[1])){
                return false;
            }
            TreeNode[] leftNodes = {nodeArray[0].left, nodeArray[1].left };
            TreeNode[] righttNodes = {nodeArray[0].right, nodeArray[1].right };
            node_queue.add(leftNodes);
            node_queue.add(righttNodes);
        }

        return true;
    }


    public TreeNode mergeTrees(TreeNode t1, TreeNode t2){
        if (t1 == null)
            return t2;
        if (t2 == null)
            return t1;
        t1.val += t2.val;
        t1.left = mergeTrees(t1.left, t2.left);
        t1.right = mergeTrees(t1.right, t2.right);
        return t1;
    }

    public TreeNode mergeTreesIterative(TreeNode t1, TreeNode t2){
        if(t1 == null)
            return t2;
        Stack<TreeNode[]> stack = new Stack<>();
        stack.push(new TreeNode[]{t1, t2});
        while(!stack.isEmpty()){
            TreeNode[] t = stack.pop();
            if(t[0] == null || t[1] == null){
                continue;
            }
            t[0].val += t[1].val;
            if(t[0].left == null){
                t[0].left = t[1].left;
            }else{
                stack.push(new TreeNode[] {t[0].left, t[1].left});
            }
            if(t[0].right == null){
                t[0].right = t[1].right;
            }else{
                stack.push(new TreeNode[] {t[0], t[1].right });
            }
        }
        return t1;
    }

    public int sumOfLeftLeaves(TreeNode root){
        sum = 0;
        if(root == null){
            return 0;
        }
        findSum(root, -1);
        return sum;
    }

    public void findSum(TreeNode root, int direction){
        if(root == null){
            return;
        }
        if(root.left == null && root.right == null){
            if(direction ==0){
                sum += root.val;
            }
        }
        findSum(root.left, 0);
        findSum(root.right, 1);
    }

    public void printTree(TreeNode root){
        if(root == null)
            return;
        printTree(root.left);
        System.out.println(root.val);
        printTree(root.right);
    }

    public void printPreOrder(TreeNode root){
        if(root == null)
            return;
        System.out.println(root.val);
        printTree(root.left);
        printTree(root.right);
    }

    public boolean isValidBST(TreeNode root){
        boolean isvalid = isValidBstDFS(root, root.val, root.val);
        return isvalid;
    }

    public boolean isValidBstDFS(TreeNode root, int max, int min){
        if(root == null){
            return true;
        }
        System.out.println("I get called with val " + max + " and the current value is " + root.val);
        if(root.val < min || root.val > max ) {
            System.out.println("I fuck up called with val " + max + " and the current value is " + root.val);
            return false;
        }else{
            return isValidBstDFS(root.left, min, root.val ) && isValidBstDFS(root.right, root.val,max); }
    }

    public boolean pathSum(TreeNode root, int target){
        return pathSumRecursive(root, target);
    }
    public boolean pathSumRecursive(TreeNode root, int target) {
        if(root == null)
            return false;
        if(root.left == null && root.right == null && root.val - target ==0)
            return true;
        return pathSumRecursive(root.left, target-root.val) || pathSumRecursive(root.right, target-root.val);
    }


    public List<List<Integer>> pathSumII(TreeNode root, int target){
        List<List<Integer>> paths = new ArrayList<>();
        findPaths(root, target , new ArrayList<Integer>(), paths);
        return paths;
    }
    public void findPaths(TreeNode root, int target, List<Integer> current, List<List<Integer>> paths){
        if(root ==null)
            return;
        current.add(root.val);
        if(root.left ==null && root.right == null && target ==root.val)
            paths.add(current);
        findPaths(root.left, target-root.val, new ArrayList<Integer>(current), paths);
        findPaths(root.right, target-root.val, new ArrayList<Integer>(current), paths);
    }

    int min_depth = 0;
    public boolean isBalanced(TreeNode root){

        return checkBalanced(root, 0);



    }
    public boolean checkBalanced(TreeNode root, int depth){


        return true;

    }

    public TreeNode invertTree(TreeNode root){
        if (root == null) {
            return null;
        }
        TreeNode right = invertTree(root.right);
        TreeNode left = invertTree(root.left);
        root.left = right;
        root.right = left;
        return root;
    }

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        int rval = root.val;
        int pval = p.val;
        int qval = q.val;

        if(pval > rval && qval > rval)
            return lowestCommonAncestor(root.right, p,q);
        if(pval < rval && qval < rval)
            return lowestCommonAncestor(root.left, p, q);
        else
            return root;
    }


    public TreeNode lowestCommonAncestorBinaryTree(TreeNode root, TreeNode p, TreeNode q) {
        Deque<TreeNode> stack = new ArrayDeque<>();
        Map<TreeNode, TreeNode> parentMap = new HashMap<>();
        parentMap.put(root, null);
        stack.push(root);

        // Iterate until we find both the nodes p & q
        while(!parentMap.containsKey(p) || !parentMap.containsKey(q)){
            TreeNode node = stack.pop();
            if(node.left != null){
                parentMap.put(node.left, node);
                stack.push(node.left);
            }
            if(node.right != null){
                parentMap.put(node.right, node);
                stack.push(node.right);
            }
        }

        // Ancestors set for node p

        Set<TreeNode> ancestors = new HashSet<>();
        // Process all ancestors for node p using parent pointers

        while(p != null){
            ancestors.add(p);
            p = parentMap.get(p);
        }

        while(!ancestors.contains(q))
            q = parentMap.get(q);

        return q;
    }



    //    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
//        int pval = p.val;
//        int qval = q.val;
//        if(pval > qval){
//            int temp = pval;
//            pval = qval;
//            qval = temp;
//        }
//
//        TreeNode lca = new TreeNode(lcaRecursive(root, pval, qval));
//
//        return root;
//    }
//
//    public int lcaRecursive(TreeNode root, int pval, int qval){
//        if(root.val < qval && root.val > pval){
//            return root.val;
//        }
//        if(root.val < pval){
//            return lcaRecursive(root.right, pval, qval);
//        }else if(root.val > qval){
//            return lcaRecursive(root.left, pval, qval);
//        }
//        return -1;
//    }




}

package org.mddarr.dynamicprogramming;

public class DpProblems {

    public static void main(String[] args){
        int[] houses = {1,2,3,1};

        Solution solution = new Solution();
        int nsteps = solution.climbStairs(3);
        System.out.println("The number of steps is "+ nsteps);

    }


}

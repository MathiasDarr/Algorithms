package org.mddarr.subarrays;

public class SubarryProblems {
    public static void main(String[] args){
        Solution solution = new Solution();

        int[] nums = {2,3,-2,4};
        int maxs = solution.maxProduct(nums);
        System.out.println("The subarray with maximum contiguous product has product of " + maxs);
    }

}

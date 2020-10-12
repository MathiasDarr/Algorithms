package org.mddarr.arrays;

public class Intersection {
    public static void main(String[] args){
        int[] nums = {1,2,2,1};
        int[] nums2 = {2,2};
        Solution solution = new Solution();
        int[] inter = solution.intersection(nums, nums2);
        int[] inter2 = solution.intersectII(nums, nums2);
//        for(int num: inter){
//            System.out.println(num);
//        }
        for(int num: inter2){
            System.out.println(num);
        }

    }

}

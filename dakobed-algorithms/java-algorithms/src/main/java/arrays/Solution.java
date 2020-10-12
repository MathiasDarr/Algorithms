package arrays;

public class Solution {
    public int maxSubArray(int[] nums){
        int currentMax=nums[0];
        int maxEndingHere=nums[0];
        for (int i=1;i<nums.length;++i){
            maxEndingHere= Math.max(maxEndingHere+nums[i], nums[i]);
            currentMax=Math.max(currentMax, maxEndingHere);
        }
        return currentMax;

    }
}

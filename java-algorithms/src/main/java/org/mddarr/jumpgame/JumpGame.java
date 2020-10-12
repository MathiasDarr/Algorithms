package org.mddarr.jumpgame;

public class JumpGame {

    public static boolean canJump(int[] nums){
        int lastPost = nums.length -1;
        for(int j = nums.length-1; j>=0;j--){
            if(nums[j] + j >= lastPost){
                lastPost = j;
            }
        }
        return lastPost ==0;
    }

//    public static boolean canJumpFromPosition(int position, int[] nums){
//        if(position == nums.length -1)
//            return true;
//        int furthestJump = Math.min(position + nums[position], nums.length -1);
//        for(int nextPosition = position+1; nextPosition <= furthestJump; nextPosition++){
//            if(canJumpFromPosition(nextPosition, nums)){
//                return true;
//            }
//        }
//        return false;
//    }
//
//    public static boolean canJump(int[] nums){
//        return canJumpFromPosition(0, nums);
//    }
    public static void main(String[] args){
        int[] nums = {3,2,1,1,4};
        System.out.println("I can make the jump " + canJump(nums));
    }

}

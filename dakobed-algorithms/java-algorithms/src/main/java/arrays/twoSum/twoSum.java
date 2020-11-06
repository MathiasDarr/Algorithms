package arrays.twoSum;

public class twoSum {
    public static void main(String[] args) {
        int[] nums = {2,7,11,15};
        int target = 9;
        Solution solution = new Solution();
        int[] indices = solution.twoSum(nums, target);
        for(int num: indices){
            System.out.println(num);
        }
    }
}

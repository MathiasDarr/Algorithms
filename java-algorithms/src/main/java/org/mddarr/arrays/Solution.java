package org.mddarr.arrays;

import java.util.*;

public class Solution {
    List<List<Integer>> output = new ArrayList<>();

    public int[] topKFrequent(int[] nums, int k) {

        if(k == nums.length){
            return nums;
        }

        Map<Integer, Integer> counts = new HashMap<>();
        for(int n:nums){
            counts.put(k, counts.getOrDefault(n, 0)+1);
        }

        Queue<Integer> heap = new PriorityQueue<>(
        (n1,n2) -> counts.get(n1) - counts.get(n2));
        return new int[] {1};
    }



    public int findMin(int[] nums){
        System.out.println(nums.toString());
        for(int n: nums){
            System.out.println(n);
        }
        if(nums.length == 0) {
            System.out.println("Why");
            return -1;
        }
        if(nums[0] < nums[nums.length-1]) {
            System.out.println("Why");
            return nums[0];
        }
        int left = 0;
        int right = nums.length -1;
        while(right>= left){
            int leftv = nums[left];
            int rightv = nums[right];
            System.out.println("I get called");
            while(nums[left+1]==leftv )
                if(left+1== nums.length-1)
                    return nums[left];
                left++;
            while(right-1 > 0 && nums[right-1]==rightv )
                right--;
            int mid = left +(right-left)/2;
            if(nums[mid] < nums[mid-1]){
                System.out.println(Arrays.toString(nums));
                return nums[mid];
            }
            else if(nums[mid] > nums[mid+1]) {
                System.out.println(nums);
                return nums[mid + 1];
            }if(nums[left] > nums[mid]) {
                System.out.println(nums);
                right = mid - 1;
            }
            else{
                left = mid+1;
            }
        }
        return -1;
    }


    public boolean canJump(int[] nums) {
        if(nums.length == 0){
            return true;
        }
        Stack<int[]> jumpstack = new Stack<>();
        Set<Integer> seen = new HashSet<>();
        int n = nums.length;
        int[] firstjump = {nums[0],0};
        jumpstack.add(firstjump);
        while(!jumpstack.isEmpty()){
            int[] current_jump = jumpstack.pop();
            int jumpvalue = current_jump[0];
            int jumpindex = current_jump[1];
            if(!seen.contains(jumpindex)){
                if(jumpindex + jumpvalue >n)
                    return true;
                for(int i =1; i<= jumpvalue; i++){
                    int[] nextjump = {nums[i], i + jumpindex};
                    jumpstack.add(nextjump);
                }
            }
            seen.add(jumpindex);
        }
        return false;
    }



    public int minPathSum(int[][] grid){
        if(grid == null || grid.length ==0){
            return 0;
        }

        int[][] dp = new int[grid.length][grid[0].length];
        for(int i=0; i < dp.length; i++){
            for(int j =0; j < dp[i].length; j++){
                dp[i][j] += grid[i][j];
                if(i > 0 && j > 0){
                    dp[i][j] += Math.min(dp[i-1][j], dp[i][j-1]);
                }else if(i >0){
                    dp[i][j] += dp[i-1][j];
                }else if(j > 0){
                    dp[i][j] += dp[i][j-1];
                }
            }
        }
        return dp[dp.length-1][dp[0].length-1];
    }


    public int uniquePaths(int m, int n){
        int[][] dp = new int[m][n];
        for(int i =0; i < dp.length; i++){
            dp[i][0] = 1;
        }
        for(int i =0; i< dp[0].length; i++){
            dp[0][i] = 1;
        }

        for(int i =1; i < dp.length; i++){
            for(int j=1; j < dp[0].length; j++){
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        return dp[dp.length-1][dp[0].length-1];
    }

//    public List<List<Integer>> subsets(int[] nums){
//        int n = nums.length;
//        return output;
//    }
//    public void backtrack(int index, int[] nums, ArrayList<Integer> current){
//        if(index == nums.length){
//            return;
//        }
//        backtrack(index+1, nums, results);
//
//
//    }

    public int uniquePaths2(int[][] obstacleGrid) {
        int[][] dp = new int[obstacleGrid.length][obstacleGrid[0].length];

        dp[0][0] = 1;
        if(obstacleGrid[0][0] ==1)
            return 0;
        for (int i = 1; i < obstacleGrid.length; i++) {
            dp[i][0] = (obstacleGrid[i][0] == 0 && dp[i-1][0] == 1) ? 1 : 0;
        }
        for (int i = 1; i < obstacleGrid[0].length; i++) {
            dp[0][i] = (obstacleGrid[0][i] == 0 && obstacleGrid[0][i - 1] == 1) ? 1 : 0;
        }

        for(int i =0; i < obstacleGrid.length; i++){
            for(int j=0; j < obstacleGrid[0].length; j++){
                System.out.println(dp[i][j]);
            }
        }


        for (int i = 1; i < obstacleGrid.length; i++) {
            for (int j = 1; j < obstacleGrid[0].length; j++) {
                System.out.println(" i + " + i + " j " + j);
//                if(obstacleGrid[i][j] != 1){
//                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
//                }
//                if (obstacleGrid[i][j] == 1) {
//                    dp[i][j] = 0;
//                }
//                else if(dp[i-1][j] == 0){
//                    dp[i][j] = dp[i][j-1];
//                }
//                else if(dp[i][j-1] == 0){
//                    dp[i][j-1] = dp[i-1][j];
//                }
//                else{
//                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
//                }
            }
        }
        for(int i =0; i < obstacleGrid.length; i++){
            for(int j=0; j < obstacleGrid[0].length; j++){
                System.out.println(dp[i][j]);
            }
        }
        return dp[obstacleGrid.length-1][obstacleGrid[0].length-1];
    }


    public int smallestDistancePair(int[] nums, int k){
        Arrays.sort(nums);
        int WIDTH = 2* nums[nums.length -1];
        int[] multiplicity = new int[nums.length];
        for(int i =1; i < nums.length; ++i){
            
        }
        return 2;
    }

    public int majorityElement(int[] nums){
        int n2 = nums.length/2;
        HashMap<Integer, Integer> counts= new HashMap<>();
        for (int value : nums) {
            if (counts.containsKey(value)) {
                counts.put(value, counts.get(value) + 1);
            } else {
                counts.put(value, 1);
            }
            if (counts.get(value) > n2) {
                return value;
            }
        }
        return -1;
    }

    public int[] intersection(int[] nums1, int[] nums2){
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();

        for(int num: nums1){
            set1.add(num);
        }
        for(int num: nums2){
            set2.add(num);
        }
        Set<Integer> intersectionSet= new HashSet<>();
        for(int num:nums1){
            if(set2.contains(num)){
                intersectionSet.add(num);
            }
        }
        int[] intersectionArray = new int[intersectionSet.size()];
        int count = 0;
        for(int num: intersectionSet){
            intersectionArray[count] = num;
            count++;
        }
        System.out.println();
        return intersectionArray;
    }

    public int[] intersectII(int[] nums1, int[] nums2){
        HashMap<Integer, Integer> map1 = new HashMap<>();
        HashMap<Integer, Integer> map2 = new HashMap<>();

        for(int num: nums1){
            if(map1.containsKey(num)){
                map1.put(num, map1.get(num)+1);
            }else{
                map1.put(num, 1);
            }
        }
        for(int num: nums2){
            if(map2.containsKey(num)){
                map2.put(num, map2.get(num)+1);
            }else{
                map2.put(num, 1);
            }
        }
        HashMap<Integer, Integer> outputmap = new HashMap<>();
        int count = 0;
        for(int num: map1.keySet()){
            if(map2.containsKey(num)){
                outputmap.put(num, Math.min(map1.get(num),map2.get(num)));
                count += Math.min(map1.get(num),map2.get(num));
            }
        }
        int[] outputarray = new int[count];
        int current_count = 0;


        for(int num: outputmap.keySet()){
           int n = outputmap.get(num);


           for(int i = current_count; i < current_count+n; i++){
                outputarray[i] = num;
           }
           current_count += n;
        }

        return outputarray;
    }

}


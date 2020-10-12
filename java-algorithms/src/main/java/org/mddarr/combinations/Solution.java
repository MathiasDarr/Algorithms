package org.mddarr.combinations;

import java.util.*;

public class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target){
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(candidates);
        findCombinations(candidates, 0, target, new ArrayList<Integer>(), result);
        return result;
    }
    private void findCombinations(int[] candidates, int index, int target,List<Integer> current,  List<List<Integer>> result){
        if(target == 0){
            result.add(current);
            return;
        }
        if(target<0)
            return;
        for(int i = index; i< candidates.length; i++){
            current.add(candidates[i]);
            findCombinations(candidates, index+1, target-candidates[i], current, result);

        }
    }

    public int[] twoSum(int[] nums, int target){
        Map<Integer, Integer> map = new HashMap<>();
        for(int i =0; i < nums.length; i++){
            map.put(nums[i], i);
        }
        for(int i =0; i< nums.length; i++){
            int complement = target - nums[i];
            if(map.containsKey(complement) && map.get(complement) != i){
                return new int[] {i, map.get(complement)};
            }
        }
        throw new IllegalArgumentException("no two sum solution");
    }




}

//
// Created by mddarr on 10/13/20.
//

#include "Solution.h"

int Solution::numIslands(vector<vector<char>>& grid){
    int size = nums.size();
    vector<int> dp(size, 0);
    dp[0] = nums[0];
    int currentMax = dp[0];

    for(int i =1; i < size; i++){
        dp[i] = max(nums[i], nums[i] + dp[i-1]);
        currentMax = max(dp[i], currentMax);
    }
    return currentMax;
}




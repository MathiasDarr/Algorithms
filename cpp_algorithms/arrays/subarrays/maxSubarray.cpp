#include <iostream>
#include <vector>
using namespace std;

class Solution{
public:

    void coolSaying(){
        cout << "preaching" << endl;
    }


    int maxSubArray(vector<int>& nums){
        int size = nums.size();
        vector<int> dp(size, 0);
        dp[0] = nums[0];
        int maxx = dp[0];

        for(int i=1; i<size; i++){
            dp[i] = max(nums[i], nums[i] + dp[i-1]);
            maxx = max(dp[i], maxx);
        }

        return maxx;
    }
};

int main()
{

    vector<int> nums{-2,1,-3,4,-1,2,1,-5,4};

    Solution solution;
    int m = solution.maxSubArray(nums);

    cout << "The maximum subarray within nums is "  << m << endl;
    return 0;
}

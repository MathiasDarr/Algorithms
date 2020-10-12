#include <iostream>
#include "arrays/Solution.h"
#include <vector>

using namespace std;

int main() {
    std::cout << "Hello, World!" << std::endl;
    Solution solution;
    vector<int> nums{-2,1,-3,4,-1,2,1,-5,4};

    cout << "The maximum value of this subarray is " << solution.maxSubArray(nums) << endl;

    return 0;
}

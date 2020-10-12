#include<iostream>
#include <vector>
#include <unordered_set>


using namespace std;

 struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode() : val(0), left(nullptr), right(nullptr) {}
      TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
      TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };
 

class Solution{
public:
    bool findTarget(TreeNode* root, int k){
        return findTarget(root, k, unordered_set<int>() = {});
    }
    bool findTarget(TreeNode* root, int k, unordered_set<int>& hashSet){
        if(root == nullptr)
            return false;
        if(hashSet.find(k-root->val) != hashSet.end())
            return true;
        hashSet.insert(root->val);
        return findTarget(root->left, k, hashSet) || findTarget(root->right, k, hashSet);
    }


    vector<int> twoSum(vector<int>& numbers, int target){
        int left = 0;
        int right = numbers.size()-1;
        while(left<right){
            if(numbers[left]+numbers[right]==target){
                return {left+1,right+1};
            }else if(numbers[left]+numbers[right]<target){
                left++;
            }else if(numbers[left]+numbers[right]>target){
                right--;
            }
        }
        return {};
    }

};

void printVector(vector<int> const &a ){
    cout << "The vector elements are : " << endl;
    for(int i=0; i < a.size(); i++){
        cout << a.at(i) << ' ';
    }
}


int main(){

    // vector<int> numbers{2,7,11,15};
    // int target = 9;
    // Solution solution;
    // vector<int> result = solution.twoSum(numbers, target);
    // printVector(result);
    //cout << numbers << endl;

    TreeNode root{5};
    TreeNode left{3};
    TreeNode right{6};
    TreeNode leftleft{2};
    TreeNode leftright{4};
    TreeNode rightright{7};
    
    root.left = &left;
    root.right = &right;
    root.left->left = &leftleft;
    root.left->right = &leftright;
    root.right->right = &rightright;


    Solution solution;
    cout << solution.findTarget(&root, 29) << endl;


}
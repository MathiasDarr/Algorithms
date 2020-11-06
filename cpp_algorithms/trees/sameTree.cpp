//
// Created by mddarr on 10/16/20.
//

#include <iostream>
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
    bool isSameTree(TreeNode* p, TreeNode* q){
        if(p == nullptr && q == nullptr){
            return true;
        }else if(p == nullptr | q == nullptr){
            return false;
        }else if(p->val != q-> val){
            return false;
        }else{
            return isSameTree(p->left, q->left) && isSameTree(p->right, q->right );
        }
    }
};
int main(){
    TreeNode root1{1};
    TreeNode left{2};
    TreeNode right{3};

    root1.left = &left;
    root1.right = &right;



    TreeNode root2{1};
    TreeNode left2{2};
    TreeNode right2{3};

    root2.left = &left2;
    root2.right = &right2;

    Solution solution;
    cout << "The two trees are the same " << solution.isSameTree(&root1, &root2);

}

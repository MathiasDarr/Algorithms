#include <iostream>
#include <vector>
#include <queue>
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
    int minDepth(TreeNode* root){
        if(!root){
            return 0;
        }
        int depth = 0
        
        queue<TreeNode*> q;
        q.push(root);
        
        while(!queue.empty()){
            int n = q.size();
            depth++;

            while(n--){
                TreeNode *node q.front();
                q.pop();
                if(node->left== NULL && node->right == NULL){
                    return depth;
                }
                if(node->left){
                    q.push(node->left);
                }
                if(node->right){
                    q.push(node->right)
                }
            }

        }
        
        
        return 99;



    }


    // int minDepth(TreeNode* root){
    //     if(!root) return 0;
    //     int lh = minDepth(root->left);
    //     int rh = minDepth(root->right);

    //     // be careful, it's the height to leaves
    //     if(!root->left) return 1+rh;
    //     if(!root->right) return 1+lh;
    //     return 1 + min(lh , rh);
    // }
};

int main()
{
    TreeNode root{2};
    TreeNode left{9};
    TreeNode right{20};
    TreeNode rightLeft{15};
    TreeNode rightright{7};
    root.left = &left;
    root.right = &right;
    root.right->left = &rightLeft;
    root.right->right = &rightright;

    Solution solution;

    cout << "hello " << solution.minDepth(&root) << endl;
    
    
    return 0;
}

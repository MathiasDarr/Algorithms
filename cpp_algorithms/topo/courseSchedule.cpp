#include <iostream>
#include <vector>

using namespace std;
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        return true;
    }
};
// class Solution{

//     bool canFinish(int n, vector<vector<int>>& prerequisites){
//         vector<vector<int>> G(n);
//         vector<int> degree(n,0);
//         vector<int> bfs;
        
//         for(auto& e: prerequisites){
//             G[e[1]].push_back(e[0]);
//             degree[e[0]]++;
        
//         }
//         return true;
//     }

// };


int main(){
    vector<vector<int>> pre{{1,0}, {0,1}};
    Solution solution;

    bool canFinish = solution.canFinish(2,pre);
    cout << "Can I finish the courses " << canFinish << endl;

}
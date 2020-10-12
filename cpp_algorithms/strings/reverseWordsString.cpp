#include <iostream>
#include <vector>
#include <queue>
#include <sstream>
using namespace std;

class Solution {
public:
    string reverseWords(string s) {
        string word;
        string res;
        stringstream ss(s);
        while(ss >>word){
            res = word + " " + res;
        }
        return res.substr(0, res.size()-1);
    }
};



int main(){
    string s = "the sky is blue";
    cout << s << endl;
    Solution solution;
    string revs = solution.reverseWords(s);
    cout << revs << endl;

}
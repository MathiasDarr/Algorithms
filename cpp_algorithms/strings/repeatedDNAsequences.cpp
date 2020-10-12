#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        if(s.length<11)
            return {};


        unordered_set<string> results;
        unordered_set<string> hashSet;
        int i;
        for(i=0; i<s.length()-9; i++){
            string newS = s.substr(i,10);
            if(hashSet.find(newS) != hashSet.end()){
                results.insert(newS);
            }
            hashSet.insert(newS);
        }
        vector<string> result;
        for(auto x:results){
            result.push_back(x);
        }
        return result;    

    }
};


void printVector(vector<string> const &a ){
    cout << "The vector elements are : " << endl;
    for(int i=0; i < a.size(); i++){
        cout << a.at(i) << ' ';
    }
}

int main(){
    string s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT";
    Solution solution; 
    vector<string> results = solution.findRepeatedDnaSequences(s);
    printVector(results);

}


#include<iostream>
#include<vector>
#include <unordered_map> 


using namespace std;



class Solution{
public:
    bool isBipartite(vector<vector<int>>& graph){
        unordered_map<int, int> adjlist;
        for(int i =0; i < graph.size(); i++){
            adjlist.insert({graph[i][0], graph[i][1]});
            adjlist.insert({graph[i][1], graph[i][0]});
        }
        return true;
    }




};

template<typename K, typename V>
void print_map(unordered_map<K,V> const &map)
{
    for(auto const& pair:map){
        cout << "{" << pair.first << ":" << pair.second << "}" << endl;
    }
}


int main(){
    vector<vector<int>> graph {{1,3},{0,2}, {1,3}, {0,2}};
    unordered_map<int, char> map ={
        {1,'a'},
        {2, 'b'}
    };
    print_map(map);
    return 0;
    // print_map(graph);

    // cout << graph[0][1] << endl;

    // Solution solution;
    // bool isBipartite = solution.isBipartite(graph);
    // cout << "the graph is biPartite " << solution.isBipartite(graph) << endl;

}
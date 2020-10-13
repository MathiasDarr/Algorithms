//
// Created by mddarr on 10/13/20.
//
#include <iostream>
#include <vector>

#define ROW 4
#define COL 5

using namespace std;

class Solution {
private:
    const vector<vector<int>> directions = {{0,1}, {0,-1}, {-1, 0}, {1,0}};

    void dfs(int i, int j, int nRows, int nCols, vector<vector<char>>& grid){
        if(i >= 0 && i < nRows && j >= 0 && j < nCols && grid[i][j] =='1'){
            grid[i][j] ='0';
            for(vector<int> direction: directions){
                this->dfs(i+direction[0], j + direction[1], nRows, nCols, grid);
            }
        }
    }

public:
    int numIslands(vector<vector<char>>& grid) {
        int nRows = grid.size();
        int nCols = grid[0].size();

        int count = 0;
        int i;
        int j;
        for(i =0; i < nRows; i++){
            for(j = 0; j < nCols; j++){
                if(grid[i][j] == '1'){
                    count++;
                    this->dfs(i, j, nRows, nCols, grid);
                }
            }
        }
        return count;
    }
};



int main(){
    vector<vector<char>> grid = {  {'1','1','0','0','0'},
                                          {'1','1','0','0','0'},
                                          {'0','0','1','0','0'},
                                          {'0','0','0','1','1'}};
//    cout << "The first element is " << firstVector[0][0] << endl;

    Solution solution;
    int count = solution.numIslands(grid);
    cout << "The number of islands is " << count << endl;

    return 0;
}
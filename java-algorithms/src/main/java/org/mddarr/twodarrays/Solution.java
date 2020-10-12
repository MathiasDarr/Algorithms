package org.mddarr.twodarrays;

public class Solution {
    public int[][] directions = {
        {0,1}, {1,0}, {0,-1}, {-1,0}
    };
    public void sinkDFS(char[][] grid, int i, int j){
        if(i >=0 && i< grid.length && j >= 0 && j < grid[0].length){
            if(grid[i][j] == '1'){
                grid[i][j] = '0';
                for(int k = 0; k < directions.length; k++){
                    int newi = directions[k][0] + i;
                    int newj = directions[k][1] + j;
                    sinkDFS(grid, newi, newj);
                }
            }
        }
    }

    public int numIslands(char[][] grid){
        int n = grid.length;
        int m = grid[0].length;
        int output = 0;
        for(int i=0; i < n; i++){
            for(int j=0; j < m; j++){
                if(grid[i][j] == '1'){
                    sinkDFS(grid, i, j);
                    output +=1;
                }
            }
        }
        return output;
    }



}

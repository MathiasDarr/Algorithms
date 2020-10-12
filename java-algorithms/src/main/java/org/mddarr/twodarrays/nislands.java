package org.mddarr.twodarrays;

public class nislands {
    public static void main(String[] args){
        char[][] grid ={
                {'1','1', '1','0','1'},
                {'1','1', '0','0','0'},
                {'0','0', '0','0','0'},
                {'1','0', '0','1','1'},
        };
        Solution solution = new Solution();
        System.out.println("The number of islands in this grid is "+ solution.numIslands(grid));
    }

}

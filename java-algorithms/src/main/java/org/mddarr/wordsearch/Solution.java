package org.mddarr.wordsearch;

import java.util.HashSet;

public class Solution {
    int[][] directions = {
            {0,1}, {-1,0}, {1,0}, {0,-1}
    };
    public boolean dfs(char[][] board, int index, String word, int m, int n, HashSet<int[]> seen){
        if(index==word.length()-1){
            return  true;
        }
        for(int i=0; i < directions.length; i++) {
            int[] direction = directions[i];
            int newx = m+ direction[0];
            int newy = n + direction[1];
            if(newx >=0 && newx < board.length && newy >=0 && newy < board[0].length){

            }
        }
        if(word.indexOf(index) != board[m][n]) {
            return false;
        }
        return false;
    }

    public  boolean exist(char[][] board, String word){
        for(int i =0; i < board.length; i++){
            for(int j = 0; j<board.length; j++){
                if(board[i][j] == word.indexOf(0)){
                    HashSet<int[]> seen = new HashSet<>();
                    seen.add(new int[]{i, j});
                    if(dfs(board, 0, word, i, j, seen))
                        return true;
                }
            }
        }
        return false;
    }
}

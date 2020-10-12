package org.mddarr.wordsearch;

public class WordSearch {

    public static void main(String[] args){
        Solution solution = new Solution();
        char[][] board = {
                {'A','B','C','E'},
                {'S', 'F', 'C', 'S'},
                {'A', 'D', 'E', 'E'}
        };
        System.out.println(" The word has been found" + solution.exist(board, "SEE"));
    }




}

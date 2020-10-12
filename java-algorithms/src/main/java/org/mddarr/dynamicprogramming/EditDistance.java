package org.mddarr.dynamicprogramming;

public class EditDistance {
    public static void main(String[] args) {
        String word1 = "intention";
        String word2 = "execution";
        Solution solution = new Solution();
        System.out.println("The minimum edit distance is " + solution.minDistance(word1, word2));

    }
}

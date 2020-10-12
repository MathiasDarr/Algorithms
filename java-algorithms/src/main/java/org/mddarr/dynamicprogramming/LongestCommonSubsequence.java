package org.mddarr.dynamicprogramming;

public class LongestCommonSubsequence {
    public static void main(String[] args) {
        String text1 = "AGGTAB";
        String text2 = "GXTXAYB";
        Solution solution = new Solution();
        System.out.println("The longest common subsequence is " + solution.longestCommonSubsequence(text1, text2));
    }
}

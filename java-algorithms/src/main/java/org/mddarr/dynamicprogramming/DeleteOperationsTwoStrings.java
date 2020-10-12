package org.mddarr.dynamicprogramming;

public class DeleteOperationsTwoStrings {
    public static void main(String[] args) {
        String word1 = "sea";
        String word2 = "eat";
        Solution solution = new Solution();

        System.out.println("The minimum number of deletes is " + solution.minDeletesTwoStrings(word1, word2));

    }


}

package org.mddarr.strings;

public class Palindrome {
    public static void main(String[] args){
//        String s = "A man, a plan, a canal: Panama";
        String s = "A man, a plan, a canal: Panama";

        Solution solution = new Solution();
        boolean ispalindrome = solution.isValidPalindrome(s);

        System.out.println("and s is a palindrome  " + ispalindrome);

//        System.out.println(s.replac eAll(" ",""));
    }

}

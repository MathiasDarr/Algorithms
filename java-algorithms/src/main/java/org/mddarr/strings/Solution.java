package org.mddarr.strings;

import java.util.HashSet;
import java.util.Set;

public class Solution {
    private static Set<Character> vowels =
            new HashSet<>() {
                {
                    add('a');
                    add('e');
                    add('i');
                    add('o');
                    add('u');
                    add('A');
                    add('E');
                    add('I');
                    add('O');
                    add('U');
                }
            };

    public String toGoatLatin(String S) {
        String suff = "";
        StringBuilder sb = new StringBuilder();

        for(String tok: S.split(" ")){
            suff += 'a';
        }

        return "";
    }

    public int lengthOfLastWord(String s) {
        String[] strings = s.split(" ");

        if(strings.length ==0)
            return 0;

        String lastword = strings[strings.length-1];

        return lastword.length();
    }

    public boolean isValidPalindrome(String s){
        String stripped = s.replaceAll("[^a-zA-Z0-9]","");
        System.out.println(stripped);
        System.out.println(stripped.substring(0,1));
        int n = stripped.length();
        stripped = stripped.toLowerCase();
        for(int i =0; i< n/2;i++){
            System.out.println("s of i is " + stripped.substring(i,i+1));
            System.out.println(("s of n - i " + stripped.substring(n-i-1, n-i)));
            if(!stripped.substring(i, i + 1).equals(stripped.substring(n - i - 1, n - i)))

                return false;
        }

        return true;
    }

}

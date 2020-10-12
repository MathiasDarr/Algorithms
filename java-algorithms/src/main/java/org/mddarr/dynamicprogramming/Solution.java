package org.mddarr.dynamicprogramming;

public class Solution {



    public int longestCommonSubsequence(String text1, String text2) {
        int m = text1.length();
        int n = text2.length();

        int[][] dp = new int[m+1][n+1];
        for(int i =1; i<=m; i++){
            for(int j=1; j<=n; j++){
                if(text1.charAt(i-1)==text2.charAt(j-1)){
                    dp[i][j] = dp[i-1][j-1] +1;
                }else{
                    dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
                }
            }
        }
        return dp[m][n];
    }


    public int minDeletesTwoStrings(String s1, String s2) {
        int[][] dp = new int[s1.length()+1][s2.length()+1];

        for(int i =0; i <= s1.length(); i++){
            for(int j =0; j <= s2.length(); j++){
                if(i==0 || j ==0 ){
                    dp[i][j] = i+j;
                }
                else if(s1.charAt(i-1) == s2.charAt(j-1)){
                    dp[i][j] = dp[i-1][j-1];
                }else{
                    dp[i][j] = Math.min(dp[i-1][j],dp[i][j-1]) +1;
                }
            }
        }

        return dp[s1.length()][s2.length()];
    }


    public int minDistance(String word1, String word2) {

        int m = word1.length();
        int n = word2.length();

        int[][] dp = new int[m+1][n+1];

        for(int i =1; i < m+1; i++){
            dp[i][0] =i;
        }
        for(int j =1; j< n+1; j++){
            dp[0][j] = j;
        }

        for(int i =1; i < m+1; i++ ){
            for(int j=1; j < n+1; j++){
                if(word1.charAt(i-1) != word2.charAt(j-1)){
                    dp[i][j] = Math.min(dp[i-1][j], Math.min(dp[i-1][j-1],dp[i][j-1])) +1;
                }else{
                    dp[i][j] = dp[i-1][j-1];
                }
            }
        }
        return dp[m][n];
    }



    public int rob(int[] nums){
        if(nums.length ==0) return 0;
        int dp[] = new int[nums.length +1];
        dp[0] = 0;
        dp[1] = nums[0];
        for(int i =1; i < nums.length; i++){
            dp[i+1] = Math.max(dp[i], dp[i-1] + nums[i]);
        }
        return dp[nums.length];
    }

    public int climbStairs(int n){
        if(n==1){
            return 1;
        }
        int[] dp = new int[n+1];
        dp[1] = 1;
        dp[2] = 2;
        for(int i =3; i <= n; i++){
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }

//    public int numDecodings(String s, int decodePointer, int[] dp){
//        if(decodePointer >= s.length()){
//            return 1;
//        }
//        if(dp[decodePointer] > -1){
//            return dp[decodePointer];
//        }
//        int totalDecompositions =0;
//        for(int i =1; i <= 2; i++){
//            if(decodePointer +i <= s.length()){
//                String snippet = s.substring(decodePointer, decodePointer+i);
//            }
//        }
//    }

    public boolean isValid(String s){
            if(s.length() ==0 || s.charAt(0) =='0'){
                return false;
            }
            int value = Integer.parseInt(s);
            return value >= 1 && value <= 26;
    }



//    public int decodeWays(String s){
//        int[] dp = new int[s.length()+1];
//        dp[0] = 1;
//        dp[1] = s.charAt(0);
//        for(int i = 0; i < s.length(); i++){
//            int oneDigit = Integer.valueOf(s.substring(i-1, i));
//            int twoDigits = Integer.valueOf(s.substring(i-2, i));
//            if(oneDigit >= 1){
//                dp[i] += dp[i-1];
//            }
//            if(twoDigits >= 10 && twoDigits<=26){
//                dp[i] += dp[i-2];
//            }
//        }
//    }

}

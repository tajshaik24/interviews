/**
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
 */
class Solution {
    public String longestPalindrome(String s) {
        if(s == null || s.length() < 2){
            return s;
        } 
        int len = s.length(), startIndex = 0, endIndex = 0;
        int[] dp = new int[len];        
        for(int j = 1; j < len; j++){
            for(int i = 0; i < j; i++){
                dp[i] = dp[i + 1] == 0 && s.charAt(i) == s.charAt(j) ? 0 : 1;
                if(dp[i] == 0 && (j - i) > (endIndex - startIndex)){
                    endIndex = j;
                    startIndex = i;
                }
            }
        }
        return s.substring(startIndex, endIndex + 1);
    }
}
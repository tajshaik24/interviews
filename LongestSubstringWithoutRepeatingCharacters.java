/*Given a string, find the length of the longest substring without repeating characters.
Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", which the length is 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring. 
*/
class Solution {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> contains = new HashSet<>();
        int ans = 0, i = 0, j = 0;
        while (i < s.length() && j < s.length()) {
            if (!contains.contains(s.charAt(j))){
                contains.add(s.charAt(j++));
                ans = Math.max(ans, j - i);
            }
            else {
                contains.remove(s.charAt(i++));
            }
        }
        return ans;
    }
}